from functions import salary,hello_who

#print(hello_who('Kostya'))

print(salary(hours=9,salary_by_hour=10))

if salary (hours=9,salary_by_hour=10) != 180:
    print("Error")
if hello_who('Kostya') != 'Hello,Kostya':
    print('Failed')
else:
    print('Good')
if hello_who('Leo') != 'Hello,Leo':
    print('Falied')
else:
    print('Amazing')