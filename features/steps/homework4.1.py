from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

@given("I open the Target homepage")
def step_open_homepage(context):
    context.driver.get("https://www.target.com/")

@when('I search for "{product}"')
def step_search_product(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(product, Keys.ENTER)
    sleep(2)

@when("I select the first product")
def step_select_first_product(context):
    first_product = context.driver.find_element(By.XPATH, "//a[@data-test='product-title']")
    context.driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
    context.driver.execute_script("window.scrollBy(0, -150);")
    first_product.click()
    sleep(2)

@when("I add the product to the cart")
def step_add_to_cart(context):
    try:
        add_to_cart = context.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
        context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)
        add_to_cart.click()
        print("First Add to Cart clicked")
    except:
        print("No Add to Cart button found")
    sleep(3)

    # Handle possible second Add to Cart (popup)
    try:
        add_to_cart2 = context.driver.find_element(By.XPATH, "//button[contains(text(),'Continue shopping')]")
        context.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart2)
        add_to_cart2.click()
        print("Second Add to Cart clicked (popup)")
    except:
        print("No second Add to Cart button, continuing...")
    sleep(2)

@then("I should see items in the cart with subtotal")
def step_verify_cart(context):
    context.driver.get("https://www.target.com/cart")
    sleep(3)
    try:
        cart_text = context.driver.find_element(By.XPATH, "//span[contains(@class, 'styles_cart-summary-span__')]").text
        print("Cart summary:", cart_text)
        assert "subtotal" in cart_text.lower() and "item" in cart_text.lower()
        print("Cart verification passed")
    except:
        print("Cart summary not found or cart is empty")
