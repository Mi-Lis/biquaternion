import numpy
from pyquaternion import Quaternion
from dataclasses import dataclass
from dual_quaternions import DualQuaternion
@dataclass
class Bi_Num:
    polar = False  
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.a = x[0][0]
            self.b = x[0][1]
        else:
            if ('r' in kwargs) and ('phi' in kwargs):
                x,y = kwargs.get('r'), kwargs.get('phi')
                self.r = x
                self.phi = y
                self.polar = True
            else:
                x,y = args
                self.a = x
                self.b = y              
    def norm(self):
        return abs(self.a)
    def __neg__(self):
        return Bi_Num(-self.a, -self.b)
    def inv(self):
        return Bi_Num(self.a, -self.b)   
    def __add__(self, b):
        if type(b) is Bi_Num:
            return Bi_Num(self.a+b.a, self.b+b.b)
        else:
            return Bi_Num(self.a+b, self.b) 
    def __sub__(self, b):
        if type(b) is Bi_Num:
            return Bi_Num(self.a-b.a, self.b-b.b)
        else:
            return Bi_Num(self.a-b, self.b) 
    def __mul__(self, b):
        if type(b) is Bi_Num:
            return Bi_Num(self.a*b.a, self.a*b.b + self.b*b.a)
        else:
            return Bi_Num(self.a*b, self.b*b)    
    def __str__(self):
        if self.polar == False:
            if isinstance(self.a, (int, float, numpy.float64)):
                if self.b == 0.0:
                    return str(self.a)
                if self.b > 0.0:
                    return '{}+s*{}'.format(self.a, self.b)
                if self.b < 0.0:
                    return '{}-s*{}'.format(self.a, abs(self.b))
            else:
                return '({})+s*({})'.format(self.a, self.b)
        if self.polar == True:
            if self.r == 0:
                return str(0)
            if self.r == 1:
                return '1+s*{}'.format(self.phi)
            if self.r!=0:
                return '{}(1+s*{})'.format(self.r, self.phi)
    def __pow__(self, y):
        return Bi_Num(self.a**y, y*self.a**(y-1)*self.b)
    def __iadd__(self, b):
        if type(b) is Bi_Num:
            return Bi_Num(self.a+b.a, self.b+b.b)
        else:
            return Bi_Num(self.a+b, self.b)
    def __isub__(self, b):
        if type(b) is Bi_Num:
            return Bi_Num(self.a-b.a, self.b-b.b)
        else: 
            return Bi_Num(self.a-b, self.b)
    def __imul__(self, b):
        if type(b) is Bi_Num:
            return Bi_Num(self.a*b.a, self.a*b.b + self.b*b.a)
        else:
            return Bi_Num(self.a*b, self.b*b) 
    def __truediv__(self, b):
        if type(b) is Bi_Num:
            if b.a == 0:
                print("Нельзя")
                return False
            return Bi_Num((self.a/b.a),((-self.a*b.b + self.b*b.a)/b.a**2))
        else:
            return Bi_Num(self.a/b, self.b/b)
    def __truediv__(self, b):
        if type(b) is Bi_Num:
            if b.a == 0:
                print("Нельзя")
                return False
            return Bi_Num((self.a/b.a),((-self.a*b.b + self.b*b.a)/b.a**2))
        else:
            return Bi_Num(self.a/b, self.b/b)
    def __getitem__(self, i):
            if i == 0:
                return self.a
            if i == 1:
                return self.b
