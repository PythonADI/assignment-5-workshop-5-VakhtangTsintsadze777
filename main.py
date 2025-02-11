# 1
language = 'english'
programming_language = 'python'
fruit = 'apple'
number = 10
color = 'blue'

print("\nis language == 'english'? i predict True")
print(language == 'english')
print("\nis language == 'georgian'? i predict False")
print(language == 'georgian')

print("\nis programming_language == 'python'? i predict True")
print(programming_language == 'python')
print("\nis programming_language == 'javascript'? i predict False")
print(programming_language == 'javascript')

print("\nis fruit == 'apple'? i predict True")
print(fruit == 'apple')
print("\nis fruit == 'banana'? i predict False")
print(fruit == 'banana')

print("\nis number == 10? i predict True")
print(number == 10)
print("\nis number == 5? i predict False")
print(number == 5)

print("\nis color == 'blue'? i predict True")
print(color == 'blue')
print("\nis color == 'red'? i predict False")
print(color == 'red')

# 2
# conditional_tests.py

# 3,4,5

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
elif alien_color == 'yellow':
    print("You just earned 10 points for shooting the alien!")
else:
    print("You just earned 15 points for shooting the alien!")


# 6

age = 3
person = ""
if age < 2:
    person = "baby"
elif 2 < age < 4:
    person = "toddler"
elif 4 < age < 13:
    person = "kid"
elif 13 < age < 20:
    person = "teenager"
elif 20 < age < 65:
    person = "adult"
elif age > 65:
    person = "elder"

print(person)

# 7


favorite_fruits = ["apple", "fig", "peach"]

if "banana" in favorite_fruits:
    print("You really like bananas!")
    
if "apple" in favorite_fruits:
    print("You really like apples!")

if "orange" in favorite_fruits:
    print("You really like oranges!")

if "fig" in favorite_fruits:
    print("You really like figs!")

if "peach" in favorite_fruits:
    print("You really like peaches!")

# 8

usernames = ["dato", "admin", "vakho", "gio", "jaden"]

for username in usernames:
    if username != 'admin':
        print(f"hello {username}")
    else:
        print(f"Hello {username}, would you like to see a status report?")

# 9

# hello_admin.py


# 10

current_users = ["dato", "adam", "vakho", "gio", "jaden"]
new_users = ["luka", "adam", "vakho", "gela", "jack"]

current_users_lower = [user.lower() for user in current_users]

for name in new_users:
    if name.lower() in current_users_lower:
        print(f"{name.lower()} is taken by someone else. please change it")
    else:
        print(f"welcome {name.lower()}.")

# 11

numbers = []
i = 1
while 0 < i <= 9:
    numbers.append(i)
    i += 1
print(numbers)

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    elif number > 3:
        print(f"{number}th")