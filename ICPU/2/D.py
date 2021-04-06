while True:
    n = int(input())
    a = [int(input()) for _ in range(n)]
    dp = [[0] for _ in range(n)]
    dp.append([0])
    print(dp)
