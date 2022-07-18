## decades.py

# name = input("What's your name\n")
# greeting = "Hello" + " " + name
# print(greeting)

# age = int(input("How old are you?\n"))

# decades = age // 10
# years = age % 10

# print("You are " + str(decades) + " decades old and " + str(years) + " years old")

# temp = 55

# if temp > 80: 
#     print("It's too hot")
#     print("Stay inside!")
# elif temp < 60:
#     print("It's too cold! Stay inside!")
# else: 
#     print("Enjoy the outdoors!")
# import random


## rockPaperScissors.py

# computerChoice = random.choice(['scissors', 'rock', 'paper'])
# userChoice = input("Do you want - rock, paper, or scissors\n")

# if computerChoice == userChoice:
#     print('TIE')
# elif userChoice == 'rock'  and computerChoice == 'scissors':
#     print('WIN')
# elif userChoice == 'paper'  and computerChoice == 'rock':
#     print('WIN')
# elif userChoice == 'scissors'  and computerChoice == 'paper':
#     print('WIN')
# else:
#     print('You lose, computer wins!')


## expenses.py

# expenses = [10.50, 8,5, 15, 20, 5, 3]
# total = sum(expenses)
# # sum = 0

# # for x in expenses:
# #     total = sum + x

# print('You spent $', total, ' on lunch this week.', sep='')

## loan.py

# Get the loan details

# moneyOwed = float(input('How much money do you owe, in dollars?\n')) #50,000
# apr = float(input('What is the annual percentage rate\n')) #3%
# payment = float(input('What will your monthly payment be, in dollars?\n')) #1,000
# months = int(input('How many months do you want to see results for?\n')) #24

# # DIVIDE APR by 100 to make it a percent, then divide by 12 to make monthly
# monthlyRate = apr/100/12


# for i in range(months):
#     #add interest
#     interestPaid = moneyOwed * monthlyRate
#     moneyOwed = moneyOwed + interestPaid

#     if(moneyOwed - payment < 0):
#         print('The last payment is', moneyOwed)
#         print('You payed off the loan in', i+1, 'months')
#         break

#     # Make Payment
#     moneyOwed = moneyOwed - payment

#     # Print the results after this month's payment
#     print('Paid', payment, 'of which', interestPaid, 'was interest', end=' ')
#     print('Now I owe', moneyOwed)

## movieSchedule.py

# from os import cpu_count


# currentMovies = {
#     'The Grinch': '11:00am',
#     'Rudolph': '1:00pm',
#     'Frosty The Snowman': '3:00pm',
#     'Christmas Vacation': '5:00pm'
# }

# print('We are currently showing the following movies:')
# for key in currentMovies:
#     print(key)

# movie = input('What movie would you like the showtime for?\n')

# showtime = currentMovies.get(movie)
# if showtime == None:
#     print("Requested showtime isn't playing")
# else:
#     print(movie, 'is playing at', showtime)

## contacts.py

# contacts = {
#     "number":4,
#     "students":
#     [
#         {"name": "Sarah Holderness", "email":"sarah@example.com"},
#         {"name": "Harry Potter", "email":"harry@example.com"},
#         {"name": "Hermione Granger", "email":"hermione@example.com"},
#         {"name": "Ron Weasley", "email":"ron@example.com"}
#     ]
# }

# for student in contacts["students"]:
#     print(student["email"])

## spacePeople.py

# import requests

# people = requests.get('http://api.open-notify.org/astros.json')
# json = people.json()

# print(json)

# print('The people currently in space are')
# for p in json['people']:
#     print(p['name'])

# weather.py

apiKey = '8e364147eaa300db0ad1448598bf31e9'

