"""Given two integers a and r i,e first term and common ratio of a GP series. Find the nth term of the series.
Note: As the answer can be rather large, print its modulo of 1000000007 (109 + 7).

Examples:

Input: a = 2, r = 2, n = 4
Output: 16
Explanation: The GP series is 2, 4, 8, 16, 32,... in which 16 is the 4th term.
Input: a = 4, r = 3, n = 3
Output: 36
Explanation: The GP series is 4, 12, 36, 108,.. in which 36 is the 3rd term."""

# def print_series(a,r,n):
#     result = []
#     i = 0
#     while i < 10:
#         result.append(a)
#         a = a * r
#         i = i+1
#     return result

def print_nth_gp_series(a,r,n):

    an = a*pow(r,n-1)
    return an


a = int(input("Enter a "))
r = int(input("Enter r "))
n = int(input("Enter n "))

output = print_nth_gp_series(a,r,n)
print(output)


    