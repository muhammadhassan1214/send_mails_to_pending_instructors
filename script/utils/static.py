from selenium.webdriver.common.by import By


class Locators:
    # Login Page Locators
    SIGN_IN_BUTTON = (By.XPATH, "(//button[text()= 'Sign In | Sign Up'])[1]")
    USERNAME_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    SUBMIT_BUTTON = (By.ID, "btnSignIn")
    PROFILE_ICON = (By.XPATH, "//span[@title= 'Nathaniel Shell' and contains(@class, 'Header_userName')]")

    # Dashboard Page Locators
    TRAINING_CENTER_NAV = (By.CSS_SELECTOR, "button[id='Training Center']")
    ORGANIZATION_USERS_DROPDOWN = (By.CSS_SELECTOR, "button[title='Organization Users']")
    INSTRUCTORS_ANCHOR = (By.XPATH, "//a[text()='Instructors']/parent::div")
    SELECTED_ORGANIZATION = (By.XPATH, "(//div[text()='Shell CPR, LLC.'])[1]")
    ORGANIZATION_INPUT = (By.CSS_SELECTOR, "input[aria-label=Organization]")
    ORGANIZATION_TO_SELECT = (By.XPATH, "//div[@title='Shell CPR, LLC.' and text()='Shell CPR, LLC.']")


class ApiEndpoints:
    def get_headers(self: str) -> dict:
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'ext_id': 'dacbf678-f0cd-4f43-aaf0-7cd5058fb9f9',
            'origin': 'https://atlas.heart.org',
            'priority': 'u=1, i',
            'referer': 'https://atlas.heart.org/',
            'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'x-jwt-token': self
        }
        return headers
