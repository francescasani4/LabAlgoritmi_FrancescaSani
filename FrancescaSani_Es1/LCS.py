from itertools import combinations
class LCS:
    def __init__(self, sequence):
        self.sequence = sequence
        self.lenght = 0

    def allSubsequences(self, s):
        out = set()

        for r in range(1, len(s) + 1):
            for c in combinations(s, r):
                out.add(''.join(c))

        return sorted(out)

    # algoritmo forza-bruta
    def lcs_bruteForce(self, s):
        substrings = self.allSubsequences(self.sequence)
        self.lenght = 0

        for i in range(len(substrings)):
            sub = substrings[i]
            index = -1
            maxL = 0
            maxSub = ''

            for j in range(len(sub)):
                found = False

                for k in range(len(s)):
                    if sub[j] == s[k] and index < k and found == False:
                        maxL += 1
                        index = k
                        maxSub += sub[j]
                        found = True

            if maxL > self.lenght:
                self.lenght = maxL
                self.result = maxSub

        return self.lenght

    # algoritmo ricorsivo
    def lcs_recursive(self, s):
        m = len(self.sequence) - 1
        n = len(s) - 1

        self.lenght = self.lcs_rec(s, m, n)

        return self.lenght

    def lcs_rec(self, s, m, n):
        if m < 0 or n < 0:
            return 0
        elif self.sequence[m] == s[n]:
            return 1 + self.lcs_rec(s, m - 1, n - 1)
        else:
            return max(self.lcs_rec(s, m, n - 1), self.lcs_rec(s, m - 1, n))

    # algoritmo ricorsivo con memoization
    def lcs_memoization(self, s):
        m = len(self.sequence)
        n = len(s)

        c = [[0 for x in range(m + 1)] for y in range(n + 1)]
        self.lenght = self.lcs_recMemoization(s, c, m, n)

        return self.lenght

    def lcs_recMemoization(self, s, c, m, n):
        if c[m][n] != 0:
            return c[m][n]
        elif m <= 0 or n <= 0:
            return 0
        elif self.sequence[m - 1] == s[n - 1]:
            c[m][n] = 1 + self.lcs_recMemoization(s, c, m - 1, n - 1)
            return c[m][n]
        else:
            c[m][n] = max(self.lcs_recMemoization(s, c, m, n - 1), self.lcs_recMemoization(s, c, m - 1, n))
            return c[m][n]

    # algoritmo bottom-up
    def lcs_bottomUp(self, s):
        m = len(self.sequence)
        n = len(s)

        c = [[0 for x in range(m + 1)] for y in range(n + 1)]

        for i in range(1, m + 1):
            c[0][i] = 0
        for j in range(1, n + 1):
            c[j][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.sequence[i - 1] == s[j - 1]:
                    c[j][i] = c[j - 1][i - 1] + 1
                elif c[j - 1][i] >= c[j][i - 1]:
                    c[j][i] = c[j - 1][i]
                else:
                    c[j][i] = c[j][i - 1]

        self.lenght = c[n][m]

        return self.lenght