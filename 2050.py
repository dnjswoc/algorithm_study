'''
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

[제약 사항]
문자열의 최대 길이는 200이다.

[입력]
알파벳으로 이루어진 문자열이 주어진다.

[출력]
각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
'''

Al = input()
# A = 65, Z = 90
Al_len = len(Al)
Al_asc = []
for i in range(Al_len):
    Al_asc.append(ord(Al[i])-64)
print(*Al_asc)
