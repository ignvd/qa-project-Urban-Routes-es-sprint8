from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # Selectores
    ADDRESS_INPUT = (By.ID, "address")
    COMFORT_TARIFF = (By.ID, "comfort")
    PHONE_INPUT = (By.ID, "phone")
    ADD_CARD_BUTTON = (By.ID, "add-card")
    CVV_FIELD = (By.ID, "code")
    MESSAGE_FIELD = (By.ID, "message")
    SUBMIT_BUTTON = (By.ID, "submit")
    SEARCH_MODAL = (By.ID, "search-modal")

    # Métodos
    def set_address(self, address):
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def select_tariff_comfort(self):
        self.driver.find_element(*self.COMFORT_TARIFF).click()

    def set_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def add_credit_card(self, cvv):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()
        self.driver.find_element(*self.CVV_FIELD).send_keys(cvv)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()  # Simula cambio de enfoque
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def send_message(self, message):
        self.driver.find_element(*self.MESSAGE_FIELD).send_keys(message)

    def wait_for_search_modal(self):
        modal = self.driver.find_element(*self.SEARCH_MODAL)
        assert modal.is_displayed(), "El modal de búsqueda no apareció."
