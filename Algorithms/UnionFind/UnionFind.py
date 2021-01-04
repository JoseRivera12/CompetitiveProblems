class UnionFind:
    """initialize n sites whith integers(0 to n-1)"""
    def __init__(self, n):
        if n < 0:
            raise ValueError("n cant be lower to 0")
        self.count = n    
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def validate(self, p):
        """validate that p is a valid index"""
        n = len(self.parent)
        if(p < 0 or p >= n):
            raise ValueError("Invalid index")

    def find(self, p):
        """return element if the set containing element"""
        self.validate(p)
        while(p != self.parent[p]):
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, p, q):
        """merge the set containing element with the set containing element"""
        rootP = self.find(p) 
        rootQ = self.find(q)
        if rootP == rootQ:
            return 
        if self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        elif self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP]+=1
        self.count-=1

    def connected(self, p, q):
        """returns if the two elements are in the same set"""
        #Can be replaced with two calls of find 
        return self.find(p) == self.find(q) 

def main():
    with open("largeUF.txt") as file:
        num_elems = file.readline()
        unionFind = UnionFind(int(num_elems))
        input = [line.rstrip("\n").split(" ") for line in file.readlines()]
        for value in input:
            p = int(value[0])
            q = int(value[1])
            if unionFind.connected(p,q): continue
            unionFind.union(p, q)         

if __name__ == "__main__":
    main()