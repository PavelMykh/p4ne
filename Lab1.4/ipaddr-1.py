from ipaddress import *
import random

class IPv4RandomNetwork (IPv4Network):
    def __init__(self, n1='11.0.0.0', n2='223.0.0.0', p1=8, p2=24):
        net = (random.randrange(int(IPv4Address(n1)), int(IPv4Address(n2))))
        pref = (random.randrange(p1, p2 + 1))
        IPv4Network.__init__(self, (net, pref), strict=False)

def ind(x1, x2):
    ind1 = (int(x2) * 10**12 + int(x1))
    return ind1
L = []
num = 50
n1='11.0.0.0'
n2='223.0.0.0'
p1=8
p2=24
#num =int(input('Enter number of subnets, integer (default 50):') or 50)
#n1 =str(input('Enter start net, default 11.0.0.0:') or '11.0.0.0')
#n2 =str(input('Enter end net, default 223.0.0.0:') or '223.0.0.0')
#p1 =int(input('Enter start prefix, default 8:') or 8)
#p2 =int(input('Enter end prefix, default 24:') or 24)

x = IPv4RandomNetwork()
while len(L) < num:
    if x not in L:
        L = L + [x]
        x = (IPv4RandomNetwork())

#for i in range(num):
#print(L[3].network_address)
#print(L[3].prefixlen)
#print(ind((L[3].network_address), (L[3].prefixlen)))



sort = [[]]
for gen in range(0, 32):
    sort = sort + [[]]
for m in range(p1, (p2 + 1)):
    for ne in L:
        if ne.prefixlen == m:
            sort[m] = sort[m] + [ne]


for masp in range(p1, (p2 + 1)):
    if len(sort[masp]) > 0:
        for mmm in sort[masp]:
            print(mmm)

