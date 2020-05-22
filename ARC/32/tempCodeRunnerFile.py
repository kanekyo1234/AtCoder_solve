
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
