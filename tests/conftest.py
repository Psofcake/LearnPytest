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

@pytest.fixture(scope="module") #함수 정의 상단에 픽스처임을 먼저 알림
def calc_instance(): #픽스처 함수. 이름은 알아서
    print("\n--Calculator 인스턴스 생성(conftest.py)")  #픽스처 호출을 확인하기 위한 프린트문
    calc = Calculator()
    return calc
