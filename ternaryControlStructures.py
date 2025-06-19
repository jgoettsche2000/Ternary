
# Class definition
class Ternary():
    def __init__(self, value):
        t = {True, False, None}
        self.value = value

    def __str__(self):
        if self.value:
            return 'True'
        elif self.value == None:
            return 'Unknown'
        return 'False'
    
    def __repr__(self):
        if self.value:
            return "<class 'Ternary(True)'>"
        elif self.value == None:
            return "<class 'Ternary(Unknown)'>"
        return "<class 'Ternary(False)'>"
    
    def __and__(self, other):
        if type(other) == "<class 'bool'>":
            if (self.value == True) and (other == True):
                return Ternary(True)
            if (self.value == False) or (other == False):
                return Ternary(False)
            return Ternary(None)
        else:
            if (self.value == True) and (other.value == True):
                return Ternary(True)
            if (self.value == False) or (other.value == False):
                return Ternary(False)
            return Ternary(None)
        
    def __rand__(self, other):
        print(type(other))
        if str(type(other)) == "<class 'bool'>":
            if (self.value == True) and (other == True):
                return Ternary(True)
            if (self.value == False) or (other == False):
                return Ternary(False)
            return Ternary(None)
        else:
            if (self.value == True) and (other.value == True):
                return Ternary(True)
            if (self.value == False) or (other.value == False):
                return Ternary(False)
            return Ternary(None)
    
    def __or__(self, other):
        if str(type(other)) == "<class 'bool'>":
            if (self.value == True) or (other == True):
                return Ternary(True)
            if (self.value == False) and (other == False):
                return Ternary(False)
            return Ternary(None)
        else:
            if (self.value == True) or (other.value == True):
                return Ternary(True)
            if (self.value == False) and (other.value == False):
                return Ternary(False)
            return Ternary(None)
        
    def __ror__(self, other):
        if str(type(other)) == "<class 'bool'>":
            if (self.value == True) or (other == True):
                return Ternary(True)
            if (self.value == False) and (other == False):
                return Ternary(False)
            return Ternary(None)
        else:
            if (self.value == True) or (other.value == True):
                return Ternary(True)
            if (self.value == False) and (other.value == False):
                return Ternary(False)
            return Ternary(None)
    
    def __not__(self):
        if self.value == True:
            return Ternary(False)
        if self.value == None:
            return Ternary(None)
        return Ternary(True)
    
    def __xor__(self, other):
        if str(type(other)) == "<class 'bool'>":
            if ((self.value == True) and (other == True)) or ((self.value == False) and (other == False)):
                return Ternary(True)
            if ((self.value == True) and (other == False)) or ((self.value == False) and (other == True)):
                return Ternary(False)
            return Ternary(None)
        else:
            if ((self.value == True) and (other.value == True)) or ((self.value == False) and (other.value == False)):
                return Ternary(True)
            if ((self.value == True) and (other.value == False)) or ((self.value == False) and (other.value == True)):
                return Ternary(False)
            return Ternary(None)
        
    def __rxor__(self, other):
        if str(type(other)) == "<class 'bool'>":
            if ((self.value == True) and (other == True)) or ((self.value == False) and (other == False)):
                return Ternary(True)
            if ((self.value == True) and (other == False)) or ((self.value == False) and (other == True)):
                return Ternary(False)
            return Ternary(None)
        else:
            if ((self.value == True) and (other.value == True)) or ((self.value == False) and (other.value == False)):
                return Ternary(True)
            if ((self.value == True) and (other.value == False)) or ((self.value == False) and (other.value == True)):
                return Ternary(False)
            return Ternary(None)
        
    def __int__(self):
        if self.value == True:
            return 1
        elif self.value == None:
            return 0
        return -1
    
    def __add__(self, other):
        return self.__int__() + other
    
    def __radd__(self, other):
        return other + self.__int__()
    
    def __sub__(self, other):
        return self.__int__() - other
    
    def __rsub__(self, other):
        return other - self.__int__()
    
    def __mul__(self, other):
        return self.__int__() * other
    
    def __rmul__(self, other):
        return other * self.__int__()
    
    def __truediv__(self, other):
        return self.__int__() / other
    
    def __rtruediv__(self, other):
        return other / self.__int__()
    
    def __floordiv__(self, other):
        return self.__int__() // other
    
    def __rfloordiv__(self, other):
        return other // self.__int__()
    
    def __mod__(self, other):
        return self.__int__() % other
    
    def __rmod__(self, other):
        return other % self.__int__()
    
    def __pow__(self, other):
        return self.__int__() ** other
    
    def __rpow__(self, other):
        return other ** self.__int__()
    
# Testing
def main():
    t = Ternary(None)
    print(str(t // 5))

if __name__ == '__main__':
    main()