@dataclass
class Bi_Quaternion:
    def __init__(self, *args, **kwargs):
        if len(args)==4:
            _a,_b,_c,_d = args
            self.q = [_a,_b,_c,_d]
            self.a = _a
            self.b = _b
            self.c = _c
            self.d = _d
        
        if len(args)==2:
            l_1, l_2 = args
            self.q = [l_1, l_2]
            self.a = l_1
            self.b = l_2
    def __str__(self):
        if len(self.q) == 4:
            return '({})+({})*i+({})*j+({})*k'.format(self.a, self.b, self.c, self.d)
        if len(self.q) == 2:
            return '({})+s({})'.format(self.a, self.b)
    def __sub__(self, b):
        if type(b) is Bi_Quaternion:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is Bi_Num:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a-b, self.b)
    def __isub__(self, b):
        if type(b) is Bi_Quaternion:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a-b.a, self.b-b.b, self.c-b.c, self.d-b.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a-b.a, self.b-b.b)
        elif type(b) is Bi_Num:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a-b.a, self.b-b.b)
        else:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a-b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a-b, self.b)
    def __add__(self, b):
        if type(b) is Bi_Quaternion:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a+b.a, self.b+b.b)
        elif type(b) is Bi_Num:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a+b.a, self.b+b.b)
        else:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a+b, self.b)
    def __iadd__(self, b):
        if type(b) is Bi_Quaternion:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a+b.a, self.b+b.b, self.c+b.c, self.d+b.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a+b.a, self.b+b.b)
        elif type(b) is Bi_Num:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a+b.a, self.b+b.b)
        else:
            if len(self.q) == 4:
                return Bi_Quaternion(self.a+b, self.b, self.c, self.d)
            if len(self.q) == 2:
                return Bi_Quaternion(self.a+b, self.b)
    def __mul__(self, b):
        if type(b) is Bi_Quaternion:
            if len(self.q) == 2 and len(b.q)==2:
                return Bi_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
            elif len(self.q) == 4 and len(b.q)==4:
                return Bi_Quaternion(-b.b * self.b - b.c * self.c - b.d * self.d + b.a * self.a,
                     b.b * self.a + b.c * self.d - b.d * self.c + b.a * self.b,
                     -b.b * self.d + b.c * self.a + b.d * self.b + b.a *self.c,
                     b.b * self.c - b.c * self.b + b.d * self.a + b.a *self.d)
            
            else:
                print('Приведите к единому типу')    
                return self
        else:
            if self.q == 2:
                return Bi_Quaternion(b*self.a, b*self.b)
            if self.q == 4:
                return Bi_Quaternion(b*self.a, b*self.b, b*self.c, b*self.d)      
    def __imul__(self, b):
        if type(b) is Bi_Quaternion:
            if len(self.q) == 2 and len(b.q)==2:
                return Bi_Quaternion(self.a*b.a, self.a*b.b + self.b*b.a)
            elif len(self.q) == 4 and len(b.q)==4:
                return Bi_Quaternion(-b.b * self.b - b.c * self.c - b.d * self.d + b.a * self.a,
                     b.b * self.a + b.c * self.d - b.d * self.c + b.a * self.b,
                     -b.b * self.d + b.c * self.a + b.d * self.b + b.a *self.c,
                     b.b * self.c - b.c * self.b + b.d * self.a + b.a *self.d)
            
            else:
                print('Приведите к единому типу')    
                return self
        else:
            if self.q == 2:
                return Bi_Quaternion(b*self.a, b*self.b)
            if self.q == 4:
                return Bi_Quaternion(b*self.a, b*self.b, b*self.c, b*self.d)
    def to_quaternions(self):
        _a = Quaternion(self.a.a, self.b.a, self.c.a, self.d.a)
        _b = Quaternion(self.a.b, self.b.b, self.c.b, self.d.b)
        self.a = _a
        self.b = _b
        self.q = [self.a, self.b]

        return Bi_Quaternion(self.a, self.b)
    def to_bi_num(self):
        _a = Bi_Num(self.a[0], self.b[0])
        _b = Bi_Num(self.a[1], self.b[1])
        _c = Bi_Num(self.a[2], self.b[2])
        _d = Bi_Num(self.a[3], self.b[3])
        self.a = _a
        self.b = _b
        self.c = _c
        self.d = _d
        self.q = [self.a, self.b, self.c, self.d]
        return Bi_Quaternion(self.a, self.b, self.c, self.d)
    def __neq__(self):
        if self.q == 2:
            return Bi_Quaternion(-self.a, -self.b)
    def inv(self):
        if len(self.q) == 2:
            return Bi_Quaternion(self.a.conjugate, self.b.conjugate)
        if len(self.q) == 4:
            return Bi_Quaternion(self.a.inv(), self.b.inv(), self.c.inv(), self.d.inv())
    def norm(self):
        if len(self.q) == 2:
            return Bi_Num((self*self.inv()).a[0], (self*self.inv()).b[0])
        if len(self.q) == 4:
            t = self.to_quaternions()
            return Bi_Num((t*t.inv()).a[0], (t*t.inv()).b[0])
    def __getitem__(self, i):
        if len(self.q) == 2:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
        if len(self.q) == 4:
            if i == 0:
                return self.a
            if i == 1:
                return self.b
            if i == 2:
                return self.c
            if i == 3:
                return self.d


l1 = Quaternion(1,1,1,1)
l2 = Quaternion(1,1,1,1)
v = Bi_Quaternion(l1,l2)
v = v.to_bi_num()
print(v.norm())