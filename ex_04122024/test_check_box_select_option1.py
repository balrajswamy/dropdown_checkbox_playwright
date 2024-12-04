import pytest
import allure
from playwright.sync_api import sync_playwright, Page,expect
import time


@pytest.fixture(scope="function")
def setup_teardown():
    """Fixture to initialize and teardown Playwright browser and page."""
    playwright = sync_playwright().start()  # Start Playwright
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Load the login page
    page.goto("https://awesomeqa.com/practice.html")
    page.wait_for_load_state("networkidle")
    time.sleep(3)  # Reduce unnecessary sleep time
    yield page  # Provide the page object to tests

    # Teardown
    context.close()
    browser.close()
    playwright.stop()  # Ensure Playwright is properly stopped

@pytest.mark.positive
def test_checkbox_dropdown(setup_teardown):
    """
    this is working with selected date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown
    #clicking at checkboxes to click at automation tester
    page.locator("//input[@value='Automation Tester']").click()
    # clicking at checkboxes to click at manual tester
    time.sleep(1)
    page.locator("//input[@value='Manual Tester']").click()
    time.sleep(3)
    #to select south america
    try:

        page.locator("//select[@id='continents']").select_option(index=2)
        print("\nselect africa using select index")
    except:
        print("\n select index is not working")
    time.sleep(5)
    try:

        page.locator("#continents").select_option("South America")
        print("\nSelected South America using select_option")
    except:
        page.locator("//select[@id='continents']/option[5]").select_option(5)
        print("\nSelected South America using Xpath")

    time.sleep(3)

    try:
        page.locator("//select[@id='selenium_commands']/option[3]").click()
        print("\nSelected with Switch Commands using Xpath")
    except:
        page.locator("//select[@id='selenium_commands']").select_option("Switch Commands")
        print("\nSelected with Switch Commands using select_option")
    time.sleep(3)

#page.locator("//select[@id='continents']").select_option(label="South America")


def test_select_text():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com//dropdown")  # Replace "URL" with the actual URL
        time.sleep(1)
        #page.locator("//select[@id='dropdown']").click()
        time.sleep(3)

        try:
            #using visible text
            page.locator("//select[@id='dropdown']").select_option("Option 2")
        except:
            #using index value inside the tag
            page.locator("//select[@id='dropdown']").select_option("2")
        time.sleep(3)
        context.close()
        browser.close()
