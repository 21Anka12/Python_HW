"""import webbrowser

webbrowser.open_new("https://www.google.com")
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com")
