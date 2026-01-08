current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# The += operator is shorthand for current_number = current_number + 1
print("\nLet's let the user choose when to quit:\n")
prompt = "\nTell me something, and I will repeat it back to you:\n"
prompt += "\nEnter 'quit' to end the program. \n"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
      print(message)
print("\nLet's use a flag:\n")
prompt = "\nTell me something, and I will repeat it back to you:\n"
prompt += "\nEnter 'quit' to end the program. \n"
active = True
while active:
   message = input(prompt)
   if message == 'quit':
      active = False
   else:
      print(message)
print("\nLet's use a break to exit a loop:\n")
# The break statement directs the flow of your program
# You can use it to control which lines of code are executed and aren't,
# so the program only executes code that you want it to, when you want it to
prompt = "\nPlease enter the name of a city you have visited: \n"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
   city = input(prompt)
   if city == 'quit':
      break
   else:
      print(f"I'd love to go to {city.title()}!")
print("\nLet's use continue in a loop:\n")
current_number = 0
while current_number < 10:
   current_number += 1
   if current_number % 2 == 0:
      continue
# Use continue statement to return to the beginning of the loop,
# based on the result of a conidtional test
print("\nLet's avoid infinite loops:\n")
x = 1
while x <= 5:
   print(x)
   x += 1 #If not this, it becomes infinite
print("\nLet's practice:\n")
print("Pizza toppings:")
pizza = "What toppings do you want on your pizza?"
pizza += "Enter 'quit' when done. "
toppings = []
while toppings != 'quit':
   toppings = input(pizza)
   print(toppings)
print("\nMovie Tickets:\n")
age = input("How old are you? ")
age = int(age)
while age != 'quit':
  if age < 3:
    print("The ticket is free.")
  elif age >= 3:
    print("The ticket costs $10.")
  elif age > 12:
    print("The ticket costs $15.") 
while age == 'quit':
   break
print("\nThree exits:\n")
pizza = "What toppings do you want on your pizza?"
pizza += "Enter 'quit' when done. "
toppings = []
active = True
while active:
   toppings = input(pizza)
   if message == 'quit':
    active = False
   else:
      print(toppings)
print("\nInfinity:\n")
x = 67
while x <= 69:
   print(x)
print("\nLet's use while loop with lists and dictionaries:\n")
print("Let's move items from one list to another:")
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
   current_user = unconfirmed_users.pop()
   print(f"Verifying user: {current_user.title()}")
   confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print("\nLet's remove all instances of specific values from a list:\n")
# remove() only removes one value, to remove all instances of a value:
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
print("\nLet's practice:\n")
print("Sandwiches:")
sandwich_orders = [
    'tuna sandwich', 
    'pastrami sandwich',
    'grilled cheese sandwich',
    'ham sandwich',
    'pastrami sandwich',
    'tomato sandwich',
    'chicken sandwich',
    'pastrami sandwich',
    ]
print(sandwich_orders)
print("The Deli unfortunately ran out of pastrami sandwich.")
while 'pastrami sandwich' in sandwich_orders:
   sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)
finished_sandwiches =[]
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print(f"I made your {making_sandwich}.")
    finished_sandwiches.append(making_sandwich)
print("\nThe following sandwiches have been made:\n")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())


