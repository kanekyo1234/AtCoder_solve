n = int(input())
a=[".###..#..###.###.#.#.###.###.###.###.###.",
   ".#.#.##....#...#.#.#.#...#.....#.#.#.#.#.",
   ".#.#..#..###.###.###.###.###...#.###.###.",
   ".#.#..#..#.....#...#...#.#.#...#.#.#...#.",
   ".###.###.###.###...#.###.###...#.###.###."]
s=[list(str(input())) for _ in range(5) ]

jugh = [12, 8, 11, 11, 9, 11, 12, 7, 13, 12]
for i in range(5):
    a[i] = list(a[i])

for i in range(n): # s
    for j in range(10): #a
        count = 0
        for k in range(5):
            for l in range(1,4):
               # print(s[k][l+i*4],end="")
                #print(a[k][l + j * 4],end="")
                if s[k][l + i * 4] == a[k][l + j * 4]:
                    count+=1
                else:
                    count-=1000
        
       # print(count)
        if count == 15:
            print(j,end="")
            break
    

