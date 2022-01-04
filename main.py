import random

user_name = input("Hi, what's your name?\n  ")

print("\nHow was your day today, " + str(user_name) + "? ")
day = input("Choose one: good, bad, ok\n  ")

if day == "good":
  input("\nThat's awesome! What did you do today?\n  ")
elif day == "bad":
  input("\nI'm sorry your day wasn't that good today, what happened?\n  ")
elif day == "ok":
  input("\nThat's nice, atleast nothing bad happened. Anyways, What did you do today?\n  ")
else:
  day = input("You can only choose good, bad, or ok\n  ")

print("\nWell, here's a joke that will make you happier: What do you call a fake pasta? Impasta!")
joke = input("Do you want to hear some more of my hilarious jokes?\nType yes or no\n  ")


jokes_list = [
  "Why do bees have sticky hair? Because they use honeycombs!", 
  "Why don't eggs tell jokes...because they would crack each other up!", 
  "What did the fish say when he swam into a wall? Dam!", 
  "Why couldn't the pony sing a lullybuy? She was a little hoarse!", 
  "What did the shark say after eating the clownfish? This tastes a little funny!"
]


if joke == "yes":
  (print(random.choice(jokes_list)))
elif joke == "no":
  print("No worries, " + user_name + " sometimes I myself cringe at what comes out of my own mouth")
else:
  input("\n Type yes or no\n  ")

input("\nSo what's your favorite food? I really like taquitos, Butter Chicken, loaded omletes....and soo much, I could go on for hours!\n  ")

print("\nOoh that sounds delicious " + user_name + "! I'm craving some too!")
input("Well since we're on the topic of food, what food do you dislike the most?\n")