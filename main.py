from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import os


def transliterate(input='કેમ છો'):
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
    driver.get('https://www.anirdesh.com/gujarati/unicode-to-english.php')

    textarea_id = driver.find_element_by_id('text-uni')
    for i in range(16):
        textarea_id.send_keys(Keys.BACKSPACE)
    textarea_id.send_keys(input)

    convert_button = driver.find_element_by_xpath(
        "//*[@id='controls']/table/tbody/tr/td[3]")
    convert_button.click()

    # output_id = driver.find_element_by_id('text_hari')
    page_html = driver.page_source
    page_soup = bs(page_html, 'lxml')
    output_soup = page_soup.find(id='text_hari')
    return output_soup.text


if __name__ == "__main__":
    print(transliterate())
