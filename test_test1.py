#--pip 패키지 업데이트 명령어-- (.venv가상환경 터미널에 입력)
# python -m pip install --upgrade pip

#--pytest 설치 명령어--
# pip install pytest

#--버전 확인--
# pytest --version

#--vsCode에서 자동 저장 기능 설정하기--
# 파일 > 자동 저장 체크

#--pytest가 테스트코드를 탐색하는 규칙--
# 파일 명 : test_*.py, *_test.py
# 함수 명 : 파일 내 test_로 시작하는 함수.
# 클래스 명 : Test로 시작하는 클래스 내 test_로 시작하는 메서드.

#소스코드 구조를 그대로 따르는 방식 권장.
#예) a를 테스트하는 테스트코드 => test_a


def print_hello():
    print("Hello")

print_hello()

def test_print_hello():
    assert 1==1

#파이썬 실행 버튼 기능 명령어
#python test_test1.py

#파이테스트 실행 명령어
#pytest
#동작) test_로 시작하는 파일 명을 찾고 test_로 시작하는 함수를 자동으로 테스트 코드로 인식.
