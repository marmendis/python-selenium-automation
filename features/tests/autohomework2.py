from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Start Chrome in Incognito mode ---
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    # 1. Open Target.com
    driver.get("https://www.target.com/")

    # 2. Click Account button (top-right corner)
    account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "account"))
    )
    account_button.click()

    # 3. Click Sign In button from side navigation
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-test='accountNav-signIn']"))
    )
    sign_in_button.click()

    # 4. Verify Sign In page opened
    # Check "Sign in or create account" header
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Sign in or create account')]"))
    )
    print("✅ 'Sign in or create account' text is visible.")

    # Check Sign In button presence
    driver.find_element(By.ID, "login")
    print("✅ Sign In button is visible.")

finally:
    driver.quit()