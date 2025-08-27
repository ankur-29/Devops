age = int(input('hi, Enter your age : '))
#print('YOU ARE ' + age + ' YEARS OLD')

if age >= 18:
    print('you are eligible for voting.')
else :
    print('you are not eligible for voting')

#if, else and else-if example
marks = int(input("Hi, Enter your test marks : "))
grade = ''
if marks >= 90 :
    grade = 'A'
elif marks >= 80 :
    grade = 'B'
elif marks >= 70 :
    grade = 'C'
elif marks >= 60 :
    grade = 'D'
elif marks >= 50 :
    grade = 'E'
else :
    grade = 'F'

print('Your grade is : ' + grade)
