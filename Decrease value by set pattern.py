s = set([12,10, 13, 15, 8, 9])
for i in range(len(s), 0, -1):
    print(s)
    s.remove(max(s))