from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given("I open the Target homepage")
def step_open_homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.target.com")
    time.sleep(3)

@when('I search for "{product}"')
def step_search_product(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(product)
    search_box.submit()
    time.sleep(3)

@when("I add the first product to the cart")
def step_add_first_product(context):
    driver = context.driver
        # Click the first product link
        first_product = driver.find_element(By.CSS_SELECTOR, 'a[data-test="product-title"]')
        first_product.click()
        time.sleep(3)

        # Find all possible add-to-cart buttons
        add_buttons = driver.find_elements(By.CSS_SELECTOR,
                                           'button[data-test="add-to-cart-button"], button[data-test="orderPickupButton"]')

        # Click the first button
        if add_buttons:
            add_buttons[0].click()
            print("Clicked the first Add to Cart button")
        else:
            print("No add-to-cart buttons found!")

time.sleep(3)


@then("I should see at least one item in the cart")
def step_verify_cart(context):
    driver = context.driver
    cart_icon = driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
    cart_icon.click()
    time.sleep(3)

    # Check cart items
    cart_items = driver.find_elements(By.CSS_SELECTOR, 'div[data-test="cart-item"]')
    assert len(cart_items) >= 1, "Cart is empty!"
    print(f"Test Passed: {len(cart_items)} item(s) in the cart")

    driver.quit()
