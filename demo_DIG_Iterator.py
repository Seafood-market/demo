class Counter(object):
    def __init__(self,start,stop):
        self.current = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        
        else:
            c = self.current
            self.current += 1
        return c

for c in Counter(101,103):
    print(c,sep=',')

c=Counter(201,203)

while True:
    try:
        print(next(c),sep=',')
    
    except StopIteration:
        break