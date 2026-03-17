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

#Collected 1 item <-인식된 테스트 함수 개수
#Pytest는 본적으로 tests 디렉토리 탐색. 
#함수를 정의해두기만 해도 자동으로 검사

#각 테스트가 모든 assert를 통과한 경우 . 표시됨 (예: test_test1.py ...)
#assert문 중 하나 이상 실패 케이스가 있으면 F 표시됨 (예: test_test1.py .F.)
#assert 외 다른 예외 발생 시 E 표시
#의도적으로 건너뛴 테스트는 s 표시 (@pytest.mark.skip 등)
#xfail-예상된 실패(실제로 실패)는 x 표시
#Xpass-예상된 실패가 성공(잠재적문제)는 X 표시
