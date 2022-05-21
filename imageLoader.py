import os
from selenium import webdriver
import urllib.request
from selenium.webdriver.common.by import By

csv = []
with open('data.csv', 'r') as f:
    csv = f.readlines()

data = dict()
for i, line in enumerate(csv):
    parsed = line.split(',')
    data[i + 1] = parsed

# 1 based
requiredImages = [i + 1 for i in range(len(csv))]

# check what images we already have
existing = [int(f.split('.')[0]) for f in os.listdir('images')]

for exist in existing:
    requiredImages.remove(exist)

browser = webdriver.Firefox()
for req in requiredImages:
    d = data[req]
    s = f"{d[0]}{d[2]}{d[3]}"
    s = s.replace(' ', '+')
    browser.get(f"https://www.google.com/search?q={s}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwisidrilOz3AhUNTt8KHQ1QCNEQ_AUoAXoECAEQAw&biw=2057&bih=1111&dpr=0.9")
    
    ip = browser.find_element(By.CLASS_NAME, 'islrc').find_elements(By.XPATH, './/*')[1]
    img = ip.find_element(By.TAG_NAME, 'img').get_attribute('src')
    
    urllib.request.urlretrieve(img, f'images/{req}.jpg')