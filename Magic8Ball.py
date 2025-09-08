#Magic8Ball.py
#Name: Francisco Pineda Lopez
#Date: 09/07/2025
#Assignment: Lab #2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.

answers = ["As I see it, yes.", "Ask again later", "Yes", "No", "It is decidedly so", "Concentrate and ask again", "Outlook Good", "Without a doubt."]

  #Answer question randomly with one of the options from your earlier list.
length = len(answers)
r = random.random() * length

r = int(r)

print(r)
response = answers[r]
print(response)

if __name__ == '__main__':
  main()
