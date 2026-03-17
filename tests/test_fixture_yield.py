#tests/test_fixture_yield.py

# yield : setup(환경 준비)-test(실행)-teardown(정리 작업) 구조를 지원.
# DB, 파일핸들, 네트워크 연결 등 외부자원을 다루는 경우 필요.
# 테스트 함수에 값을 전달하고, 테스트함수가 실행 완료 되면 다음라인으로 넘어감.

import pytest

@pytest.fixture
def file_writer():
    f=open('test.txt','w',encoding='utf-8')
    print("파일 열기") #1
    yield f #파일을 밀어넣고 작업이 끝날때까지 대기
    print("파일 닫기") #4
    f.close()

def test_write_sentence(file_writer):
    print("테스트 시작") #2
    text = "pytest fixture test\n"

    file_writer.write(text) #쓰기
    file_writer.flush() #버퍼 비우기

    with open("test.txt", encoding="utf-8") as f:
        content = f.read()

    assert text in content #3
