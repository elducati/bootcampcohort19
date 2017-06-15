class BinarySearch():
    
    def __init__(self, the_length, step):
        self.alist = [i for i in range(0 + step, the_length * step, step)]
        self.length = the_length
        self.step = step
        self.first = 2
        self.last = self.length
        self.counter = 0
        self.found = False
        self.mid = (self.first + self.last) // 2

    def search(self, val):
        while self.first <= self.last and not self.found:
            self.mid = (self.first + self.last) // 2
            self.counter += 1
            if self.alist[self.mid] == val:
                self.found = True
            else:
                if val <= self.alist[self.mid]:
                    self.last = self.mid
                    self.search(val)
                else:
                    self.first = self.mid
                    self.search(val)

            return {'count': self.counter, 'index': self.mid}
