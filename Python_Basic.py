

# 연산
a = 7
b = 3

print(a / b)
print(a % b)
# 몫
print(a // b)

# list 초기화
a = list()
print(a)

n = 10
a = [0] * n
print(a)

# list 인덱싱과 슬라이싱

a = [1, 2, 3, 4, 5, 6, 7]

# 맨 뒤 인덱스 출력
print(a[-1])

# 뒤에서 세번 째 인덱스 출력
print(a[-3])

print(a[1 : 4])

# 리스트 컴프리헨션

# 홀수만 포함하는 리스트 셍성
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 제곱 값만 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# 2차원 리스트 초기화(N X M)

n = 3
m = 4
# 언더바로 변수를 사용하지 않을 경우 이렇게 표현할 수 있다
array = [[0] * m for _ in range(n)]
print(array)

# 리스트 관련 기타 메서드

a = [1, 4, 3]
print("default list : ", a)

a.append(2)
print("삽입 : ", a)

# 정렬 후 그 배열이 저장된다.
a.sort()
print("오름차순 정렬 : ", a)

a.sort(reverse = True)
print("내림차순 정렬 : ", a)

a.reverse()
print("배열 뒤집기 ", a)

# index 1에 숫자 3 추가
a.insert(1, 10)
print(a)

print("값이 1인 데이터 갯수 : ", a.count(1))

a.remove(1)
print("값이 1인 데이터 삭제 : ", a)

# 특정 숫자 여러개를 삭제 하고  싶을 때

a = [1, 3, 5, 2, 5, 4, 2, 1, 5, 8, 7]
del_data = {1, 5}

result = [i for i in a if i not in del_data]
print(result)