from playwright.sync_api import sync_playwright
import os

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url="http://localhost:8000")
        with page.expect_response("**") as response_info:
            page.get_by_role("button").click()

        response = response_info.value
        response.finished()
        response_body = response.body()
        with open("saved_output.pdf", "wb") as new_file: 
            new_file.write(response_body)


        saved_output_size = os.stat("saved_output.pdf").st_size
        example_pdf_size = os.stat("example_pdf.pdf").st_size
        assert saved_output_size == example_pdf_size


if __name__ == "__main__":
    main()