import random

number = random.randint(1,31) # number는 1부터 30까지의 랜덤 숫자를 뱉어냄을 지정해줌
print(f' 내 마음속 숫자 : {number}') # 랜덤 숫자가 눈에 보이게 print로 작성해줌
running = True # running은 True여야 작동하기 때문에 True임을 지정


while running: # while이 running(True)인 함수 작성
    guess = int(input('1~31 중 내가 생각한 숫자는?')) # 입력받은 값을 정수(int) 로 변환하여 guess 에 대입
    print(f'입력받은 숫자 : {guess}') # 입력받은 숫자가 guess임을 지정하고 눈에 보이게 print로 표현

    if guess == number: # 입력 받은 값이 내가 생각한 숫자랑 같은 경우를 가정
        print('정답입니다.')  # 같은 숫자를 입력했을 때 나오는 말 입력
        running = False # 그리고 running 이 True가 아니어야 멈추기 때문에 False로 변함을 입력
    elif guess > number: # 입력 받은 값이 내가 생각한 숫자보다 클 경우를 가정
        print('내가 생각한 숫자보다 큽니다.') # 큰 숫자를 입력했을 때 나오는 말 입력
    elif guess < number: # 입력 받은 값이 내가 생각한 숫자보다 작을 경우를 가정
        print('내가 생각한 숫자보다 작습니다.') # 작은 숫자를 입력했을 때 나오는 말 입력