from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",['enable-automation'])
browser = webdriver.Chrome(options=options)
browser.get("https://wenku.baidu.com/view/60ec32ba33d4b14e852468c8.html")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
text = browser.page_source
html = etree.HTML(text)
txts = html.xpath("//div[@class='ie-fix']//text()")
print(txts)
txt2 = "".join(txts)
txt = txt2
with open("wenku.html","w",encoding="utf-8")as f:
    f.write(txt)