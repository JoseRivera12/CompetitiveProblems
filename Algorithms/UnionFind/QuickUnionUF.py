class QuickUnionUF:
    def __init__(self, n): 
        self.count = n
        self.parent = [i for i in range(n)]

    def count(self):
        """return the number of sets"""
        return self.count

    def validate(self, p):
        """validate p is a valid in index"""
        n = len(self.parent)
        if p < 0 or p >= n:
            raise ValueError("Invalid index")

    def find(self, p):
        """return the set of the container element"""
        self.validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def connected(self, p, q):
        """return if two elements are in the same set"""
        self.validate(p)
        self.validate(q)
        return self.parent[p] == self.parent[q]

    def union(self, p, q):
        """merges the set containing element p with the set of element q"""
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        self.parent[rootP] = rootQ
        self.count -= 1

def main():
    #Sets from https://algs4.cs.princeton.edu/15uf/
    with open("tinyUF.txt") as file:
        num_elems = file.readline()
        unionFind = QuickUnionUF(int(num_elems))
        input = [line.rstrip("\n").split(" ") for line in file.readlines()]
        for value in input:
            p = int(value[0])
            q = int(value[1])
            if unionFind.connected(p,q): continue
            unionFind.union(p, q)         
    
if __name__ == "__main__":
    main()