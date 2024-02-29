print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
comb = name1 + name2
lower = comb.lower()
t = lower.count('t')
r = lower.count('r')
u = lower.count('u')
e = lower.count('e')
first = t + r + u + e 
l = lower.count('l')
o = lower.count('o')
v = lower.count('v')
e = lower.count('e')
sec = l + o + v + e
res = int(str(first) + str(sec))
if res < 10 or res > 90:
  print(f'Your score is {res}, you go together like coke and mentos.')
elif res >= 40 and res <= 50:
  print(f"Your score is {res}, you are alright together.")
else:
  print(f"Your score is {res}.")