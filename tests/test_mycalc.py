# tests/test_mycalc.py

#from apps import mycalc as c
from apps.mycalc import add, subtract #테스트 대상 함수 가져오기
import pytest

# 양수끼리의 합을 검사하는 테스트 함수 정의
def test_add_positive_number():
    # Arrange(준비) : 테스트에 필요한 변수나 상태를 설정합니다.
    a=12
    b=13
    expect = 25
    # Act(실행) : 테스트하려는 함수를 호출합니다.
    actual = add(a,b)
    # Assert(검증) : 실제 결과가 예상 결과와 같은지 확인합니다.
    #assert로 결과 검증 - 조건이 True가 아니면 AssertionError 발생 => 테스트 실패
    assert add(12,13) == 25

def test_add_negative_number():
    a = -3
    b = -5
    expect = -8
    actual = add(a,b)
    assert actual == expect

def test_substract_with_negative_number():
    assert subtract(5,-3) == 8
    assert subtract(-3,5) == -8
#    assert가 여러개여도 됨. 다만 모든 assert가 통과해야 해당 테스트함수 통과로 체크됨.

#def test_fail_example(): 
#    assert add(2,2)==3 #의도적으로 fail 발생시키기
