from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=23)

    # TODO переключите темную тему в зависимости от времени суток

    if 6 < current_time.hour < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if 6 < current_time.hour < 22 and dark_theme_enabled_by_user is None:
        is_dark_theme = False
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = None

    # TODO найдите пользователя с именем "Olga"
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет

    suitable_users = [user for user in users if user['age'] < 20]

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def custom_rename(func, *args):
    func_rename = func.__name__.replace('_', ' ').title().upper()
    args_rename = ", ".join([*args])
    print(f"{func_rename} [{args_rename}]")
    return f"{func_rename} [{args_rename}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = custom_rename(open_browser, browser_name)
    assert actual_result == "OPEN BROWSER [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = custom_rename(go_to_companyname_homepage, page_url)
    assert actual_result == "GO TO COMPANYNAME HOMEPAGE [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = custom_rename(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "FIND REGISTRATION BUTTON ON LOGIN PAGE [https://companyname.com/login, Register]"
