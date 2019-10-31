from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators
from pages.locators import CartPageLocators
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    
    def test_guest_should_see_login_link_on_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    #Гость открывает главную страницу 
    link = MainPageLocators.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    #Переходит в корзину по кнопке в шапке сайта
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    #Ожидаем, что в корзине нет товаров
    cart_page.cart_should_be_empty()
    #Ожидаем, что есть текст о том что корзина пуста      
