def f(x: str) -> str:
    ss = [x[i:i+16] for i in range(0, len(x), 16)]
    ss = [[s[i:i+2] for i in range(0, 16, 2)][::-1] for s in ss]
    ss = sum(ss, [])
    ss = [s for s in ss if s != '']
    ss = list(map(lambda x: chr(int(x, 16)), ss))
    print(''.join(ss))

f('3465527b67616c6646546e3172505f646f735f654430635f000a7d597a34655f')
