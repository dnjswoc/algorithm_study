'''
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

[제약 사항]
각 수는 0이상 10000 이하의 정수이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

T = int(input())
# 입력받을 테스트 케이스의 수를 T로 설정

for i in range(T):
    data = list(map(int, input().split()))  # 테스트 케이스 입력
    sum = 0
    for k in range(len(data)):  # 테스트 케이스의 길이만큼 반복수 설정
        if int(data[k])%2 == 1: # 인덱스를 이용하여 홀수 구하기
            sum += data[k]
    print(f'#{i+1} {sum}')      # 홀수의 합계를 구하고 f-string을 사용하여 결과 출력