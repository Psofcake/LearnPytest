#selenium/1.webpage_open.py

# selenium 설치 명령어 : pip install selenium
# 버전 확인
# import selenium
# print("Selenium: ", selenium.__version__)

from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options

# 옵션 설정
opts = Options()
opts.add_experimental_option("detach",True) # 브라우저 유지. (창을 열어 두고 싶을 때)
#opts.add_argument("--headless==new") # 창 없이 실행 (브라우저 창을 화면에 띄우지 않고(백그라운드에서) 실행하는 모드) #new : 최신 버전을 의미
opts.add_argument("--window-size = 1280,900") # 창 크기 설정

#driver = webdriver.Chrome(options = opts)
driver = webdriver.Edge(options = opts)

try:
    driver.get("https://www.python.org") #브라우저 열기
    print(f"title : {driver.title}")
finally:
    #driver.quit() # 브라우저 닫기
    pass
