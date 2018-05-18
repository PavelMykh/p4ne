from ipaddress import IPv4Network
import random


class Sub:
    def __init__(self, n='11.0.0.0', p='/8'):
        self.net = n
        self.pre = p
    def __str__(self):
        return self.net + self.pre
    def getnet(self):
        return self.net
    def getpre(self):
        return self.pre


o1 = str(random.randint(11, 223))
o2 = str(random.randint(0, 255))
o3 = str(random.randint(0, 255))
p = '/' + str(random.randint(8, 24))
n = o1 + '.' + o2 + '.' + o3 + '.' + "0"
net = Sub(n, p)

print(net)
#listN = ['']
#for i in range(0,50):
