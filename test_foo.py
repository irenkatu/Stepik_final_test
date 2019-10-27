#from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest
import time


#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


"""@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])"""

"""def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_cart()
   # product_page.solve_quiz_and_get_code()
    #product_page.check_add_item_to_basket()"""

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
#Добавляем товар в корзину
    #product_page = ProductPage(browser, browser.current_url)
    page.add_item_to_cart()
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
 

def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    #product_page = ProductPage(browser, browser.current_url)
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
#Добавляем товар в корзину
   # product_page = ProductPage(browser, browser.current_url)
    page.add_item_to_cart()
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

