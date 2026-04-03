import time

from playwright.sync_api import sync_playwright


URL = "https://the-internet.herokuapp.com/"

def navigate_to_example(example_name: str):
    page.locator(f"text = {example_name}").click()

    # page.locator("#username").fill("tomsmith")
    # page.locator("#password").fill("SuperSecretPassword!")
    # page.get_by_role("button", name = "Login").click()
    # page.get_by_role("link", name="Logout").click()
    # return page.url  # передаёт весь урл сайта
    #        #page.title()  # передаёт корень урл сайта

    # checkbox1 = page.locator("(//form[@id = 'checkboxes']/input)[1]")
    # checkbox2 = page.locator("(//form[@id = 'checkboxes']/input)[2]")
    #
    # assert checkbox1.is_checked() == False
    # assert checkbox2.is_checked() == True
    #
    # # checkbox1.click()
    # # checkbox2.click()
    # checkbox1.check()
    # checkbox2.uncheck()
    #
    # assert checkbox1.is_checked() == True
    # assert checkbox2.is_checked() == False
    #
    # return (f"Checkbox 1: checked = {checkbox1.is_checked()}\n"
    #        f"Checkbox 2: checked =  {checkbox2.is_checked()}

    # dropdown_loc = page.locator('#dropdown')
    # assert page.locator('#dropdown>option:first-child').inner_text() == "Please select an option", "Неверный локатор"
    #
    # dropdown_loc.select_option(label="Option 1")
    # selected_text = page.locator('[selected="selected"]')
    # option_1_text = selected_text.inner_text()
    # print(option_1_text)
    # assert "Option 1" in option_1_text
    #
    # dropdown_loc.select_option(label="Option 2")
    # selected_text = page.locator('[selected="selected"]')
    # option_2_text = selected_text.inner_text()
    # print(option_2_text)
    # assert "Option 2" in option_2_text
    #
    # return f" Выбрано: {option_2_text}"

    # input_number_loc = page.locator("[type='number']")
    # input_number_loc.fill('123')
    # field_data = input_number_loc.input_value()
    # assert field_data == '123'
    #
    # input_number_loc.clear()
    # input_number_loc.fill('456')
    # field_data = input_number_loc.input_value()
    # assert field_data == '456'
    #
    # return f'Введено: 456'

    # figure_loc = page.locator('(//div[@class="example"]/div/img)[1]')
    # hidden_info_locator = page.locator('(//div[@class="figcaption"]/h5)[1]')
    # figure_loc.hover()
    # assert hidden_info_locator.is_visible()
    # assert hidden_info_locator.inner_text() == 'name: user1'
    #
    # return "Навели на изображение. Текст: name: user1"

    page.locator('[onclick="jsAlert()"]').click()
    page.on("dialog", lambda dialog: dialog.accept())




if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        title_locator = page.locator(".heading").text_content()
        assert "the-internet" in title_locator, "Неправильный заголовок"
        print(f"Сайт доступен. Заголовок: {title_locator}")

        # auth_page = navigate_to_example("Form Authentication")
        # print(auth_page)
        # assert "/login" in auth_page, "Неверный заголовок"
        # print(f"Перешли в: Form Authentication | URL: {auth_page}")

        # assert "/secure" in auth_page, "Неверный заголовок"
        # print(f"Успешный вход! URL: {auth_page}")

        # assert "/login" in auth_page
        # print(f"Успешный выход! URL: {auth_page}")

        # checkbox_page = navigate_to_example("Checkboxes")
        # print(checkbox_page)

        # dropdown = navigate_to_example("Dropdown")
        # print(dropdown)

        # Inputs = navigate_to_example("Inputs")
        # print(Inputs)

        # hovers = navigate_to_example("Hovers")
        # print(hovers)

        alerts = navigate_to_example("JavaScript Alerts")
        print(alerts)

        browser.close()