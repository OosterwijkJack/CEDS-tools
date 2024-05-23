# header to get login page
def get_header():
    return {
  
  "Host": "www5.ipg-online.com",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
  "Accept-Encoding": "gzip, deflate, br",
  "DNT": "1",
  "Sec-GPC": "1",
  "Connection": "keep-alive",
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "none",
  "Sec-Fetch-User": "?1"
}

# header to post to login page
def login_header(cookie):
  return {
  "Host": "www5.ipg-online.com",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
  "Accept-Encoding": "gzip, deflate, br",
  "Content-Type": "application/x-www-form-urlencoded",
  "Content-Length": "329",
  "Origin": "https://www5.ipg-online.com",
  "DNT": "1",
  "Sec-GPC": "1",
  "Connection": "keep-alive",
  "Referer": "https://www5.ipg-online.com/vt/login",
  "Cookie": cookie,
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1"
}

# header to get order page
def order_page_header(cookie):
   return {
  "Host": "www5.ipg-online.com",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
  "Accept-Encoding": "gzip, deflate, br",
  "Connection": "keep-alive",
  "Referer": "https://www5.ipg-online.com/vt/newlogin.faces",
  "Cookie": cookie,
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin"
}

# header to post to order page
def form_header(cookie):
   return {
    "Host": "www5.ipg-online.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "5607",
    "Origin": "https://www5.ipg-online.com",
    "Connection": "keep-alive",
    "Referer": "https://www5.ipg-online.com/vt/view/pos/orderData.faces?transactionType=default",
    "Cookie": cookie,
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

def confirm_post_headers(cookie):
  return {
  "Host": "www5.ipg-online.com",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
  "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
  "Accept-Encoding": "gzip, deflate, br",
  "Content-Type": "application/x-www-form-urlencoded",
  "Content-Length": "252",
  "Origin": "https://www5.ipg-online.com",
  "Connection": "keep-alive",
  "Referer": "https://www5.ipg-online.com/vt/view/pos/orderData.faces",
  "Cookie": cookie,
  "Upgrade-Insecure-Requests": "1",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1"
}

