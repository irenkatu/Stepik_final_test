from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.locators import ProductPageLocators
import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


#Список ссылок для нахождения битой ссылки
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


@pytest.mark.skip
@pytest.mark.need_review  
def test_guest_can_add_product_to_basket(browser):
    #Первая ссылка на которой проверяли
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #Вторая ссылка, чтоб проверить независимость данных
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    #Открываем браузер
    page.open()
    #Смотрим что за книжка и почем
    Bookname=page.find_book_name()
    Bookprice=page.find_book_price()
    #Добавляем в корзинку и решаем задачку
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    #Проверяем, что правильно добавили
    page.right_book_and_right_price_message(Bookname,Bookprice)

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_item_to_cart()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
 
@pytest.mark.skip
def test_guest_cant_see_success_message(browser): 
#Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_item_to_cart()
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The message has not dissappeared"


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK
    page = ProductPage(browser, link)
    # Гость открывает страницу товара
    page.open()
    #Переходит в корзину по кнопке в шапке 
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    #Ожидаем, что есть текст о том что корзина пуста 
    cart_page.cart_should_be_empty()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

"""
@pytest.mark.need_review   
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                         # здесь нужно добавить логины и пароли
        page.add_to_basket()
        page1 = MainPage(browser, link) 
        page1.solve_quiz_and_get_code()
        page.should_be_message_about_add_item_to_basket()
        page.should_be_correct_price()"""


"""
test_user_can_add_product_to_basket

+++1)test_guest_can_add_product_to_basket

+++2)test_guest_cant_see_product_in_basket_opened_from_product_page

test_guest_can_go_to_login_page_from_product_page"""

