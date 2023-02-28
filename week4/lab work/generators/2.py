class printEvenNumbers:
    def __init__(self, n):
        self.n = n + 1
    def __iter__(self):
        for i in range(self.n):
            if i % 2 == 0:
                yield i

n = int(input())
even_numbers = printEvenNumbers(n)
print(" ".join(str(i) for i in even_numbers))