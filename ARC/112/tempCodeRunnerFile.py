potato,  carrot, onion = map(int, input().split())

print(max(1-potato, 0)+max(2-carrot, 0)+max(3-onion, 0))
