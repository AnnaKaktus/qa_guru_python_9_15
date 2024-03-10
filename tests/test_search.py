from selene.support.shared import browser
from selene import by
import allure


def test_search_by_author():
    with allure.step("Вводим в поле поиска имя автора"):
        browser.open("https://mybook.ru/dashboard/")
        browser.element("[placeholder=\"Книга или автор\"]").type("Ленин")
        browser.element(by.text("Государство и революция")).click()


def test_search_by_name():
    with allure.step("Вводим в поле поиска название книги"):
        browser.open("https://mybook.ru/dashboard/")
        browser.element("[placeholder=\"Книга или автор\"]").type("Государство и революция")
        browser.element(by.text("Ленин")).click()
