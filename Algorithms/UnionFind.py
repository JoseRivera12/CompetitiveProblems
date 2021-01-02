class QuickFindUF:
    def __init__(self, N):    
        self.id = list()
        for i in range(0, N):
            self.id.append(i)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def __root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    #Quick union
    def union(self, p,q):
        i = self.__root(p)
        j = self.__root(q)
        self.id[i] = j

    #Quadratic in union 
    # def union(self, p, q):
    #     pid = self.id[p]
    #     qid = self.id[q]
    #     for i in range (0,len(self.id)):
    #         if self.id[i] == pid:
    #             self.id[i] = qid

def main():
    quickFind = QuickFindUF(10)
    quickFind.union(0,9)
    quickFind.union(0,1)
    print(quickFind.id)

if __name__ == "__main__":
    main()