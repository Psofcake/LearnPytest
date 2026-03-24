# tests/test_signup.py

import pytest
from pages.signup import SignupPage

SIGNUP_CASES = [ # 딕셔너리 케이스 {"키1":"값1", "키2":"값2", ... }
    {
        "email":"user@ex.com",
        "username":"max",
        "pw":"abcd12345",
        "confirm":"abcd12345",
        "terms":True,
        "expect":"가입이 완료되었습니다!"
    },
    {
        "email":"",
        "username":"max",
        "pw":"abcd12345",
        "confirm":"abcd12345",
        "terms":True,
        "expect":"입력값을 다시 확인해주세요."
    }
]
@pytest.mark.parametrize("case",SIGNUP_CASES)
def test_signup(driver,case):
    page = SignupPage(driver)
    page.open()
    page.signup(case["email"],case["username"],case["pw"],case["confirm"],case["terms"])

    flash_msg = page.flash_message()

    assert case["expect"] == flash_msg
    
