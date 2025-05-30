"""Create the multiplication table from 1 to 10 for a given number n and return the table as an array.

Examples:

Input: n = 9
Output: 9 18 27 36 45 54 63 72 81 90
Input: n = 2
Output: 2 4 6 8 10 12 14 16 18 20"""

def multiplication_table(n):
    result = []

    i = 1
    while i <= 10:
        result.append(i * n)
        i = i+1
    return result   

n = int(input("Enter the number")) #[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# n = input("Enter the number") #['3', '33', '333', '3333', '33333', '333333', '3333333', '33333333', '333333333', '3333333333']
output = multiplication_table(n)
print(output) 




