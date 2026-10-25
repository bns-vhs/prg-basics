###
# Program conducting a simple survey with yes/no questions
#

print("SURVEY")

q1 = input("Are you interested in computer science? (y/n): ") == 'y'
q2 = input("Do you like playing computer games? (y/n): ") == 'y'
q3 = input("Do you have an Instagram account? (y/n): ") == 'y'

ans1 = "Yes" if q1 else "No"
ans2 = "Yes" if q2 else "No"
ans3 = "Yes" if q3 else "No"

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {ans1}")
print(f"Playing computer games: {ans2}")
print(f"Has an Instagram account: {ans3}")