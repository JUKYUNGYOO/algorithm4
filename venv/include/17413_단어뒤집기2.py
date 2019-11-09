# https://www.acmicpc.net/problem/17413

S, tmp = input(),""

ck = False
ans = ""

for i in S:
    if i == ' ':
        if not ck:
            ans += tmp[::-1] + " "
            tmp = ""
    #         현재 보고 있는 단어를 역순으로하고 공백출
        else:
            ans += " "
    elif i == '<':
        ck = True
        ans += tmp [::-1] + "<"
        tmp = ""

    elif i == '>':
        ck = False
        ans += ">"

    else:
        if ck:
            ans += i
        else:
            tmp += i
        # 알파벳과 숫자

ans += tmp[::-1]
print(ans)