#selenium/3.find_element.py

import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 옵션 설정
opts = Options()
opts.add_experimental_option("detach",True)
opts.add_argument("--window-size = 1280,900")

driver = webdriver.Edge(options = opts)

# 페이지가 로딩될 때 요소마다 로드되는 시간이 다르다.
# 따라서 driver.implicitly_wait(시간초)을 사용해 일정한 시간동안 주기적으로 요소 탐색을 반복 시도하거나(암묵적 대기)
# 원하는 조건이 충족될 때까지 대기한다. (명시적 대기) ★★★
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.python.org") #브라우저 열기
    wait.until(lambda d: d.title != "") # 타이틀이 공백이 아니게 될때까지 대기
    print(f"title : {driver.title}")
    
    element = driver.find_element(By.ID, "id-search-field") # ID로 요소 찾기
    wait.until(EC.visibility_of_element_located((By.ID,"id-search-field"))) # EC의 함수가 인자로 튜플을 필요로 함.
    # 검색 후 해당 요소가 화면에 나올때까지 기다림
    element.clear() # 이미 들어있는 텍스트를 전부 지우는 역할
    element.send_keys("list") # "list" 입력 (위에서 클리어가 안되면 기존 문장에 덧붙여짐)
    element.send_keys(Keys.ENTER) # 엔터 입력 (검색 실행)
finally:
    #driver.quit() # 브라우저 닫기
    pass

 
