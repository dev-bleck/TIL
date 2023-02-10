import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # [1] N번 반복하면서 노선 입력, 빈도수 표시
    cnts =  [0] * 5000
    for _ in range(N):
        S, E = map(int,input().split())
        for i in range(S, E + 1):
            cnts[i] += 1

    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])

    print(f'#{test_case}', *alst)