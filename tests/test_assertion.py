#tests/test_assertion.py

#--상세 보기 명령어-- p19
#pytest -v
#각 테스트 함수명과 결과 표시 : PASSED / FAILED

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
    