# 반환타입 : O 매개변수 : O
# 지도앱
def 매표소(money) :
    print(f'{money}를 냈다.')
    return '티켓'

money = 매표소(10000)
print(money)

# 반환타입 : O 매개변수 : X
# 체중계
def 체중계(무게) :
    print('체중계에 올라갔다.')
    return f'{무게}'

print(체중계(50))

# 반환타입 : X 매개변수 : O
# 오락실
def 오락실(coin) :
    return (f'{coin} 판 가능')

coin = 오락실(5)
print(오락실(5))

# 반환타입 : X 매개변수 : X
# 초인종
def 초인종() :
    print('띵동')

print(초인종())