from pathlib import Path
import re
import time

from playwright.sync_api import sync_playwright


def inspect_page(url: str, browser_type: str, headless: bool, screenshot: bool = False) -> dict:

    with sync_playwright() as p:

        success = False
        if browser_type == "chromium":
            browser = p.chromium.launch(headless= True, slow_mo=1000)
        if browser_type == "firefox":
            browser = p.firefox.launch(headless= True, slow_mo=1000)
        else:
            browser = p.webkit.launch(headless=True, slow_mo=1000)
        
        page = browser.new_page()

        start = time.perf_counter()
        page.goto(url)
        time.sleep(20)
        page.wait_for_load_state("load")
        load_time = round(time.perf_counter() - start, 2)

        title = page.title()


        if screenshot:
            file_dir = Path("output/screenshots/")
            file_dir.mkdir(parents=True, exist_ok= True)
            safe_name = re.sub(r'[^\w\-_]', '_', url)  # безопасное имя
            screen_path = file_dir / f"{browser_type}_{safe_name}.png"
            page.screenshot(path= screen_path, full_page=True)


        page.close()
        success = True


    return {
            "url": url,
            "browser": browser_type,
            "title": title,
            "success": success,
            "viewport": page.viewport_size,     # {'width': ..., 'height': ...}
            "url_final": page.url,
            "screenshot": screen_path,
            "load_time_sec": float(load_time)
}



if __name__ == "__main__":

    result = inspect_page(url = "https://example.com", browser_type= "chromium", headless= True, screenshot= True)

    print(f"[{result['browser']}] {result['title']}\n"
          f"Viewport {result['viewport']}\n"
          f"Финальный URL: {result['url_final']}\n"
          f"Скриншот: {result['screenshot']}\n"
          f"Загрузка: {result['load_time_sec']}с\n"
          )