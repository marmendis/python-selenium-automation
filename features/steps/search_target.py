import elements
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given("I open the Target homepage")
def homepage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.target.com")
    time.sleep(3)

@when('I search for "{product}"')
def product(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(product)
    search_box.submit()
    time.sleep(3)

@when("I add the first product to the cart")
def product(context):
    driver = context.driver
add_buttons = context.driver.find_element(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']")

# Scroll into view in case it's offscreen
driver.execute_script("arguments[0].scrollIntoView(true);", add_button)

# Click the button
add_button.click()

@When("choose option")
def options(context):
    # click "Choose Options" if it exists
    try:
        choose_button = driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
        choose_button.click()
        time.sleep(2)
    except:
        pass

    # click "Add to Cart" button
    add_button = driver.find_element(By.CSS_SELECTOR,
                                     "[data-test='orderPickupButton'], [data-test='orderShippingButton']")
    add_button.click()
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
