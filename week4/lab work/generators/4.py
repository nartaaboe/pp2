class atAtoB:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __iter__(self):
        self.current = a
        return self
    def __next__(self):
        if self.current < self.b:
            result = pow(self.current, 2)
            self.current += 1
            return result
        else:
            raise StopIteration
a = int(input())
b = int(input())
fourth_one = atAtoB(a, b)
print(" ".join(str(i) for i in fourth_one))