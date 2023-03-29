# 2 3의 배수의 합

i = 1
sum = 0
while i <= 1000:
    if (i % 3 == 0):
        sum += i
    i += 1

print(sum)

# 3 별 표시하기

i = 1
while i <= 5:
    print('*'*i)
    i += 1

# 4 1부터 100까지 출력

for i in range(1, 101):
    print(i)

# 5 평균점수 구하기

student = [70, 60, 55, 75, 95]
sum = 0
for i in student:
    sum += i

print(sum/len(student))

# 6 리스트 컴프리헨션

arr = [1, 2, 3, 4, 5]
num = list(a * 2 for a in arr if a % 2 == 1)
print(num)
