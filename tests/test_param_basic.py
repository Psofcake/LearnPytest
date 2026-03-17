#파라미터화 - parametrize
#하나의 테스트 함수에 대해 여러 입력 값을 반복하고 싶을 때,
#여러 데이터 세트(파라미터)를 적용해 입력값만 바꿔서 자동 반복하는 방식

import pytest

#@pytest.mark.parametrize("인자이름1, 인자이름2, ...,기대결과", [(테스트케이스1),(tc2),(tc3),...,(tcn)] )
#테스트 함수에 전달할 인자 이름들은 문자열로 나열(쉼표로 구분)

def add(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",[(1,1,2),(2,3,5),(-1,2,1)])
def test_add(a,b,expected):
    assert add(a,b)==expected