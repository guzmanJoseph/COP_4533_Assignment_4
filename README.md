# COP 4533 – Assignment 4  

### Students
Joseph Guzman - 69641535


## How to Run

From the main project directory:

py src/main.py data/file1.in

Question 1: The graph for question 1 can be found in data/runtime_graph.png. To run the command to get the graph you need to run py src/benchmark.py. The matplotlib package is required to run this task

Question 2: OPT(i,j) = max value of a common subsequence using the first i characters of A and the first j characters of B

Base Cases: OPT(0,j) = 0, OPT(i,0) = 0

Recurrence: 
if A[i] == B[j]:
    OPT(i, j) = max(
        OPT(i-1, j),
        OPT(i, j-1),
        OPT(i-1, j-1) + value(A[i])
    )

if A[i] != B[j]:
    OPT(i, j) = max(
        OPT(i-1, j),
        OPT(i, j-1)
    )

This recurrence is correct because at each step we either include the matching character (adding its value) or skip a character from one of the strings, ensuring all possibilities are considered.

Question 3:
for i from 1 to n:
    for j from 1 to m:
        if A[i] == B[j]:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i][j-1],
                dp[i-1][j-1] + value(A[i])
            )
        else:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i][j-1]
            )

Time Complexity: O(nm) because we have two for loops