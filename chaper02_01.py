# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php


# 기본 출력 - 작은따옴표, 큰따옴표, 작은따옴표3개, 큰따옴표3개
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()  # 빈값 == 개행(줄바꿈)

# separator 옵션
print('P', 'Y', 'T', 'O', 'N')                # P Y T O N
print('P', 'Y', 'T', 'O', 'N', sep='')        # PYTON
print('P', 'Y', 'T', 'O', 'N', sep=',')       # P,Y,T,O,N
print('P', 'Y', 'T', 'O', 'N', sep='    ')    # P    Y    T    O    N
print('010', '7777', '1234', sep='-')         # 010-7777-1234
print('python', 'google.com', sep='@')        # python@google.com

print()

# end 옵션

print('Welcome to', end='    ')             # Welcome toIT News        print문은 자동 줄바꿈이지만
print('IT News', end='  ')                  # Welcome to    IT News    end옵션에 들어간 문자대로 이어줄 수 있음
print('Web Site')                           # Welcome to    IT News  Web Site
print()

# file 옵션
#import = 10 # 이미 예약어
import sys

print('Learn Python', file=sys.stdout)  # file에 '' 사이의 내용을 쓴다
print()

# format 사용(d : 3, s : 'python', f: 3.14443453)
print('%s %s' % ('one', 'two'))             # one two 
print('{} {}'.format('one', 'two'))         # one two
print('{1} {0}'.format('one', 'two'))       # two one  == 인덱스는 0부터 시작 {} 
                                                        # 비어 있으면 {0}인 것, {1}이면 2번째를 의미