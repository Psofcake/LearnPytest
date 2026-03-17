
import pytest

def test_add(calc_instance):    #픽스처를 인자로 가지고 있어야 해당 픽스처 사용 가능
    assert calc_instance.add(2,3) == 5
    assert calc_instance.add(-1,1) == 0

def test_subtract(calc_instance):
    assert calc_instance.subtract(2,3) == -1
    assert calc_instance.subtract(-1,1) == -2

def test_divide(calc_instance):
    assert calc_instance.divide(2,3) == pytest.approx(2/3)
    assert calc_instance.divide(-1,1) == -1

def test_divide_by_zero(calc_instance):
    with pytest.raises(ZeroDivisionError):
        calc_instance.divide(1,0)
