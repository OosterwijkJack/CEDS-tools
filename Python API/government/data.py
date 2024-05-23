from dataclasses import dataclass

@dataclass
class Xpaths:


    # login page
    login_enter = "/html/body/div[2]/div/div/div/div/div/div[1]/div[2]/div/div[2]/form/div[3]/div/button"
    login_load = "/html/body/script[16]"

    # start page (page after loggin in)
    start_page_last = "/html/body/script[22]"

    spot_dropdown = "//*[@id=\"main-content\"]/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div/button"
    brach_dropdown = "//*[@id=\"sub\"]/div/button"
    doc_type_dropdown = "//*[@id=\"main-content\"]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/button"

    add_customer_button = "//*[@id=\"mostrar\"]"
    customer_type_dropdown = "//*[@id=\"new_custumer\"]/div/div[1]/div[1]/div/button"
    name = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[2]/div[3]/input"
    last_name = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[2]/div[4]/input"
    address = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[2]/div[5]/input"
    id_type = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[6]/div[1]/div/button"
    passport_number = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[6]/div[2]/input"
    foreign_country_button = "//*[@id=\"new_custumer\"]/div/div[6]/div[3]/div/button"
    foreign_country_last = "//*[@id=\"bs-select-24-248\"]"
    foreign_country_input = "//*[@id=\"new_custumer\"]/div/div[6]/div[3]/div/div/div[1]/input"
    email = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[7]/div[1]/input"
    receiver_country = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[8]/div/div/button"
    keep_customer_button = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[9]/button"
    warehouse_code = "//*[@id=\"main-content\"]/div[2]/div[5]/div/div/div[2]/div[2]/div/div[1]/div/button"
    product_select = "//*[@id=\"main-content\"]/div[2]/div[5]/div/div/div[2]/div[2]/div/div[2]/span"
    
    product_line = "//*[@id=\"select2-producto-results\"]/li[6]"
    product_search = "/html/body/span/span/span[1]/input"
    add_product = "//*[@id=\"addRow\"]"
    product_quantity = "//*[@id=\"quantity1\"]"
    shipping_cost_drop = "//*[@id=\"main-content\"]/div[2]/div[7]/div/div/div[1]/div/i"
    shipping_cost_text = "//*[@id=\"acarreo_totalizado\"]"

    generate_document_enter = "//*[@id=\"btn-send-success\"]"
    


@dataclass
class login:
    email = "removed"
    password = "removed"

@dataclass
class urls:
    login_page = "https://factura.thefactoryhka.com.pa/"
    gen_doc = "https://factura.thefactoryhka.com.pa/invoices/create"
    sign_off = "https://factura.thefactoryhka.com.pa/auth/logout"

@dataclass
class document_values:
    document_type_option = "/html/body/section/section/section/form/section/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/ul/li[8]/a"
    spot_option = "/html/body/section/section/section/form/section/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div[2]/ul/li[2]/a"
    branch_option = "/html/body/section/section/section/form/section/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/ul/li[2]/a"
    invoice_number = "/html/body/section/section/section/form/section/div[2]/div[1]/div/div/div[2]/div[1]/div[4]/input[2]"
    customer_type_option = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/ul/li[5]/a"
    id_type_option = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[6]/div[1]/div/div/div[2]/ul/li[3]/a"
    foreign_country_option = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[6]/div[3]/div/div/div[2]/ul/li[2]/a" # needs to be dynamic 
    receiver_country_option = "/html/body/section/section/section/form/section/div[2]/div[4]/div/div/div[2]/div[2]/div/div[8]/div/div/div/div[2]/ul/li[139]/a"
    warehouse_code = "//*[@id=\"bs-select-2-1\"]"

