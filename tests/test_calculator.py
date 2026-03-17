# 픽스처 Fixture : 테스트를 실행하기 전에 일정하게 준비해두는 객체 데이터, 환경, 상태
# 환경 설정 단순화, 코드 중복 제거, 재현성 보장을 위해 사용.

# 픽스처 키워드
# @pytest.fixture

from apps.calculator import Calculator
import pytest

@pytest.fixture #함수 정의 상단에 픽스처임을 먼저 알림
def calc_instance(): #픽스처 함수. 이름은 알아서
    calc = Calculator()
    return calc

def test_add():
    assert calc_instance.add(2,3) == 5
    assert calc_instance.add(-1,1) == 0

def test_subtract():
    assert calc_instance.subtract(2,3) == -1
    assert calc_instance.subtract(-1,1) == -2

def test_divide():
    assert calc_instance.divide(2,3) == pytest.approx(2/3)
    assert calc_instance.divide(-1,1) == -1

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc_instance.divide(1,0)
