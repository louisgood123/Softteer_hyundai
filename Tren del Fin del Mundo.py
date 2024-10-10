from re import split

N = int(input("역의 수를 입력하시오"))

for i in range(N):
    Q = input()
    S = Q.split()
    x = S[0]
    y = S[1]

min_value = min(y, key=int)
min_index = y.index(min_value)

print(x[min_index] + y[min_index])
