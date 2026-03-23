#selenium/2.page_navi.py

import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

# 옵션 설정
opts = Options()
opts.add_experimental_option("detach",True) # 브라우저 유지. (창을 열어 두고 싶을 때)
opts.add_argument("--window-size = 1280,900") # 창 크기 설정

driver = webdriver.Edge(options = opts)

try:
    driver.get("https://www.python.org") #브라우저 열기
    print(f"title : {driver.title}")

    time.sleep(3) # 3초 지연

    driver.get("https://www.naver.com") # 네이버로 이동
    print(f"title : {driver.title}")

    time.sleep(3)

    driver.back() # 뒤로가기
    time.sleep(1)
    driver.forward() #앞으로가기
    time.sleep(1)
    driver.refresh() #새로고침
finally:
    #driver.quit() # 브라우저 닫기
    pass
