# 1 평균 점수 구하기

kor = 80
eng = 75
math = 50

avg = (kor+eng+math)/3
print(avg)

# 2 홀수 짝수 판별

num = 13
if (num % 2 == 0):
    print('짝수')
else:
    print('홀수')

# 3 주민등록번호 나누기

pin = '881120-1068234'

first = pin[:6]
last = pin[7:]

print(first, last)

# 4 주민등록번호 인덱싱

pin = '881120-1068234'
sex = pin[7]
print(sex)

# 5 문자열 바꾸기

a = "a:b:c:d"

print(a.replace(":", "#"))

# 6 리스트 역순 정렬하기

l = [1, 3, 5, 4, 2]

print(l.sort())

# 7 리스트를 문자열로 만들기

str = ['life', 'is', 'too', 'short']

print(" ".join(str))

# print(*str)

# 8 튜플 더하기

tup = 1, 2, 3
tup2 = (4,)
tup3 = tup+tup2
print(tup3)
