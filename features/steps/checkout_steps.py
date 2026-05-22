from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Locators


@given("I am logged in to SauceDemo")
def step_login_to_saucedemo(context):
    context.wait = WebDriverWait(context.browser, 10)
    context.browser.get("https://www.saucedemo.com/")

    context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='username']"))
    ).send_keys("standard_user")
    context.browser.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys(
        "secret_sauce"
    )
    context.browser.find_element(By.CSS_SELECTOR, "[data-test='login-button']").click()

    context.wait.until(EC.url_contains("inventory.html"))


@given("I have items in my cart")
def step_add_items_to_cart(context):
    context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_BIKE_LIGHT))
    ).click()
    context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_TSHIRT))
    ).click()
    context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_ONESIE))
    ).click()
    context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.ADD_RED_TSHIRT))
    ).click()

    context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.CART_ICON))
    ).click()
    context.wait.until(EC.url_contains("cart.html"))
    cart_items = context.wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, Locators.CART_ITEM))
    )
    assert len(cart_items) == 4


@when('I checkout with first name "{first_name}", last name "{last_name}", and zip code "{zip_code}"')
def step_checkout(context, first_name, last_name, zip_code):
    checkout = context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.CHECKOUT_BTN))
    )
    context.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkout)
    checkout.click()
    context.wait.until(EC.url_contains("checkout-step-one.html"))

    first_name_input = context.wait.until(
        EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_FIRSTNAME))
    )
    first_name_input.clear()
    first_name_input.send_keys(first_name)

    last_name_input = context.wait.until(
        EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_LASTNAME))
    )
    last_name_input.clear()
    last_name_input.send_keys(last_name)

    zip_input = context.wait.until(
        EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_ZIP))
    )
    zip_input.clear()
    zip_input.send_keys(zip_code)

    context.wait.until(
        EC.element_to_be_clickable((By.ID, Locators.CHECKOUT_CONTINUE))
    ).click()
    context.wait.until(EC.url_contains("checkout-step-two.html"))

    context.wait.until(
        EC.element_to_be_clickable((By.ID, Locators.FINISH_BTN))
    ).click()


@then('I should see the order confirmation "{message}"')
def step_verify_order_confirmation(context, message):
    context.wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, Locators.ORDER_CONFIRMATION),
            message,
        )
    )
    confirmation = context.browser.find_element(
        By.CSS_SELECTOR,
        Locators.ORDER_CONFIRMATION,
    )
    assert message in confirmation.text
