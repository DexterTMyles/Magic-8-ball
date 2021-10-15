import random

name = input("What is your Name?: ")
questions = "Will I be Rich?"
answer = ''
random_number = random.randint(1,9)

if name == name and random_number == 1:
  answer = "Yes - definitely"
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

print(f"{name} asks: {questions}")
print(f"Magic 8-Ball's answer:  {answer}")