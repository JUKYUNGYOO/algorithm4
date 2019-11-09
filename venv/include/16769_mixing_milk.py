# https://www.acmicpc.net/problem/16769

# 우유를 담은 병 3개
# 용량이 있음
# 미리 차있는 우유의 양도 있음
# 1->2->3 총 2회
# 이렇게 순환을 총 100번 돌렸을 때
# 마지막 상태는?

C,M = list(),list()
# Capacity, Milk

for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)


for i in range(100):
    idx = i % 3
#    (0,1,2)
    nxt = (idx+1) % 3
# 다음칸
#    Max(현재우유의양 - 다음칸으로 전달되는 우유의양, 0 )

    M[idx], M[nxt] = max(M[idx]-(C[nxt]-M[nxt]),
                        0),min(C[nxt],M[nxt]+M[idx])
    # print(M[idx],M[nxt])

#   내가보고있는것, 다주거나, 남기거나
#     M[idx] = max(C[nxt] - M[nxt] + M[idx],0)
#     M[nxt] = min(C[nxt],M[nxt]+M[idx])
#    max(C[nxt]:자신의 용량 ,두개 우유의 합)

for i in M:
    print(i)
# 현재 우유양 출력






