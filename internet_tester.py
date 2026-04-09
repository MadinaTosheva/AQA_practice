import pytest
from playwright.sync_api import sync_playwright, expect
from pathlib import Path


URL = "https://the-internet.herokuapp.com/"

@pytest.fixture
def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        yield page

        browser.close()


def navigate_to_example(page, example_name: str):
    page.locator(f"text = {example_name}").click()
    return page.url


def test_task_01(launch_browser):
    page = launch_browser

    title_locator = page.locator(".heading").text_content()
    assert "the-internet" in title_locator, "Неправильный заголовок"
    print(f"Сайт доступен. Заголовок: {title_locator}")


def test_task_02(launch_browser):
    page = launch_browser

    auth_page = navigate_to_example(page, "Form Authentication")
    print(auth_page)
    assert "/login" in auth_page, "Неверный заголовок"
    print(f"Перешли в: Form Authentication | URL: {auth_page}")


def test_task_03(launch_browser):
    page = launch_browser

    navigate_to_example(page, "Form Authentication")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name = "Login").click()

    assert "/secure" in page.url, "Неверный заголовок"
    print(f"Успешный вход! URL: {page.url}")


def test_task_04(launch_browser):
    page = launch_browser

    navigate_to_example(page, "Form Authentication")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Logout").click()

    assert "/login" in page.url
    print(f"Успешный выход! URL: {page.url}")


def test_task_05(launch_browser):
    page = launch_browser
    navigate_to_example(page, "Checkboxes")
    checkbox1 = page.locator("(//form[@id = 'checkboxes']/input)[1]")
    checkbox2 = page.locator("(//form[@id = 'checkboxes']/input)[2]")

    assert checkbox1.is_checked() == False
    assert checkbox2.is_checked() == True

    checkbox1.check()
    checkbox2.uncheck()

    assert checkbox1.is_checked() == True
    assert checkbox2.is_checked() == False

    print(f"Checkbox 1: checked = {checkbox1.is_checked()}\n"
          f"Checkbox 2: checked =  {checkbox2.is_checked()}")


def test_task_06(launch_browser):
    page = launch_browser

    navigate_to_example(page, "Dropdown")
    dropdown_loc = page.locator('#dropdown')
    assert page.locator('#dropdown>option:first-child').inner_text() == "Please select an option", "Неверный локатор"

    dropdown_loc.select_option(label="Option 1")
    selected_text = page.locator('[selected="selected"]')
    option_1_text = selected_text.inner_text()
    print(option_1_text)
    assert "Option 1" in option_1_text

    dropdown_loc.select_option(label="Option 2")
    selected_text = page.locator('[selected="selected"]')
    option_2_text = selected_text.inner_text()
    print(option_2_text)
    assert "Option 2" in option_2_text

    print(f" Выбрано: {option_2_text}")


def test_task_07(launch_browser):
    page = launch_browser
    navigate_to_example(page, "Inputs")
    input_number_loc = page.locator("[type='number']")
    input_number_loc.fill('123')
    field_data = input_number_loc.input_value()
    assert field_data == '123'
    input_number_loc.clear()
    input_number_loc.fill('456')
    field_data = input_number_loc.input_value()
    assert field_data == '456'
    print(f'Введено: 456')


def test_task_08(launch_browser):
    page = launch_browser
    navigate_to_example(page, "Hovers")
    figure_loc = page.locator('(//div[@class="example"]/div/img)[1]')
    hidden_info_locator = page.locator('(//div[@class="figcaption"]/h5)[1]')
    figure_loc.hover()
    assert hidden_info_locator.is_visible()
    assert hidden_info_locator.inner_text() == 'name: user1'

    print("Навели на изображение. Текст: name: user1")


def test_task_09(launch_browser):
    page = launch_browser
    navigate_to_example(page, "JavaScript Alerts")
    page.locator('[onclick="jsAlert()"]').click()
    page.on("dialog", lambda dialog: dialog.accept())


def test_task_10(launch_browser):
    page = launch_browser

    navigate_to_example(page, "File Upload")
    new_file = Path("test_upload.txt")
    new_file.write_text("Hello Playwright")

    page.locator("#file-upload").set_input_files(new_file)
    page.locator("#file-submit").click()
    uploaded_file = page.locator("#uploaded-files")
    expect(uploaded_file).to_be_visible()

    assert uploaded_file.inner_text() == new_file.name
    print(f'✅ Файл загружен: {new_file.name}')


def test_task_11(launch_browser):
    page = launch_browser

    navigate_to_example(page, "Dynamic Loading")
    page.get_by_role("link", name="Example 1").click()
    page.get_by_role("button", name="Start").click()

    text_loc = page.locator("#finish>h4")
    expect(text_loc).to_be_visible()

    assert text_loc.inner_text() == "Hello World!"
    print(f'✅ Элемент появился: {text_loc.inner_text()}')


def test_task_12(launch_browser):
    page = launch_browser

    file_dir = Path("output/screenshots/")
    file_dir.mkdir(parents=True, exist_ok=True)

    navigate_to_example(page, "Form Authentication")
    screen_path = file_dir / "Form_Authentication.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()
    assert page.url == URL

    navigate_to_example(page, "Checkboxes")
    checkbox1 = page.locator("(//form[@id = 'checkboxes']/input)[1]")
    checkbox2 = page.locator("(//form[@id = 'checkboxes']/input)[2]")
    checkbox1.check()
    checkbox2.uncheck()
    assert checkbox1.is_checked() == True
    assert checkbox2.is_checked() == False
    screen_path = file_dir / "Checkboxes.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()

    navigate_to_example(page, "Dropdown")
    dropdown_loc = page.locator('#dropdown')
    dropdown_loc.select_option(label="Option 2")
    selected_text = page.locator('[selected="selected"]')
    option_2_text = selected_text.inner_text()
    assert "Option 2" in option_2_text
    screen_path = file_dir / "Dropdown.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()

    navigate_to_example(page, "Inputs")
    input_number_loc = page.locator("[type='number']")
    input_number_loc.fill('999')
    field_data = input_number_loc.input_value()
    assert field_data == '999'
    screen_path = file_dir / "Inputs.png"
    page.screenshot(path=screen_path, full_page=True)
    page.go_back()

    navigate_to_example(page, "Hovers")
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
