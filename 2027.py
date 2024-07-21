'''
주어진 텍스트를 그대로 출력하세요.
'''

text = ['+', '+', '+', '+', '+']
for i in range(len(text)):
    text[i] = '#'
    if i == 0:
        print(''.join(text))
        continue
    text[i-1] = '+'
    print(''.join(text))