h = list(map(int, input().strip().split(' ')))
w = input().strip()
a = 'abcdefghijklmnopqrstuvwxyz'
print(1 * len(w) * max([h[a.index(l)]for l in w]))
