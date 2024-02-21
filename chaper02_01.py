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


# end 옵션

