from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class_xpath = '//*[@id="ctl00_ContentPlaceHolderIcerik_grdDersler_ctl00_ctl12_btnDerseGir_input"]'

driver = webdriver.Chrome()

def xfind(xpath):
    return driver.find_element("xpath", xpath)

driver.get("https://eders.pusula.pau.edu.tr/CanliDers/OgrenciDersListesi.aspx")

xfind( '//*[@id="lvPusula_txtKullanici"]').send_keys(USERNAME)
xfind('//*[@id="lvPusula_txtSifre"]').send_keys(PASSWORD)

xfind('//*[@id="lvPusula_btnGiris"]').click()

xfind(class_xpath).click()

sleep(3)

i = 1
while 1:
    video_list = xfind('//*[@id="ctl00_ContentPlaceHolderIcerik_RadPageView3"]')
    driver.execute_script(
        "arguments[0].setAttribute('class', 'rmpView')", video_list)

    xfind('/html/body/form/div[5]/div[2]/div/div[2]/div/div[4]/div[2]/div/table/tbody/tr[' + str(i) + ']/td[4]/span/input[1]').click()

    try :
        save = driver.find_element(
            "xpath", '//*[@id="ctl00_ContentPlaceHolderIcerik_radWndMazeret_C_btnMazeretKaydet_input"]').click()
    except:
        pass

    sleep(1)
    driver.switch_to.window(window_name=driver.window_handles[1])
    driver.close()
    driver.switch_to.window(window_name=driver.window_handles[0])
    try:
        xfind('//*[@id="ctl00_apPusulaModal"]/div/div[3]/button').click()
    except:
        pass
    i += 1
    sleep(1)