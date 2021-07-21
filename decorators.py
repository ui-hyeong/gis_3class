
def decorator(func):
    def decorated(input_text):
        print('함수시작2')
        func(input_text)
        print('함수 끝2')
    return decorated

@decorator   # decorator 적용
def hello_world(input_text):
    print('함수시작1')
    print(input_text)
    print('함수 끝1')
hello_world('hello')