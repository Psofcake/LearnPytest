#tests/test_signup_mock_by_playwright.py

import json
import pytest
from pages.signup_by_playwright import SignupPage
from playwright.sync_api import expect

URL = "file:///C:/Users/EDU01-14/Documents/swtest/pages/signup_mock.html"

FAKE_CASES = [
    {
        "id": "success",
        "status": 200,
        "json_body": {"status": "ok", "message": "회원가입성공(Mocked)"},
        "expected": "회원가입성공(Mocked)",
    },
    {
        "id": "fail",
        "status": 500,
        "json_body": {"status": "error", "message": "서버오류(Mocked)"},
        "expected": "서버오류(Mocked)",
    },
]
@pytest.mark.parametrize("case",FAKE_CASES, ids=[i["id"] for i in FAKE_CASES]) #ids=["success","fail"]
def test_signup_mock(page, case):
    def handle_mock_responce(route):
        route.fulfill(
            status = case["status"],
            content_type = "application/json",
            #body=json.dumps({"status":"ok","message":"회원가입 성공(Mocked)"})
            body=json.dumps(case["json_body"])
        )

    page.route("http://localhost:8000/api/signup",handle_mock_responce)
    #앞의 페이지를 만나면 서버로 돌리지 않고 내가 만든 목업페이지로 라우팅

    s = SignupPage(page)
    s.open(URL)
    s.signup(
        email="test@ex.com",
        username="HongGilDong",
        password="abc12345",
        confirm="abc12345",
        terms=True)
    
    expect(s.flash).to_contain_text(case["expected"])
