# https://www.acmicpc.net/problem/9037

def check(N,candy):
    for i in range(N):
        # 홍수이면 candy[i] += 1
        if candy[i] % 2 == 1:
            candy[i] += 1
    return len(set(candy)) == 1
# set(candy) 같은수가 다 사라짐
# len(set(candy)) == 1
# 모든 수가 같은지 check
def teacher(N,candy):
    # 오른쪽으로 전달해 주어야 되는 사탕
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        # 홀수이면 , candy[idx] +=1
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx+1) % N] = candy[idx]
    for idx in range(N):
        candy[idx] += tmp_lst[idx]
    return candy






def process():
    N, candy = int(input()), list(map(int,input().split()))
    cnt = 0
    # 다 같아 지는 경우에만 멈추므로 not check
    while not check(N,candy):
        cnt += 1
        candy = teacher(N,candy)
    print(cnt)

for i in range(int(input())):
    process()
