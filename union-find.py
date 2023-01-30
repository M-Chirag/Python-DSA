class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.size = {}

        # initialize all nodes as parents of themselves and having rank(height) =0
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
            self.size[i] = 1

    def find(self, n):

        if self.parent[n] == n:
            return n

        # recursively set the root of the tree as parent to all the subsequent nodes in the call stack -->
        # Path compression
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def unionByRank(self, n1, n2):

        parent1, parent2 = self.find(n1), self.find(n2)

        if parent1 == parent2:
            return False

        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1

        elif self.rank[parent2] < self.rank[parent1]:
            self.parent[parent1] = parent2

        else:
            # setting parent1 as parent2 so have to increase the rank of p2
            self.parent[parent1] = parent2
            self.rank[parent2] += 1

    def unionBySize(self, n1, n2):

        parent1, parent2 = self.find(n1), self.find(n2)

        if parent1 == parent2:
            return False

        if self.size[parent1] < self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]


uf = UnionFind(7)

# uf.unionByRank(1, 2)
# uf.unionByRank(2, 3)
# uf.unionByRank(4, 5)
# uf.unionByRank(6, 7)
# uf.unionByRank(5, 6)

# if uf.find(3) == uf.find(7):
#     print("Same")
# else:
#     print("Not Same")

# uf.unionByRank(3, 7)

# if uf.find(3) == uf.find(7):
#     print("Same")
# else:
#     print("Not Same")


uf.unionBySize(1, 2)
uf.unionBySize(2, 3)
uf.unionBySize(4, 5)
uf.unionBySize(6, 7)
uf.unionBySize(5, 6)

if uf.find(3) == uf.find(7):
    print("Same")
else:
    print("Not Same")

uf.unionByRank(3, 7)

if uf.find(3) == uf.find(7):
    print("Same")
else:
    print("Not Same")
