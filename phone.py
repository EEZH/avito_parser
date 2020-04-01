from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string
from pytesseract import pytesseract
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

firefox_options = Options()
firefox_options.add_argument('-headless')
pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Евгений\Desktop\Python\Parsing\geckodriver.exe')
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
        # button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a [@class="button item-phone-button js-item-phone-button button-origin contactBar_greenColor button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card contactBar_height"]'))).click()
        button = self.driver.find_element_by_xpath('//a [@class="button item-phone-button js-item-phone-button button-origin contactBar_greenColor button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card contactBar_height"]')
        button.click()



    def navigate(self, link=None):
        self.driver.get(link)

        # self.driver.get('https://www.avito.ru/tyumen/kvartiry/2-k_kvartira_53.7_m_110_et._1911035607')
        # sleep(3)
        # try:
        # button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a [@class="button item-phone-button js-item-phone-button button-origin contactBar_greenColor button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card contactBar_height"]'))).click()

        self.but_gettr()
        # button = self.driver.find_element_by_xpath('//a [@class="button item-phone-button js-item-phone-button button-origin contactBar_greenColor button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card contactBar_height"]')
        # button.click()

        sleep(4)
        self.take_screenshot()
        # image = self.pic_catch()
        while True:
            try:
                image = self.driver.find_element_by_xpath('//div [@class="item-phone-big-number js-item-phone-big-number"]//*')
                location = image.location
                size = image.size
                break
            except NoSuchElementException:
                continue



        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x, y, x+width, y+height)).save('tel.gif')
        self.crop(location, size)
        self.driver.quit()
        return self.crop(location, size)



# def main():
#     b = Bot()
#
#
# if __name__ == '__main__':
# #     main()
# b = Bot()
# x = b.navigate()
# print(x)
