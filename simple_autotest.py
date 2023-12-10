from functions import salary,hello_who

assert hello_who('Kostya') == 'Hello,Kostya', 'Hello who error'
assert hello_who('Leo') == 'Hello,Leo', 'Hello who error'
assert hello_who('Nikita') == 'Hello,Nikita', 'Hello who error'
assert salary(hours=2, salary_by_hour=1) == 4
assert salary(hours=2, salary_by_hour=2) == 8
