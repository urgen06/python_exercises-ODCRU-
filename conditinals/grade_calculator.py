"""Ask the user for a score (0–100) and print the letter grade: A (90+), B (80–89), C (70–79), D (60–69), F (below 60).

Use if/elif/else
Handle invalid input (negative or >100)"""


try:
    marks = int(input("Enter marks (0-100): ") )
    if marks < 0 or marks > 100:
        raise ValueError
except ValueError:
        print("Invalid marks. Marks should be positive and >= 100")
        exit()
    
    
if marks >= 90:
    print("you have got Grade A")
elif marks >= 80:
    print("you have got Grade B")
elif marks >= 70:
    print("you have got Grade C")
elif marks >=60:
    print("you have got Grade D")
else:
    print("you have got Grade F")


 
