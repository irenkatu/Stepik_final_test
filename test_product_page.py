from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.locators import ProductPageLocators
from pages.locators import LoginPageLocators
import pytest
import time


link = ProductPageLocators.PRODUCT_PAGE_LINK


@pytest.mark.need_review  
def test_guest_can_add_product_to_basket(browser):
    #Первая ссылка на которой проверяли
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #Вторая ссылка, чтоб проверить независимость данных
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    #Открываем браузер
    page.open()
    #Смотрим что название и цену
    Bookname=page.find_book_name()
    Bookprice=page.find_book_price()
    #Добавляем в корзинку и решаем задачку
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    #Проверяем, что правильно добавили
    page.right_book_and_right_price_message(Bookname,Bookprice)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_item_to_cart()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()
 

def test_guest_cant_see_success_message(browser): 
    #Открываем страницу товара 
    page = ProductPage(browser, link)
    page.open()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.add_item_to_cart()
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_disappear()


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

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    #Открываем страницу браузера
    page = ProductPage(browser, link)
    page.open()
    #Проверяем, что можем зайти на страницу логина
    page.go_to_login_page()

@pytest.mark.auth_user
class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = LoginPageLocators.LOGIN_PAGE_LINK # Открываем ссылку на страницу логина\регистрации
        self.browser = browser
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
        page = LoginPage(browser, link)
	    # открываем нужную страницу
        page.open()
        # генерим тестовую почту, задаем пароль 
        email, password = page.make_email_and_pass()
        # регистрируем нового пользователя
        page.register_new_user(email, password)
        # проверяем, что пользователь авторизован
        page.should_be_authorized_user() # на деле такие проверки лучше не делать (setup не для этого)

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_LINK
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        # берем функции со страницы product_page	
        page = ProductPage(browser, link)
        # открываем страницу
        page.open()
        page.should_be_authorized_user()
        bookToCompare = page.find_book_name()
        priceToCompare = page.find_book_price()
        # добавляем товар в корзину
        page.add_item_to_cart()
        #проверка цены и наименования товара в корзине
        page.right_book_and_right_price_message(bookToCompare, priceToCompare)

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_LINK
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        #берем функции со страницы product_page
        page = ProductPage(browser, link)
	    # открываем страницу
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()



