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
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_load_state("networkidle")
    time.sleep(3)  # Reduce unnecessary sleep time
    yield page  # Provide the page object to tests

    # Teardown
    context.close()
    browser.close()
    playwright.stop()  # Ensure Playwright is properly stopped

@pytest.mark.positive
def test_click_alert(setup_teardown):
    page = setup_teardown

    try:
        # locate the web elements
        page.on("dialog", lambda dialog: dialog.accept())
        time.sleep(6)
        page.locator("//button[@onclick='jsAlert()']").click()
        print("\nALert confirm button clicked at popup!")

        # Alert popup will handled automatically we cannot find ok button at popup
    except:
        # locate the web elements

        page.locator("//button[@onclick='jsAlert()']").click()
        print("\nALert button clicked with popup passed!")

        # Alert popup will handled automatically we cannot find ok button at popup
    time.sleep(3)
    result_message = '//p[@id="result"]'
    page.wait_for_selector(result_message)
    success_message = page.locator(result_message).text_content()
    assert success_message == 'You successfully clicked an alert'


@pytest.mark.negative
def test_click_alert_confirm(setup_teardown):
    page = setup_teardown

    try:
        # locate the web elements
        page.on("dialog", lambda dialog: dialog.accept()) # to click at Ok button
        #page.on("dialog", lambda dialog: dialog.dismiss()) # to click at Cancel
        time.sleep(6)
        page.locator("//button[@onclick='jsConfirm()']").click()
        print("\nALert button clicked at popup!")

        # Alert popup will handled automatically we cannot find ok button at popup
    except:
        pass

        # Alert popup will handled automatically we cannot find ok button at popup
    time.sleep(3)
    result_message = '//p[@id="result"]'
    page.wait_for_selector(result_message)
    success_message = page.locator(result_message).text_content()
    assert success_message == 'You clicked: Ok'


@pytest.mark.smoke
def test_typing_alert_prompt(setup_teardown):
    page = setup_teardown

    try:
        # locate the web elements
        typing_txt = "Balaji!"

        page.on("dialog", lambda dialog: dialog.accept(typing_txt)) # to click at Ok button

        #page.on("dialog", lambda dialog: dialog.dismiss()) # to click at Cancel
        time.sleep(6)
        page.locator("//button[@onclick='jsPrompt()']").click()
        print("\nTyped at alert prompt as Balraj!")

        # Alert popup will handled automatically we cannot find ok button at popup
    except:
        pass

        # Alert popup will handled automatically we cannot find ok button at popup
    time.sleep(3)

    result_message = '//p[@id="result"]'
    page.wait_for_selector(result_message)
    success_message = page.locator(result_message).text_content()
    assert success_message == f'You entered: {typing_txt}'