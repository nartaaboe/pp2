class ReverseIterator:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.current = self.n
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            result = self.current
            self.current -= 1
            return result
        
lastn = int(input())
last_one = ReverseIterator(lastn)
print(" ".join(str(i) for i in last_one))