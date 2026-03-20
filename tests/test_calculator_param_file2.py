import pytest

# 동적 파라미터화
def test_add(calc_instance, ADDCASES):
    a,b,expected = ADDCASES
    if expected == TypeError:
        with pytest.raises(TypeError):
            calc_instance.add(a,b)
    else :
        assert calc_instance.add(a,b) == expected
