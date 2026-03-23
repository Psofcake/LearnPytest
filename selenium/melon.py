# selenium/melon.py

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

wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.melon.com")
    wait.until(lambda d: d.title != "")
    print(f"title : {driver.title}")
    
    element = driver.find_element(By.ID, "top_search")
    wait.until(EC.visibility_of_element_located((By.ID,"top_search")))

    element.clear()
    element.send_keys("bts")
    element.send_keys(Keys.ENTER)

    # [앨범] 탭으로 이동
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[title="앨범 - 페이지 이동"]'))).click() # 요소가 클릭 가능한지 확인

    # 첫번째 앨범 선택
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[title="ARIRANG - 페이지 이동"]'))).click()
    # 안되면 => wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frm"]/div/ul/li[1]/div/div/dl/dt/a'))).click()

    #"곡정보"아이콘 선택
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'[title="Body to Body 곡정보"]'))).click()

    #노래제목 가져오기 title = (요소).text
    #title = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"song_name")))
    #titleText = title.text
    #print(titleText)

    #노래 가사 가져오기 lyric = (요소).text
    #lyric = wait.until(EC.text_to_be_present_in_element((By.ID, "d_video_summary")))
    #lyricText = lyric.text
    #print(lyricText)
    '''
    with open(title+".txt","w",encoding="utf-8")as f:
        f.write(lyric)
    print(f"{title}.txt 파일에 노래가사가 저장되었습니다.")'''
finally:
    #driver.quit()
    pass

 
