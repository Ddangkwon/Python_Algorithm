import sys

int(input(("갯수를 입력하세요 : ")))


data = list(map(int, input().split()))

data.sort()
print(data)

# 데이터 나눠서 입력받기

n, m, k = map(int, input().split())
print(n, m, k)

# 문자열 입력 ㅂ다기

data = sys.stdin.readline().rstrip()
print(data)

# 정답 문자열 입력 시 정수 to 문자 형변환

test_case = 1
answer = 10
print("#" + str(test_case) + " " + str(answer))