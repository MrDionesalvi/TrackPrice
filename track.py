
import time
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
import json

Path = "O:/Dione-dev/Imparo-Python/TrackPrice/siti.json"
data = json.load(open(Path))

globalPrice = "1000"

while True:
    browser = webdriver.Chrome(executable_path='O:/Dione-dev/Things/chromedriver.exe')
    for i in data:
        browser.get(data[i]['link'])

        try:
            instock = browser.find_element_by_xpath(data[i]['class']['stock'])
            if instock:
                print("\nProdotto Disponibile:")
                pricew = browser.find_element_by_xpath(data[i]['class']['price'])
                if pricew:
                    str_w = pricew.text
                    digits=str_w.strip('€').replace('.','')
                    price = digits[:digits.index(',')]
                    price = str(digits)
                    print("Prezzo "+ data[i]['nome'] + ": " + price)
                    if price < globalPrice:
                        print("Economico mando notifica")
        except(NoSuchElementException):
            print("\nNon disponibile")

    browser.quit()
    time.sleep(20)
    print("\nGiro Finito \n")