import random

wordbank= ["indentation", "spaces"] 

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num = int(input('Choose a number between 0 and 20: '))

student_name = tlgstudents[num]

print(f'{student_name} always uses <{wordbank[2]}> <{wordbank[1]}> to indent')

bonus1_studentName = random.choice(tlgstudents)

print(bonus1_studentName)

