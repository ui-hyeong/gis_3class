
# def decorator(func):
#     def decorated(input_text):
#         print('함수시작2')
#         func(input_text)
#         print('함수 끝2')
#     return decorated

# @decorator   # decorator 적용
# def hello_world(input_text):
#     print('함수시작1')
#     print(input_text)
#     print('함수 끝1')
# hello_world('hello')

def decorator(func):
    def decorated(b, h):
        if b >0 and h>0 :
            func(b, h)
        else:
            print('error')
    return decorated


@decorator
def triangle(b, h):
    print(b*h*0.5)
@decorator
def rectangle(b, h):
    print(b*h)

triangle(2, -3)
rectangle(2, 3)