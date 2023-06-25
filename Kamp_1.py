from selenium import webdriver 
import time #ekran süresi icin time içeri aktarildi
import configparser
import os
import pyautogui #ekran görüntüsü için pyautogaui ice aktarildi
 
 
driver = webdriver.Chrome() #web tarayıcısını chorme üzerinden gerceklestirilecegi icin .Chorme(bu kisim kullanilacak tarayiciya göre degistirilebilir) yazildi

url = "https://www.youtube.com"

driver.get(url)

time.sleep(1)
driver.maximize_window() #ekrani büyütmek icin

url = "https://www.youtube.com/lofigirl"
driver.get(url)
print(driver.title)

if "Lofi Girl" in driver.title: 
    ScreenShot = pyautogui.screenshot()
    file_name = " youtube-Lofigirl.jpg"
    path = r"C:\Users\LENOVO\OneDrive\Masaüstü" #kaydedliecek yer belirlenildi
    concordence = os.path.join(path,file_name)
    ScreenShot.save(concordence)      
        
time.sleep(3)

driver.back() #tekrardan youtube ekranina dönmek için kullanildi ( tercihe bagli)
time.sleep(3)


driver.close