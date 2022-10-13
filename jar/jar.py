class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        updated_size = self.size + n

        if updated_size > self.capacity or n < 0:
            raise ValueError('Invalid deposit')

        self.size = updated_size

    def withdraw(self, n):
        updated_size = self.size - n

        if updated_size < 0 or n < 0:
            raise ValueError('Invalid withdraw')

        self.size = updated_size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError('Invalid capacity')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError('Invalid size')
        self._size = size


def main():
    jar1 = Jar()

    print(f'Jar capacity: {jar1.capacity}')
    print(f'Jar size: {jar1.size}')
    jar1.deposit(3)
    print(f'Jar size: {jar1.size}')
    jar1.withdraw(1)
    print(f'Jar size: {jar1.size}')
    print(jar1)

    print('\n\n')

    jar2 = Jar(20)

    print(f'Jar capacity: {jar2.capacity}')
    print(f'Jar size: {jar2.size}')
    jar2.deposit(10)
    print(f'Jar size: {jar2.size}')
    jar2.withdraw(3)
    print(f'Jar size: {jar2.size}')
    print(jar2)


if __name__ == '__main__':
    main()
