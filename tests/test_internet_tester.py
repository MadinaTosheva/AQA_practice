from playwright.sync_api import expect
from pathlib import Path

from pages.allerts_page import AlertsPage
from pages.base_page import BasePage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.file_upload_page import UploadFilePage
from pages.hovers_page import HoverPage
from pages.input_page import InputPage
from pages.login_page import LoginPage
from pages.login_success_page import LoginSuccessPage
from pages.main_page import MainPage


def test_task_01(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    title = main_page.get_page_title()

    assert "the-internet" in title, "Неправильный заголовок"
    print(f"Сайт доступен. Заголовок: {title}")


def test_task_02(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_login()

    login_page_url = LoginPage(page).get_page_url()

    assert "/login" in login_page_url, "Неверный заголовок"
    print(f"Перешли в: Form Authentication | URL: {login_page_url}")


def test_task_03(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_login()

    login_page = LoginPage(page)
    login_page.login_as("tomsmith", "SuperSecretPassword!")

    login_success_page_url = LoginSuccessPage(page).get_page_url()

    assert "/secure" in login_success_page_url, "Неверный заголовок"
    print(f"Успешный вход! URL: {login_success_page_url}")


def test_task_04(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_login()

    login_page = LoginPage(page)
    login_page.login_as("tomsmith", "SuperSecretPassword!")
    login_url = login_page.get_page_url()

    login_success_page = LoginSuccessPage(page)
    login_success_page.logout()

    assert "/login" in login_url
    print(f"Успешный выход! URL: {login_url}")


def test_task_05(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_checkboxes()

    checkbox_page = CheckboxPage(page)

    assert checkbox_page.is_checked() == True
    assert checkbox_page.is_unchecked() == False

    checkbox_page.check_outbox()
    checkbox_page.uncheck_outbox()

    print(f"Checkbox 1: checked = {checkbox_page.is_unchecked()}\n"
          f"Checkbox 2: checked =  {checkbox_page.is_checked()}")


def test_task_06(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_dropdown()

    dropdown = DropdownPage(page)
    dropdown.select_option("Option 1")
    option_1_text = dropdown.get_selected_text()
    print(option_1_text)
    assert "Option 1" in option_1_text

    dropdown.select_option("Option 2")
    option_2_text = dropdown.get_selected_text()
    print(option_2_text)
    assert "Option 2" in option_2_text

    print(f" Выбрано: {option_2_text}")


def test_task_07(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_inputs()

    input_page = InputPage(page)
    input_page.fill_input_with('123')
    data = input_page.get_input_value()
    assert data == '123'
    input_page.clear_input()

    input_page.fill_input_with('456')
    data2 = input_page.get_input_value()
    assert data2 == '456'
    print(f'Введено: {data2}')


def test_task_08(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_hovers()

    hovers_page = HoverPage(page)
    hovers_page.hover_mouse_on_element()
    hovers_page.wait_element_to_be_visible()
    ele_text = hovers_page.get_element_text()

    assert ele_text == 'name: user1'

    print("Навели на изображение. Текст: name: user1")


def test_task_09(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_alerts()

    alerts_page = AlertsPage(page)
    alerts_page.go_to_jsAllert()
    alerts_page.accept_allert()


def test_task_10(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_fileUpload()

    file_upload_page = UploadFilePage(page)
    file_upload_page.create_txt_file("test_upload.txt")
    file_upload_page.write_text_into_file("Hello Playwright")
    file_upload_page.upload_file()
    file_upload_page.wait_uploaded_file_to_be_visible()
    file_name = file_upload_page.get_file_name()

    assert file_name == "test_upload.txt"
    print(f'✅ Файл загружен: {file_name}')


def test_task_11(page):
    main_page = MainPage(page)
    main_page.open_main_page()
    main_page.go_to_dynamicLoading()

    dynamic_loading_page = DynamicLoadingPage(page)
    dynamic_loading_page.go_to_example1()
    dynamic_loading_page.click_on_start_button()
    dynamic_loading_page.expect_text_to_be_visible()
    text = dynamic_loading_page.get_element_text()

    assert text == "Hello World!"
    print(f'✅ Элемент появился: {text}')


def test_task_12(page):

    file_dir = Path("../output/screenshots/")
    file_dir.mkdir(parents=True, exist_ok=True)

    BasePage().navigate_to_example(page, "Form Authentication")
    screen_path = file_dir / "Form_Authentication.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()
    assert page.url == URL

    BasePage().navigate_to_example(page, "Checkboxes")
    checkbox1 = page.locator("(//form[@id = 'checkboxes']/input)[1]")
    checkbox2 = page.locator("(//form[@id = 'checkboxes']/input)[2]")
    checkbox1.check()
    checkbox2.uncheck()
    assert checkbox1.is_checked() == True
    assert checkbox2.is_checked() == False
    screen_path = file_dir / "Checkboxes.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()

    BasePage(page).navigate_to_example("Dropdown")
    dropdown_loc = page.locator('#dropdown')
    dropdown_loc.select_option(label="Option 2")
    selected_text = page.locator('[selected="selected"]')
    option_2_text = selected_text.inner_text()
    assert "Option 2" in option_2_text
    screen_path = file_dir / "Dropdown.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()

    BasePage().navigate_to_example(page, "Inputs")
    input_number_loc = page.locator("[type='number']")
    input_number_loc.fill('999')
    field_data = input_number_loc.input_value()
    assert field_data == '999'
    screen_path = file_dir / "Inputs.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()

    BasePage().navigate_to_example(page, "Hovers")
    figure_loc = page.locator('(//div[@class="example"]/div/img)[1]')
    hidden_info_locator = page.locator('(//div[@class="figcaption"]/h5)[1]')
    figure_loc.hover()
    assert hidden_info_locator.is_visible()
    assert hidden_info_locator.inner_text() == 'name: user1'
    screen_path = file_dir / "Hovers.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()

    print("📊 ОТЧЁТ:\n"
          "✅ Form Authentication \n"
          "✅ Checkboxes\n"
          "✅ Dropdown\n"
          "✅ Inputs\n"
          "✅ Hovers\n"
          "Все тесты пройдены!")
