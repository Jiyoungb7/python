
text = input('값을 넣으면 숫자로 변환 됩니다.')

# try:
#     num = int(text)
# except Exception:
#     print('숫자를 입력해주세요.')
#     text = input('값을 넣으면 숫자로 변환 됩니다.')
# finally:
#     num = int(text)
#     print(f'당신이 입력한 값 :{num} 이 숫자로 변환 되었습니다.')

# while True:
#     text = input('값을 넣으면 숫자로 변환 됩니다.')
#     try:
#         num = int(text)  # 숫자로 변환 시도
#         break  # 성공하면 반복문 탈출
#     except ValueError:  # 숫자가 아니면 에러 발생
#         print('숫자를 입력해주세요.')
#
# print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다.')

# finally 굳이 안넣어도 된다.
while True:
    try:
        text = input('값을 넣으면 숫자로 변환 됩니다.')
        num = int(text)
        print(f'당신이 입력한 값 :{num} 이 숫자로 변환 되었습니다.')
        break
    except ValueError:
        print(f'{text}는 숫자가 아닙니다.')
