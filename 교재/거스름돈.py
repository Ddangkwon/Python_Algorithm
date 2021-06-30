
n = int(input())
answer = 0
coin_types = [500, 100, 50, 10]

for i in coin_types:
    answer += (n // i)
    n %= i

print(answer)