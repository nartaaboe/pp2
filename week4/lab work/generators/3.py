class dividesOnlyThreeAndFour:
    def __init__(self, n):
        self.n = n + 1
    def __iter__(self):
        for i in range(self.n):
            if i % 3 == 0 and i % 4 == 0:
                yield i
n = int(input())
third_one = dividesOnlyThreeAndFour(n)
print(" ".join(str(i) for i in third_one))