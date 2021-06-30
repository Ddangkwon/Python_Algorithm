
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

first_num = data[0]
second_num = data[1]
cnt = 0
answer = 0
while cnt != m:
    if(cnt % k != 0 or cnt == 0):
        answer += first_num
    else:
        answer += second_num
    cnt += 1
print(answer)