# 픽스처 Fixture : 테스트를 실행하기 전에 일정하게 준비해두는 객체 데이터, 환경, 상태
# 환경 설정 단순화, 코드 중복 제거, 재현성 보장을 위해 사용.

# 픽스처 키워드
# @pytest.fixture

from apps.calculator import Calculator
import pytest

def test_add():
    calc = Calculator() #객체를 테스트 코드마다 매번 생성하기 번거로움, 코드 중복
    assert calc.add(2,3) == 5
    assert calc.add(-1,1) == 0

def test_subtract():
    calc = Calculator() #코드 중복
    assert calc.subtract(2,3) == -1
    assert calc.subtract(-1,1) == -2

def test_divide():
    calc = Calculator() #코드 중복
    assert calc.divide(2,3) == pytest.approx(2/3)
    assert calc.divide(-1,1) == -1

def test_divide_by_zero():
    calc = Calculator() #코드 중복
    with pytest.raises(ZeroDivisionError):
        calc.divide(1,0)
