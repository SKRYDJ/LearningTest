'''
1 На странице https://esia-portal1.test.gosuslugi.ru/ найти все элементы по xpath //input и заполнить логин/пароль.
    Не заполнять те поля, которые имеют type="hidden".
2 Про Page Object. Описать BasePage, AuthPage(https://esia-portal1.test.gosuslugi.ru/),
    ProfilePage(https://esia-portal1.test.gosuslugi.ru/profile/user/personal, открывается после авторизации успешной).
    В BasePage реализовать методы 2 метода поиска элементов. get_element(ищет и возвращает 1 элемент)
    и get_elements(поиск нескольких элементов). Использовать WebDriverWait.
    Использовать правило для поиска 1 элемента visibility_of_element_located,
    для двух элементов visibility_of_any_elements_located.
    Методы должны принимать в себя selector_type, selector, timeout(задать значение по умолчанию для параметра).
    Использовать методы get_element и get_elements для реализации Page Object.
    Реализовать метод text_is_displayed(text, timeout=10) в base_page, который принимает в себя text
    (текст, который необходимо искать на странице) и timeout(поставить значение по умолчанию).
    Искать текст по XPATH, используя contains text().
    Если элемент найден, вернуть True, иначе False, учесть, что Selenium выкидывает исключение, если элемент не найден.
    assert current_page.text_is_displayed(text='LOGIN EXCEPTION TEXT', timeout=10)
3 Написать тесты, используя Page Object.
3.1 Ввод некорректного значения в поле login и поиск ошибки c помощью text_is_displayed.
3.2 Ввод некорректного значения в поле password и поиск ошибки c помощью text_is_displayed.
3.3 Ввод корректных значения и проверка, что оказались на странице ProfilePage.
'''



