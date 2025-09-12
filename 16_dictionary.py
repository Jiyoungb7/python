# dictionary는 키:값 형태로 되어있다.
# 비슷한 자료구조로는 자바스크립트 - 오브젝트, 자바 - 맵 이 있다.
dic1 = {'name':'kim,ji-young', 'phone':'010-5444-9477', 'age':10}
dic2 = {'name':'hong,gil-dong',
        'phone':'010-5444-9477',
        'friends':['Alice','John','Smith']}


# 사전에 데이터 넣기1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)