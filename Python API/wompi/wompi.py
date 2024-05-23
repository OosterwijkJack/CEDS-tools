import requests
from bs4 import BeautifulSoup
import os,sys

current_working_directory = os.path.join(os.getcwd(), "wompi")

if current_working_directory not in sys.path:
    sys.path.append(current_working_directory)

from requestData import post_requests
from requestData import request_headers
from requestData.country_codes import two_to_three_letter_codes

import time
import datetime

#import flask

# urls
login_page = r"https://www5.ipg-online.com/vt/login"
login_post_url = r"https://www5.ipg-online.com/vt/newlogin.faces"
order_page  = r"https://www5.ipg-online.com/vt/view/pos/orderData.faces?transactionType=default"
form_post_url = r"https://www5.ipg-online.com/vt/view/pos/orderData.faces"
show_order_result_url = r"https://www5.ipg-online.com/vt/view/pos/showOrderResult.faces"
confirm_order_post_url = r"https://www5.ipg-online.com/vt/view/pos/confirmOrder.faces"

def get_cc_link(form_data):
    print("Request received ...\n")
    cc_url = ""
    with requests.Session() as s:
        form_page = login(s) # login to whompi
        submitted_page = submit_form(s, form_page, form_data) # page with cc link
        cc_url = get_payment_link_from_html(submitted_page) # get cc link
        s.close() # close session

    print("Success")
    return cc_url

        
def submit_form(s: requests.sessions.Session, form_page, form_data):
    internal_data = get_page_tokens(form_page.text)
    CRSF_token = internal_data[0]
    view_state = internal_data[1]

    form_post_data = get_form_data(CRSF_token,view_state, form_data['order_number'], form_data['subtotal'], form_data['delivery_amount'], form_data['currency'], form_data['name1'], form_data['name2'], 
    form_data['address1'], form_data['address2'], form_data['city'], form_data['province'], form_data['country'], form_data['post_code'], form_data['phone'],form_data['fax'],form_data['email'],
    form_data['comment'])

    post_form_data(s,form_post_data)
    submitted_page = confirm_form_data(s,post_requests.confirm_post_request(CRSF_token, view_state))
    return submitted_page


def login(s: requests.sessions.Session):
    # set headers
    page_header = request_headers.get_header() 
    s.headers = page_header

    data = s.get(login_page)
    
    # CRSF token and view state found in html login page
    internal_data = get_login_tokens(data.text)
    CRSF_token = internal_data[0] # get token
    view_state = internal_data[1]

    login_request = post_requests.login_request(CRSF_token, view_state) # get json request

    form_page = post_login_Wompi(s,login_request,request_headers.login_header(cookie_to_string(s.cookies))) # login to whompi and return page
    return form_page

# post customer data to form
def post_form_data(s:requests.sessions.Session,data):
    post = s.post(form_post_url, data, headers=request_headers.form_header(cookie_to_string(s.cookies)), allow_redirects=True)  
    time.sleep(3)

    print("post code:",post.status_code)

#confirm the post data
def confirm_form_data(s:requests.sessions.Session, data):
    post = s.post(confirm_order_post_url, data, headers=request_headers.confirm_post_headers(cookie_to_string(s.cookies)), allow_redirects=True)
    time.sleep(3)
    print("Post confirm status code:",post.status_code)
    return post.text

# returns post data needed to creater cc link
def get_form_data(token,view, order_number, subtotal, deliver_amount, currency,name1,name2,address1,address2,
city,province,country,post_code,phone,fax,email,comment):
    
    now = datetime.datetime.now()
    expiry = datetime.datetime(now.year, now.month+1, now.day).strftime("%d/%m/%Y") # expiry date one month from now

    country = two_to_three_letter_codes(country) # 3 letter country code

    total = "{:.2f}".format(float(subtotal) + float(deliver_amount))

    form_data = post_requests.form_post_request(token,view,expiry,order_number,subtotal,deliver_amount,total,currency,str(now.year), name1, name2, address1, address2, 
    city,province,country,post_code,phone,fax,email,comment)

    return form_data


# login to payment gateway
def post_login_Wompi(s:requests.sessions.Session, post_data, headers):
    inside = s.post(login_post_url,post_data, headers=headers,allow_redirects=True) # send login data 
    time.sleep(3) # pause for site to load
    print("login status code:",inside.status_code)

    form_page = s.get(order_page, headers=request_headers.order_page_header(cookie_to_string(s.cookies))) # actual page where the cc links are submitted
    return form_page


# tokens in main page after logging in
def get_page_tokens(html):
    soup = BeautifulSoup(html, features='html.parser')

    search = soup.find('body')
    search = search.findNext("div", attrs={'class': "bodyPage"})
    search = search.findNext("div", attrs={'class': "pageWrap"})
    search = search.findNext("div", attrs={'id': "infoPanel"})

    token = search.findNext("input", attrs={'name': "CSRF_TOKEN"})['value']
    view = search.findNext("input", attrs={'name': "javax.faces.ViewState"})['value']

    return[token,view]

# parse CSRF and view state from login page
def get_login_tokens(html):
    soup = BeautifulSoup(html, features='html.parser')

    search = soup.find('body')
    search = search.findNext('div', attrs={'id': "content"})
    search = search.findNext("form")


    token = search.findNext('input', attrs={'name': "CSRF_TOKEN"})['value']
    state = search.findNext('input', attrs={'name': 'javax.faces.ViewState'})['value']

    return([token,state])


def get_payment_link_from_html(html):
    soup = BeautifulSoup(html, features='html.parser')
    search = soup.find("body")
    search = search.findNext("div", attrs={"class": "bodyPage"})
    search = search.findNext('div', attrs={"id": "container"})
    search = search.findNext("div", attrs={"id": "center", 'class': "column"})
    search = search.findNext("form", attrs={"id": "orderResultForm"})
    search = search.findNext('div', attrs={"id": "sectionId-", "class":"section"})
    search = search.findNext('div', attrs={"class": "sectionContent"})
    search = search.findNext('table', attrs={"class": "sectionTable"})
    search = search.findNext('span', attrs={"id": "paymentUrlText"}).text

    return(search)

def cookie_to_string(cookie):
    return "; ".join([str(x)+"="+str(y) for x,y in cookie.items()]) # convert cookies to string


if __name__ == "__main__":
    get_cc_link()