def gerador(max_number):
    r = []
    for c in range(max_number + 1):
        r.append(c)


g = gerador(623*10**21)
for v in g:
    print(v)