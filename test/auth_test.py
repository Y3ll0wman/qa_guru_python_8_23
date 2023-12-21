import allure


@allure.id("28364")
@allure.title("Auth via Google")
@allure.tag("web", "smoke")
@allure.story("External Auth")
@allure.feature("Auth")
@allure.label("msrv", "Auth")
@allure.label("owner", "allure8")
def test_google_auth():
    with allure.step("Открываем главную страницу"):
        pass
    with allure.step("Выбираем способ авторизации через Google"):
        pass
    with allure.step("Авторизуемся как пользователь Y3ll0wman"):
        with allure.step("Вводим пароль TestQA"):
            pass
        with allure.step("Вводим логин Y3ll0wman@gmail.com"):
            pass
        with allure.step("Нажимаем кнопку Войти"):
            pass
    with allure.step("Проверяем, что авторизовались успешно"):
        pass
    with allure.step("Проверяем, что данные из профиля обновились из Google"):
        with allure.step("Имя: Y3ll0wman"):
            pass
        with allure.step("Email: Y3ll0wman@gmail.com"):
            pass
