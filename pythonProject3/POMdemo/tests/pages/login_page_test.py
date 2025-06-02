from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.userName_textbox = (By.XPATH, "//input[@id='employee_id']")
        self.password_textbox = (By.XPATH, "//input[@id='password']")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.userName_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def login_button_click(self):
        self.driver.find_element(*self.submit_button).click()
