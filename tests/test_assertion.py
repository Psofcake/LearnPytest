#tests/test_assertion.py

import pytest
import warnings
from apps.mycalc import divide

#--상세 보기 명령어--
#pytest -v
#각 테스트 함수명과 결과 표시 : PASSED / FAILED

#--원하는 테스트만 선택 실행 명령어--
#pytest -k calc
#테스트 함수/클래스/파일 이름에 calc라는 단어가 포함된 테스트만 실행

#assert 구문을 사용하는 다양한 방법
def test_various_assertion():
    #참/거짓 검증 (assert, assert not)
    assert True
    assert 1
    # assert 0 <- Fail
    assert True == 1
    assert False == 0
    assert "abc"
    assert " "
    assert not ""
    assert [1,2,3] 
    assert not [] # None, 빈 컬렉션은 False로 평가
    #비교 검증 (>,<,>=,<=,!=)
    assert 5>3
    assert 10<=10
    assert 7 != 8
    #멤버십 검증 (in, not in)
    assert "pytest" in "pytest is easy" #'단어'가 '문자열'안에 포함되어 있는지 확인
    assert "world" not in "hello universe" 
    assert 3 in [1,2,3,4]   #요소가 컬렉션 안에 존재하는 지 확인
    assert 5 not in (1,2,3)
    #동일성 검증 (is, is not)
    a=[1,2]
    b=[1,2]
    c=a
    assert a==b #a와 b의 값을 비교
    # assert a is b #a와 b가 같은 메모리 주소 객체인지 확인. #Fail
    assert c is a #True #c를 수정하면 a에 영향 있음.
    #----pytest.approx----
    #컴퓨터 실수 표현 방식(부동소수점)으로 미세한 연산 차이 발생 가능.
    #assert (0.1+0.2) == 0.3  #Fail - AssertionError
    #이 때 사용하는 키워드 - pytest.approx : 두 숫자가 지정된 허용 오차+- 내에서 거의 같은지 비교.
    assert (0.1+0.2) == pytest.approx(0.3)
    
    #허용 오차 지정 - abs 절대 허용오차
    assert (1/3) == pytest.approx(0.33333,abs=0.0000034) #예상결과 0.33333와 차이가 3.4e-6이하면 허용
    #허용 오차 지정 - rel 상대 허용오차 = |(실제값-기대값)| / 기대값
    assert (0.1+0.2) == pytest.approx(0.3, rel=1.1e-5)  #0.3의 0.00011%까지 허용

def test_float_approx():
    result = divide(1,3)
    assert result == pytest.approx(1/3)
    #assert result == pytest.approx(0.333333) #Fail - AssertionError
    # 디폴트 허용 오차가 0.0000001단위이기 때문에 Error발생
    assert result == pytest.approx(0.3333333) #허용 오차 이내이므로 통과
    assert result == pytest.approx(1/3) #동일한 값이므로 통과

# 예외 발생 테스트 - 예상된 오류 pytest.raises
# 필요성 : 프로그램이 정상적으로 오류를 발생시키는지 (의도된 방어 로직)테스트
def test_divide_by_zero_exception():
    with pytest.raises(ZeroDivisionError): #ZeroDivisionError가 발생할거라고 기대
        divide(10,0)

#with 블록 내 지정된 예외 발생 시 테스트 통과
#예외 미발생 또는 다른 예외 발생 시 테스트 실패

#def test_divide_wrong_type_raises_exception():
#    with pytest.rasises(ValueError):
#        divide(10,"3") #test Fail

def function_that_warns():
    warnings.warn("이 함수는 곧 제거될 예정입니다!",DeprecationWarning) #DeprecationWarning:지원중단예정 경고
    #프로그램 실행을 중단시키지 않지만 주의를 주는 경고 메시지 발생 테스트
    return True

def test_deprecation_warning():
    with pytest.warns(DeprecationWarning):
        assert function_that_warns() #warnig이 잘 뜨도록 하며 assert를 붙이면 함수가 반환하는 값도 함께 검증
        #function_that_warns()
