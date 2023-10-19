from pwn import *
import time

cnt = 0
while True:
    cnt += 1
    time.sleep(3)
    print(f"Try {cnt}")
    p = remote("prob16.geekgame.pku.edu.cn", 10016)

    p.recvuntil(b"token: ")
    p.sendline(b"56:MEUCIB95OPBgEJNiIhO7mQhh_9Jshx-8jiz4o5J6GXHsXJwwAiEAvfambFs2zMUIA1ASGa7q5f6OjZNh3r3RSdY5czagnUc=")
    p.recvuntil(b"[...]: ")
    p.sendline(b"newgame")

    x = p.recvuntil(b"[...]: ")
    p.sendline(b"RayW")
    p.recvuntil(b"(y/n) ")
    p.sendline(b"y")


    # call help until sanity reaches 127
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"h")
    x = p.recvuntil(b"[RayW]: ")
    if x.find(b'109') == -1:
        p.close()
        continue
    p.sendline(b"h")
    x = p.recvuntil(b"[RayW]: ")
    if x.find(b'118') == -1:
        p.close()
        continue
    p.sendline(b"h")
    x = p.recvuntil(b"[RayW]: ")
    if x.find(b'127') == -1:
        p.close()
        continue

    # pickup brass key and return to dark room
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"e")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"pickup key")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"s")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"s")

    # pickup and use trinket
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"e")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"e")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"e")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"pickup trinket")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"use trinket")

    # open brass door
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"s")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"usewith key door")

    # pickup gold key
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"s")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"pickup key")
    
    # drink latte
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"s")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"e")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"e")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"e")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"s")
    
    # open gold door
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"w")
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"usewith key door")
    
    # get out
    p.recvuntil(b"[RayW]: ")
    p.sendline(b"n")
    x = p.recvuntil(b"[...]: ")
    with open('res.txt', 'wb') as f:
        f.write(x)

    p.close()
    break