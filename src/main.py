import sys


def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    k = int(lines[0])
    values = {}

    for i in range(1, k + 1):
        ch, val = lines[i].split()
        values[ch] = int(val)

    A = lines[k + 1]
    B = lines[k + 2]

    return values, A, B


def solve(values, A, B):
    n = len(A)
    m = len(B)

    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + values[A[i - 1]]
                )
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    subsequence = []
    i, j = n, m

    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1] and dp[i][j] == dp[i - 1][j - 1] + values[A[i - 1]]:
            subsequence.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1

    subsequence.reverse()
    return dp[n][m], "".join(subsequence)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        return

    values, A, B = read_input(sys.argv[1])
    max_value, subsequence = solve(values, A, B)

    print(max_value)
    print(subsequence)


if __name__ == "__main__":
    main()