# tests/conftest.py

# 픽스처 Fixture : 테스트를 실행하기 전에 일정하게 준비해두는 객체 데이터, 환경, 상태
# 환경 설정 단순화, 코드 중복 제거, 재현성 보장을 위해 사용.

# 픽스처 키워드
# @pytest.fixture

# 픽스처 재사용 범위 제어
# @pytest.fixture(scope="....") #function(테스트함수마다 실행),class(테스트 클래스마다 호출),module(파일),package(패키지),session(프로젝트전체)
# #스코프 미작성 시 scope="function"(함수 내에서만 공유)가 기본.

#여러 테스트 파일에서 동일 픽스처를 공유
#tests/conftest.py에 픽스처 정의 시 다른 파일에서 import 없이 해당 픽스처 사용 가능. 중앙관리 및 재사용성 증대
import pytest
from apps.calculator import Calculator
from tests.data_loader import load_test_data

@pytest.fixture(scope="module") #함수 정의 상단에 픽스처임을 먼저 알림
def calc_instance(): #픽스처 함수. 이름은 알아서
    print("\n--Calculator 인스턴스 생성(conftest.py)")  #픽스처 호출을 확인하기 위한 프린트문
    calc = Calculator()
    return calc

# 동적 파라미터화
def pytest_generate_tests(metafunc): #pytest가 테스트 케이스를 생성할 때 개입해서 파라미터를 동적으로 만드는 hook 함수
    if "ADDCASES" in metafunc.fixturenames: # metafunc - pytest가 테스트 함수 정보를 담아서 전달하는 객체
        cases = load_test_data("add.csv")   # metafunc에 "SUBCASES"가 있으면 add.csv 로드하기.
        metafunc.parametrize("ADDCASES",cases)
    elif "SUBCASES" in metafunc.fixturenames:
        cases = load_test_data("sub.csv")
        metafunc.parametrize("SUBCASES",cases)


from selenium import webdriver
from selenium.webdriver.edge.options import Options
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

# <--headless 옵션 사용 정의하기>
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)
# 사용방법 : pytest tests/test_login.py --headless
# (백그라운드에서 실행하여 화면을 띄우지 않고도 결과를 확인할 수 있다.)


# 웹페이지 셀레니움 엣지 드라이버
@pytest.fixture(scope="session") # 그냥 두면 쿠키가 남아 fail됨. 따라서 초기화 필요
def driver(request): #request는 pytest가 제공하는 픽스처
    headless = request.config.getoption("--headless") #--headless옵션이 있는지 확인
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    d = webdriver.Edge(options = opts)
    print("######## driver 시작 #########")
    yield d
    d.quit()

#autouse=True - 모든 테스트함수 (파라미터 각 케이스 포함) 앞에서 자동 실행
@pytest.fixture(autouse=True)
def reset_browser_state(driver):
    driver.delete_all_cookies() #드라이버를 쓸때마다 쿠키/스토리지 정리
    driver.get("about:blank")
