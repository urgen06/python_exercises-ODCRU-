"""Print a right-angled triangle of stars for a given height n. Row 1 has 1 star, row 2 has 2, etc.

"""

n = int(input("Enter the number of rows for your right-angled triangle: "))

for i in range(1,n+1):
    for j in range(i):
        print("*", end="")
    print()