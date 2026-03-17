#apps/calculator.py

class Calculator:
    def add(self,a,b):
        # a와 b가 숫자인지 검사하는 조건문
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        #isinstance(a,(int,float)) : a가 int또는float 즉 숫자인지 확인.    
            raise TypeError("입력값은 숫자여야 합니다.")
        return a+b

    def subtract(self,a,b):
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("입력값은 숫자여야 합니다.")
        return a-b

    def divide(self,a,b):
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("입력값은 숫자여야 합니다.")
        if b ==0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다")
        return a/b
    
