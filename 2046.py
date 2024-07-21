'''
주어진 숫자만큼 #을 출력해보세요.
주어질 숫자는 100,000 이하다.
'''

num = int(input())
list_of_sharp = []
for i in range(num):
    list_of_sharp.append('#')
print(''.join(list_of_sharp))