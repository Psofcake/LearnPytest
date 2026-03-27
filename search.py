import requests
import time

# 요청할 URL (원하는 주소로 변경)
url = "https://dapi.kakao.com/v3/search/book?query=python"

API_KEY = "YOUR_REST_API_KEY"

# 검색할 내용
params = {
    "query":"서울"
}

# 카카오 API 사용
headers = {"Authorization":f"KakaoAK {API_KEY}"}

# 호출 횟수
num_requests = 5

# 속도 저장 리스트
response_times = []

print("=== 요청 시작 ===\n")

for i in range(num_requests):
    print(f"{i+1}번째 요청 중...")

    # 시작 시간 기록
    start_time = time.time()

    try:
        # HTTP GET 요청
        response = requests.get(url, headers=headers, params=params)

        # 종료 시간 기록
        end_time = time.time()

        # 걸린 시간 계산
        elapsed_time = end_time - start_time
        response_times.append(elapsed_time)

        # 결과 출력
        print(f"상태 코드: {response.status_code}")
        print(f"응답 시간: {elapsed_time:.4f} 초\n")

    except requests.exceptions.RequestException as e:
        print(f"요청 실패: {e}\n")

# 평균 계산
if response_times:
    average_time = sum(response_times) / len(response_times)
    print("=== 결과 ===")
    print(f"총 요청 횟수: {num_requests}")
    print(f"평균 응답 시간: {average_time:.4f} 초")
else:
    print("모든 요청이 실패했습니다.")