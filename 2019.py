'''
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
주어질 숫자는 30을 넘지 않는다.
'''

N = int(input())
original_number = []
multipled_number = []
number = 1
for i in range(1, N+2):
    original_number.append(i)
    multipled_number.append(f'{number} ')
    number*=2
print(''.join(multipled_number))