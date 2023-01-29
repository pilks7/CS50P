

class Jar:
    def __init__(self, capacity=12):
            self.capacity = capacity
            self.size = 0

    def __str__(self):
        return '🍪' * self.size  

    def deposit(self, n):
        # n = int(input("deposit some cookies: "))
        if self.size + n > self.capacity:
            raise ValueError("Jar can only hold {self.capacity} cookies max")
        self.size += n 

    def withdraw(self, n):
        # n = int(input('Withdraw some cookies: '))
        if n > self.size:
            raise ValueError("Not enough cookies...")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('capacity cannot be less than zero')
        self._capacity = capacity
        

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

jar = Jar(12)