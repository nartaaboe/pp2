N = int(input())
class numbersUpToN:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < N:
            self.a += 1
            return self.a * self.a
        else:
            raise StopIteration
myclass = numbersUpToN()
myit = iter(myclass)
for i in myit:
    print(i, end = " ")