# tests/data_loader.py
import csv
import ast
from pathlib import Path

def load_test_data(filename):
    file_path = Path(__file__).resolve().parents[0]/ "data" / filename
    #__file__ : 현재 파이썬 파일 위치
    #.resolve() : 절대 경로로 바꿈 (파일 이름 포함)
    #.parents[0] : 폴더로 이동 [0] = 현재 폴더, [1] = 상위 폴더
    #"data"/filename : data 폴더 안의 파일. 즉, 현재 파일 기준으로 한 단계 위 -> data폴더 -> filename파일 찾기

    cases = []  # 빈 리스트 생성
    with open(file_path, newline="", encoding="utf-8-sig") as f: #csv파일을 읽을 때 newline=""을 꼭 써주어야 자동줄바꿈되는 오류 방지 가능
        reader = csv.DictReader(f) #csv를 딕셔너리 형태로 읽음.
        '''[   {'a': '3', 'b': '2', 'expected_result': '5'},
        {'a': '3', 'b': '-2', 'expected_result': '1'},
        {'a': '3', 'b': '-6', 'expected_result': '-3'},
        {'a': '-3', 'b': '2', 'expected_result': '-1'},
        {'a': '-5', 'b': '2', 'expected_result': '-3'},
        {'a': '-5', 'b': '7', 'expected_result': '2'},
        {'a': '2', 'b': '"2"', 'expected_result': 'TypeError'},
        {'a': '"2"', 'b': '2', 'expected_result': 'TypeError'}  ]'''
        for row in reader: # 각 줄을 하나씩 처리
            a = ast.literal_eval(row["a"]) # ast.literal_eval() : csv의 모든 값은 문자열로 인식되기 때문에, 문자열을 실제 파이썬 데이터 타입으로 변환
            b = ast.literal_eval(row["b"])
            expected_raw = row["expected_result"] #문자열 상태로 가져옴
            if expected_raw == "TypeError": # 가져온 문자열이 "TypeError"이면 실제 TypeError에러타입으로 바꿔줌
                expected = TypeError
            else:
                expected = ast.literal_eval(expected_raw) #아니라면 파이썬 데이터타입으로 변환
            cases.append((a, b, expected)) #(a,b,expect) 튜플 형태로 cases리스트에 요소 추가
    return cases #List를 리턴
