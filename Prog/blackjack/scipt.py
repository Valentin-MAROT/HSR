from pwn import *
import random

p=remote('10.22.148.14', 15042)


def mise():
    buf=p.recvuntil(B']: ').decode()
    print(buf)
    p.sendline(B'5')

mise()

while True:

    buf = p.recvuntil(B')\n').decode()
    print(buf)
    #je récupere une chaine de ce genre:
    #Bank hand: [10♣, hidden]\n
    #Player hand: [10♠, 5♦]\n

    #je récupere les cartes de la banque
    buf = p.recvuntil(B'\n').decode()
    print(buf)
    #je récupere les cartes du joueur
    buf = p.recvuntil(B'\n').decode()
    print(buf)





