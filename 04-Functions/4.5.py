###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 15:
        grade = 'Very Good'
    elif points >= 12:
        grade = 'Good'
    elif points >= 9:
        grade = 'Satisfactory'  
    else:
        grade = 'Fail'
    return grade

test_result = int(input('Enter the number of points obtained on the test: '))
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')