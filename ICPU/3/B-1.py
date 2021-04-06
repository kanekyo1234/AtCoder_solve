while True:
    n = int(input())
    if n == 0:
        break
    w = []
    for i in range(n):
        word = input()
        w.append(word)
    ans = 100
    haiku = [5, 7, 5, 7, 7]
    for i in range(n-5):
        word_lengs = 0
        check_i = 0
        for j in range(i, n):
            if check_i == 5:
                ans = i
                break
            word_lengs += len(w[j])
            if word_lengs == haiku[check_i]:
                check_i += 1
                word_lengs = 0
            elif word_lengs > haiku[check_i]:
                break
        if ans != 100:
            a
            break
