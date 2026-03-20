#tests/test_calculator_param.py

import pytest
from tests.data_loader import load_test_data

add_test_cases = [(2,3,5),(-1,-1,-2),(5,-3,2),(10,0,10),(0.1,0.2,pytest.approx(0.3)),pytest.param(100,200,300,id="large_numbers")]
# pytest.param(파라미터값,id="~~") 테스트 케이스의 이름을 붙여줌.

@pytest.mark.parametrize("a,b,expected",add_test_cases)
def test_add_cases(calc_instance,a,b,expected):
    print(f"\nTesting add(a={a}, b={b}) == {expected}")
    assert calc_instance.add(a,b) == expected

# id를 설정해준 테스트케이스는 테스트 시 test_add_cases[] 안에 파라미터 값 대신 id가 출력됨.
# test_calculator_param.py::test_add_cases[2-3-5] PASSED
# test_calculator_param.py::test_add_cases[large_numbers] PASSED #id 붙여줌

# 예외 테스트 파라미터화
divide_test_cases = [(10,0,ZeroDivisionError),("10",2,TypeError),(10,"2",TypeError), pytest.param(None,5,TypeError,id="None_input_a")]

@pytest.mark.parametrize("a,b,expected_exception",divide_test_cases)
def test_divide_expections_cases(calc_instance,a,b,expected_exception):
    print(f"\nTesting divide(a={a}, b={b}) raises {expected_exception.__name__}")
    with pytest.raises(expected_exception):
        calc_instance.divide(a,b)

# 데코레이터를 쌓으면 모든 조합으로 실행
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[10,100])
def test_stacked_cases(x,y): # 2 * 2 = 총 4개의 케이스 생성
    print(f"\nTesting with (x={x}, y={y})")
    assert isinstance(x,int)
    assert isinstance(y,int)

# file 불러오기
@pytest.mark.parametrize("a,b,expected", load_test_data("add.csv"))
def test_add(calc_instance,a,b,expected):
    if expected is TypeError:
        with pytest.raises(TypeError):
            calc_instance.add(a,b)
    else :
        assert calc_instance.add(a,b) == expected
