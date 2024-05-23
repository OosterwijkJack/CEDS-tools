from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os,sys

current_working_directory = os.path.join(os.getcwd(), "government")

if current_working_directory not in sys.path:
    sys.path.append(current_working_directory)

import country_codes_sp as country

import data
import time

cService = None
driver = None

logged_in = False
cService = webdriver.FirefoxService(GeckoDriverManager().install())

#customer_data = {"name": "first", "address": "address", 
                # "city": "city", "state": "state", "post": "post", "order_id": "12345",
                 #  "country": "US", "cc": True }

def get_government_invoice(customer_data):
    global driver, logged_in, cService
    # go to login page
    invoice_number = 0
    try:
        # login to website
        if(not logged_in):
            driver = webdriver.Firefox(service=cService)
            login_firefox()
            login()
            logged_in = True

        # generate the document
        invoice_number = generate_document(customer_data)

    except Exception as e:
        logout()
        driver.close()
        print(f"Error: {str(e)}")
        exit()
        

    ask = input("Was operation succesfull? (y/n) ").lower()

    while(ask != "y" or ask != "yes" or ask != "n" or ask != "no"):
        if (ask == "n" or ask == "no"):
            raise ValueError
        if(ask == "y" or ask == "yes"):
            break
        else:
            ask = input("Was operation succesfull? (y/n) ").lower()
    
        
    # exit session

    if invoice_number != 0:
        return invoice_number
    
    raise ValueError


def generate_document(customer_data):
    global driver
    tmp = None
    driver.get(data.urls.gen_doc) # go to generate documents page

    waitForLoad(data.Xpaths.generate_document_enter)
    time.sleep(2)
    # opens dropdown and selects option
    # doc type
    driver.find_element(By.XPATH, data.Xpaths.doc_type_dropdown).click()
    waitForLoad(data.document_values.document_type_option)
    driver.find_element(By.XPATH, data.document_values.document_type_option).click()    

    # branch
    driver.find_element(By.XPATH, data.Xpaths.brach_dropdown).click()
    waitForLoad(data.document_values.branch_option)
    driver.find_element(By.XPATH, data.document_values.branch_option).click()

    # Spot
    driver.find_element(By.XPATH, data.Xpaths.spot_dropdown).click()
    waitForLoad(data.document_values.spot_option)
    driver.find_element(By.XPATH, data.document_values.spot_option).click()

    # add customer button
    driver.find_element(By.XPATH, data.Xpaths.add_customer_button).click()
    waitForLoad(data.document_values.customer_type_option)

    # customer type dropdown select
    driver.find_element(By.XPATH, data.Xpaths.customer_type_dropdown).click()
    waitForLoad(data.document_values.customer_type_option)
    driver.find_element(By.XPATH, data.document_values.customer_type_option).click()

    # customer name
    waitForLoad(data.Xpaths.name)
    driver.find_element(By.XPATH, data.Xpaths.name).send_keys(customer_data["name"].split()[0])
    driver.find_element(By.XPATH, data.Xpaths.last_name).send_keys(customer_data["name"].split()[-1])

    # customer address
    address_str = customer_data["address"] + " " + customer_data["city"] + " " + customer_data["state"] + " " + customer_data["post"]
    driver.find_element(By.XPATH, data.Xpaths.address).send_keys(address_str)

    # select passport as id
    driver.find_element(By.XPATH, data.Xpaths.id_type).click()
    waitForLoad(data.document_values.id_type_option)
    driver.find_element(By.XPATH, data.document_values.id_type_option).click()

    # "passport number"
    driver.find_element(By.XPATH, data.Xpaths.passport_number).send_keys(customer_data["order_id"] + customer_data["country"])

    # selecting dropdowns by text
    # select country
    tmp = driver.find_element(By.XPATH, data.Xpaths.foreign_country_button).click()
    waitForLoad(data.Xpaths.foreign_country_last)
    tmp = driver.find_element(By.XPATH, data.Xpaths.foreign_country_input)
    tmp.send_keys(country.codes[customer_data["country"]])
    tmp.send_keys(Keys.ENTER)

    # email
    driver.find_element(By.XPATH, data.Xpaths.email).send_keys("info@ceds.dev")
    driver.find_element(By.XPATH, data.Xpaths.keep_customer_button).click()
    time.sleep(1.5)
    
    # select warehouse
    driver.find_element(By.XPATH, data.Xpaths.warehouse_code).click()
    waitForLoad(data.Xpaths.warehouse_code)
    driver.find_element(By.XPATH, data.document_values.warehouse_code).click()

    # select purchased product
    tmp = driver.find_element(By.XPATH, data.Xpaths.product_select).click()
    waitForLoad(data.Xpaths.product_line)
    tmp = driver.find_element(By.XPATH, data.Xpaths.product_search)
    tmp.send_keys(customer_data["product"])
    time.sleep(2)
    tmp.send_keys(Keys.ENTER)

    # add prouct
    driver.find_element(By.XPATH, data.Xpaths.add_product).click()

    # product quantity
    waitForLoad(data.Xpaths.product_quantity)
    tmp = driver.find_element(By.XPATH, data.Xpaths.product_quantity)
    tmp.clear()
    quantity = customer_data['quantity']+ ".00"
    tmp.click()
    tmp.send_keys(quantity)

    # shipping cost field but really tell wether customer bought with pp or cc
    driver.find_element(By.XPATH, data.Xpaths.shipping_cost_drop).click()
    waitForLoad(data.Xpaths.shipping_cost_text)
    tmp = driver.find_element(By.XPATH, data.Xpaths.shipping_cost_text)
    tmp.clear()
    tmp.click()
    value = "45.00" if customer_data["cc"] else "20.00"
    tmp.send_keys(value)
    
    # get invoice number
    invoice = driver.find_element(By.XPATH, data.document_values.invoice_number).get_attribute("value")
    driver.find_element(By.XPATH, data.Xpaths.generate_document_enter).click()

    return invoice.lstrip("0")


def login():
    global driver
    driver.get(data.urls.login_page)
    waitForLoad(data.Xpaths.login_load)


    # enter login
    username_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(data.login.email)
    password_field.send_keys(data.login.password)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, data.Xpaths.login_enter)
    submit_button.click()

    waitForLoad(data.Xpaths.start_page_last)


def logout():
    global driver, logged_in
    driver.get(data.urls.sign_off)
    time.sleep(2)
    logged_in = False

def waitForLoad(Xpath):
    global driver
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Xpath)))
    time.sleep(1)

def login_firefox():
    email = None
    pwd = None

    with open(os.path.join(os.getcwd(), "government", "firefox login.txt"), 'r') as f:
        read = f.readlines()
        email = read[0].replace("\n", "")
        pwd = read[1].replace("\n", "")

    global driver
    driver.get("https://accounts.firefox.com/")
    
    waitForLoad("/html/body/div[3]/div/div/section/form/div[1]/input")
    driver.find_element(By.XPATH ,"/html/body/div[3]/div/div/section/form/div[1]/input").send_keys(email)
    driver.find_element(By.XPATH ,"//*[@id=\"submit-btn\"]").click()

    waitForLoad("//*[@id=\"password\"]")

    driver.find_element(By.XPATH, "//*[@id=\"password\"]").send_keys(pwd)
    driver.find_element(By.XPATH, "//*[@id=\"submit-btn\"]").click()
    
    input("Enter when logged in")

