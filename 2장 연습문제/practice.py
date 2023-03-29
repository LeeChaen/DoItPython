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
