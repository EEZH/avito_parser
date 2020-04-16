from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string
from pytesseract import pytesseract
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

firefox_options = Options()
firefox_options.add_argument('-headless')
pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Евгений\Desktop\Python\Parsing\geckodriver.exe', options=firefox_options)
        # self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def tel_recon(self):
        image2 = Image.open('tel.gif')
        phone_num = image_to_string(image2)
        return phone_num


    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x, y, x+width, y+height)).save('tel.gif')
        result = self.tel_recon()
        return result

    def but_gettr(self):
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a [@class="button item-phone-button js-item-phone-button button-origin contactBar_greenColor button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card contactBar_height"]'))).click()


    def navigate(self, link=None):
        while True:
            try:
                self.driver.get(link)
                # self.driver.get('https://www.avito.ru/tyumen/kvartiry/2-k_kvartira_53.7_m_110_et._1911035607')
                self.but_gettr()
                sleep(4)
                self.take_screenshot()
                image = self.driver.find_element_by_xpath('//div [@class="item-phone-big-number js-item-phone-big-number"]//*')

                location = image.location
                size = image.size

                image = Image.open('avito_screenshot.png')
                x = location['x']
                y = location['y']
                width = size['width']
                height = size['height']

                image.crop((x, y, x+width, y+height)).save('tel.gif')
                self.crop(location, size)
                self.driver.quit()
                return self.crop(location, size)
            except Exception:
                self.driver.quit()
                break



