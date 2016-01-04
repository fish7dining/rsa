
import random

class rsa():
    def __init__(self):
        self.x = 1
        self.y = 0
        self.mainProcess()
    def mod_mul(self, a, b, n): # a * b % n
        res = 0
        while b != 0:
            if (b & 1) > 0:
                res = ( res + a ) % n
            a = ( a + a ) % n
            b >>= 1
        return res
    def mod_exp(self, a, b, n): # a ^ b % n
        res = 1
        while b != 0:
            if (b & 1) > 0:
                res = self.mod_mul(res, a, n)
            a = self.mod_mul(a, a, n)
            b >>= 1
        return res
    def Miller_Rabin(self, n):
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
            return True
        if n == 1 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0 or (n % 7) == 0 or (n % 11) == 0:
            return False
        u = n - 1
        k = 0
        while (u & 1) == 0:
            k += 1
            u >>= 1
        for i in range(777):
            x = random.randint(2, n - 1) + 2
            if (x % n == 0):
                continue
            x = self.mod_exp(x, u, n)
            pre = x
            for j in range(k):
                x = self.mod_mul(x, x, n)
                if x == 1 and pre != 1 and pre != n - 1:
                    return False
                pre = x
            if x != 1:
                return False
        return True
    def exgcd(self, a, b):
        if b == 0:
            self.x = 1
            self.y = 0
            return a
        res = self.exgcd(b, a % b)
        t = self.x
        self.x = self.y
        self.y = t - a / b * self.y
        return res
    def mainProcess(self):
        self.P = random.randint(99999999999999999999, 999999999999999999999)
        while self.Miller_Rabin(self.P) == False:
            self.P = random.randint(99999999999999999999, 999999999999999999999)
        self.Q = random.randint(99999999999999999999, 999999999999999999999)
        while self.Miller_Rabin(self.Q) == False or self.P == self.Q:
            self.Q = random.randint(99999999999999999999, 999999999999999999999)
        print 'p:',self.P
        print 'q:',self.Q
        self.N = self.P * self.Q
        print 'n:',self.N
        self.E = (self.P - 1) * (self.Q - 1) - 1
        print 'e:',self.E
        self.exgcd(self.E, (self.P - 1) * (self.Q - 1))
        self.D = self.x
        while self.D < 0:
            self.D += (self.P - 1) * (self.Q - 1)
        print 'd:',self.D
        print '--------------------------------------------encryption:'
    def encryption(self, data):
        self.C = []
        for i in data:
            self.C.append(self.mod_exp(ord(i), self.E, self.N))
        for i in self.C:
            print i
        print '--------------------------------------------decryption:'
    def decryption(self,):
        self.M = []
        for i in self.C:
            self.M.append(self.mod_exp(i, self.D, self.N))
        for i in self.M:
            print chr(i),
        print
        print '--------------------------------------------2'

test1 = rsa()
test1.encryption('HelloWorld')
test1.decryption()