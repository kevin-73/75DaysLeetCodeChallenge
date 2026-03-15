MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.a = 1
        self.b = 0
        self.arr = []

    def append(self, val: int) -> None:
        inv = pow(self.a, MOD-2, MOD)
        self.arr.append((val - self.b) * inv % MOD)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % MOD

    def multAll(self, m: int) -> None:
        self.a = self.a * m % MOD
        self.b = self.b * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.a + self.b) % MOD
        