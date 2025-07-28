from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_edot(driver):
    driver.get("https://esuite.edot.id")
    wait = WebDriverWait(driver, 10)

    # Klik tombol "Login"
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/button[1]'))).click()

    # Isi email
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/div[2]/div/input'))).send_keys("it.qa@edot.id")

    # Klik tombol Next
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/button'))).click()

    # Isi password
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/form/div/div/input'))).send_keys("it.QA2025")

    # Klik Login
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[3]/div/button'))).click()

    # Tambahkan assertion untuk memastikan login berhasil
    assert "dashboard" in driver.current_url or "home" in driver.current_url.lower()

