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

from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Selectores
    ADDRESS_INPUT = (By.ID, "address-input")
    TARIFA_COMFORT = (By.XPATH, "//button[contains(text(),'Comfort')]")
    PHONE_INPUT = (By.ID, "phone")
    CREDIT_CARD_INPUT = (By.ID, "card-number")
    EXPIRATION_INPUT = (By.ID, "expiration")
    CVV_INPUT = (By.ID, "cvv")
    LINK_CARD_BUTTON = (By.CSS_SELECTOR, ".button-link-card")
    MESSAGE_INPUT = (By.ID, "message")
    BLANKET_BUTTON = (By.ID, "blanket")
    TISSUES_BUTTON = (By.ID, "tissues")
    ICE_CREAM_BUTTON = (By.ID, "ice-cream")
    SEARCH_MODAL = (By.ID, "search-modal")
    DRIVER_INFO = (By.ID, "driver-info")

    def __init__(self, driver):
        self.driver = driver

    def configure_address(self, address):
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def select_tarifa_comfort(self):
        self.driver.find_element(*self.TARIFA_COMFORT).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone_number)

    def add_credit_card(self, card_number, expiration, cvv):
        self.driver.find_element(*self.CREDIT_CARD_INPUT).send_keys(card_number)
        self.driver.find_element(*self.EXPIRATION_INPUT).send_keys(expiration)
        self.driver.find_element(*self.CVV_INPUT).send_keys(cvv)
        # Simula el evento de perder el foco para activar el botón
        self.driver.find_element(*self.CVV_INPUT).send_keys(Keys.TAB)

    def enter_phone_code(self, code):
        # Método para ingresar el código de confirmación
        self.driver.find_element(*self.PHONE_INPUT).send_keys(code)

    def write_message(self, message):
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.BLANKET_BUTTON).click()
        self.driver.find_element(*self.TISSUES_BUTTON).click()

    def request_ice_cream(self, quantity):
        for _ in range(quantity):
            self.driver.find_element(*self.ICE_CREAM_BUTTON).click()

    def is_searching_for_taxi_modal_displayed(self):
        # Verifica que el modal de búsqueda esté visible
        return self.driver.find_element(*self.SEARCH_MODAL).is_displayed()

    def is_driver_info_displayed(self):
        # Verifica que la información del conductor esté visible
        return self.driver.find_element(*self.DRIVER_INFO).is_displayed()

