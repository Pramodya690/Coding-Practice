"""Given the first 2 terms a1 and a2 of an Arithmetic Series. Find the nth term of the series. 

Examples:

Input: a1 = 2, a2 = 3, n = 4
Output: 5
Explanation: The series is: 2,3,4,5,6.... Thus, the 4th term is 5.
Input: a1 = 1, a2 = 3, n = 10
Output: 19
Explanation: The series is: 1,3,5,7,9,11,13,15,17,19,21.. Thus, the 10th term is 19."""



def print_series(a1,a2,n):

    result = []
    i = 1
    gap =int( a2 - a1)
    while i <= n:
        
        result.append(a1)
        a1 = a1 + gap
        i = i+1
    return result

a1 = int(input("Enter a1 "))
a2 = int(input("Enter a2 "))
n = int(input("Enter n "))

output = print_series(a1,a2,n)
print(output[n-1])


        