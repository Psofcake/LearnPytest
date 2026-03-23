#selenium/3.find_element.py

import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 옵션 설정
opts = Options()
opts.add_experimental_option("detach",True) # 브라우저 유지. (창을 열어 두고 싶을 때)
opts.add_argument("--window-size = 1280,900") # 창 크기 설정

driver = webdriver.Edge(options = opts)

try:
    driver.get("https://www.python.org") #브라우저 열기
    print(f"title : {driver.title}")
    
    element = driver.find_element(By.ID, "id-search-field") # ID로 요소 찾기

    element.clear() # 이미 들어있는 텍스트를 전부 지우는 역할
    element.send_keys("list") # "list" 입력 (위에서 클리어가 안되면 기존 문장에 덧붙여짐)
    element.send_keys(Keys.ENTER) # 엔터 입력 (검색 실행)

finally:
    #driver.quit() # 브라우저 닫기
    pass
