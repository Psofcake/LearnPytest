#tests/test_markers.py

# 마커를 활용한 테스트 제어
# @pytest.mark.마커이름 - 테스트에 메타데이터(꼬리표)를 붙이는 기능
# 테스트 방법 : pytest -m 마커이름

import pytest
import sys

# @pytest.mark.skip(reason="(건너뛰는 이유)") = 테스트 건너뛰기 
# @pytest.mark.skipif(조건문, reason="(건너뛰는 이유)") = 특정 조건에서만 건너뛰기
# @pytest.mark.xfail(조건문(특정조건에서만 실패예상시 작성), reason="(예상 실패 이유)", strict=False, raises=None(특정예외로 인한 실패예상시 작성)) = 실패 예상
# * strict=True일 경우 xfail표시 테스트가 성공 시 이전 테스트를 실패로 처리

@pytest.mark.skip(reason="아직 구현되지 않음") #(용도 = 테스트 임시 비활성화)
def test_future_feature():
    assert False #테스트 결과 : s

@pytest.mark.skipif(sys.platform == "win32", reason="윈도우에서는 동작하지 않음") # 조건이 참이면 건너뜀.(용도 = 특정 환경 의존적 테스트)
def test_linux_only_feature():
    assert True

@pytest.mark.xfail(reason="버그 #001 수정 전까지 실패 예상") #(용도 = 알려진 버그, 불안정한 기능 테스트)
def test_known_bug():
    assert 1 == 2 #테스트 결과 : x(실패하지만 xfail이라 에러로 치지 않음.)

@pytest.mark.smoke
def test_login():
    print("로그인 기능 테스트")
    assert True
