class disjoint_set():
    def __init__(self,n):
        self.S=[i for i in range(n)]
    def union(self,i,j):
        p1=self.parent(i)
        p2=self.parent(j)
        self.S[p1]=p2
    def parent(self,i):
        root=i
        while self.S[root]!=root:
            root=self.S[root]
        while self.S[i]!=i:
            x=i
            i=self.S[i]
            self.S[x]=root
        return root