from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/dynamic_loading/2"
EXPECTED = "Hello World!"

def test_dynamic_loading_selenium(driver):
    wait = WebDriverWait(driver,10)

    driver.get(URL)
    selector = (By.CSS_SELECTOR,"#start button") # ID=start, Tag=button

    # driver.find_element(By.CSS_SELECTOR,"#start button")
    wait.until(EC.element_to_be_clickable(selector)).click()

    flash_locator = (By.ID,"finish")
    flash_msg = wait.until(
        EC.visibility_of_element_located(flash_locator)
    ).text

    assert EXPECTED in flash_msg.strip()
