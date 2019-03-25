class Huffman :
    
    def __init__(self):
        self.pq = []

    def create_pq(self):
        self.pq = []
        return self.pq

    def add_last(self,pq, c):
        pq.append(c)
    
    def root(self, pq):
        return 0

    def set_root(self, pq, c):
        if len(pq) != 0:
            pq[0] = c

    def get_data(self, pq, p):
        return pq[p]

    def children(self, pq, p):
        if 2*p + 2 < len(pq):
            return [2*p + 1, 2*p + 2]
        else:
            return [2*p + 1]

    def parent(self, p):
        return (p - 1) // 2

    def exchange(self, pq, p1, p2):
        pq[p1], pq[p2] = pq[p2], pq[p1]

    def insert_in_pq(self, pq, c):
        self.add_last(pq, c)
        i = len(pq) - 1
        while i != self.root(pq) and self.get_data(pq, i) < self.get_data(pq, self.parent(i)):
            p = self.parent(i)
            self.exchange(pq, i, p)
            i = p

    def extract_last_from_pq(self, pq):
        return self.pq.pop()

    def has_children(self, pq, p):
        return 2*p + 1 < len(pq)

    def extract_min_from_pq(self, pq):
        c = pq[self.root(pq)]
        self.set_root(pq, self.extract_last_from_pq(pq))
        i = self.root(pq)
        while self.has_children(pq, i):
            # Use the data stored at each child as the comparison key
            # for finding the minimum.
            j = min(self.children(pq, i), key=lambda x: self.get_data(pq, x))
            if self.get_data(pq, i) < self.get_data(pq, j):
                return c        
            self.exchange(pq, i, j)
            i = j
        return c