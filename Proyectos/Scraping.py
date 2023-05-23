from bs4 import BeautifulSoup
import requests
import pandas as pd
import time as tm
tm.sleep(3)

url = 'https://as.com/motor/formula_1.html?omnil=src-sab'
page = requests.get(url)
result = page.text
soup = BeautifulSoup(result, 'lxml')

# pilotos

pilotos = soup.find_all(class_='main-name-in-row')

tm.sleep(3)
print(pilotos)
