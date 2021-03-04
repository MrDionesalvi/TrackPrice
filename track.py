
import time
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
import json

pathJson = "O:/Dione-dev/Imparo-Python/TrackPrice/siti.json"
pathDriver = "O:/Dione-dev/Imparo-Python/TrackPrice/driver/chromedriver.exe"
data = json.load(open(pathJson))

globalPrice = "1000"

while True:
    browser = webdriver.Chrome(executable_path=pathDriver)
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

    time.sleep(6)
    browser.quit()
    print("\nGiro Finito\n")
    time.sleep(20)