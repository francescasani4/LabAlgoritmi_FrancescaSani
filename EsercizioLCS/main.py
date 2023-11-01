#LCS versione ricorsiva
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


#LCS versione forza-bruta
def lcs_bruteforce(X, Y):
    m, n = len(X), len(Y)
    #print(m, n)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    #print(dp)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))


def LCS_bruteforce(X, Y):
    max_lcs = ""
    m, n = len(X), len(Y)

    for i in range(2 ** m):
        subsequence = "".join([X[j] for j in range(m) if (i & (1 << j)) > 0])

        is_valid_subsequence = True
        i, j = 0, 0

        while i < len(subsequence) and j < n:
            if subsequence[i] == Y[j]:
                i += 1
            j += 1

        if i < len(subsequence):
            is_valid_subsequence = False

        if is_valid_subsequence and len(subsequence) > len(max_lcs):
            max_lcs = subsequence

    return max_lcs



if __name__ == '__main__':
    S1 = "AGGTABCDEF"
    S2 = "GXTXAYBCDEF"
    print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))

    print("--------")
    # Esempio di utilizzo
    X = "AGGTABCDEF"
    Y = "GXTXAYBCDEF"
    result = lcs_bruteforce(X, Y)
    print("Lunghezza della LCS:", len(result))
    print("LCS:", result)

    print("--------")
    # Esempio di utilizzo
    X = "AGGTABCDEF"
    Y = "GXTXAYBCDEF"
    result = LCS_bruteforce(X, Y)
    print("Lunghezza della LCS:", len(result))
    print("LCS:", result)


