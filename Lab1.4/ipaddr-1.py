from ipaddress import IPv4Network
import random

class RandSub (IPv4Network):
    def __init__(self, nmin, nmax, pmin, pmax):
        IPv4Network.__init__(self, random.randrange(0x0B000000,0xDF000000), random.randint(8,24))