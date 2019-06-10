from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",['enable-automation'])
url = input("请输入网址:")
browser = webdriver.Chrome(options=options)
browser.get(url)
text = browser.page_source
html = etree.HTML(text)
txtss = html.xpath("//div[@class='ie-fix']//text()")
txt1 = "".join(txtss)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
button = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"down-arrow")))[0]
button.click()
time.sleep(3)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3.0)
text = browser.page_source
html = etree.HTML(text)
txts = html.xpath("//div[@class='ie-fix']//text()")
print(txts)
txt2 = "".join(txts)
txt = txt1+txt2
txt = txt.replace("\u2002\u2002","")
with open("wenku.html","w",encoding="utf-8")as f:
    f.write(txt)