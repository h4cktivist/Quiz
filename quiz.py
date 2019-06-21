from datetime import datetime
lives = 10
name = input ("Enter your name: ")
print ("Hello, " + name)
print ("You are here to solve the quest! Created by school subjects.")
print ("Your goal is answer the questions and to spend less time and save all 5 lives.")
print ("To start the game type 'GO'. Good luck!")
a = input ("Type here: ")
if a == "GO":
	print ("Time is started!")
	st = datetime.now()
	print (" ")
	ans = input ("Informatics: What is brain of computer? ")
	while ans.upper() != "CPU" and lives > 1:
		lives -= 1
		ans = input ("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now()
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Right. Keep going!")
print (" ")
ans = int(input ("Math: 2x + 18 = 84  x = "))
while ans != 33 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Awesome. Keep going!")
print (" ")
ans = int(input ("Math: Square root of 225: "))
while ans != 15 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Good. Keep going!")
print (" ")
ans = int(input ("Geography: How many continents in the world? "))
while ans != 6 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Excellent. Keep going!")
print (" ")
ans = int(input ("How many players in one football team? "))
while ans != 11 and lives > 1:
	lives -= 1
	ans = int(input("PE: Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Right. Keep going!")
print (" ")
ans = int(input ("Geometry: The sum of the inner corners of the triangle is equal to: "))
while ans != 180 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Very good. Keep going!")
print (" ")
ans = int(input ("English: How many letters in English language? "))
while ans != 26 and lives > 1:
	lives -= 1
	ans = int(input("Wrong. Be careful you've only {0} lives. ".format(lives)))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Cool. Keep going!")
print (" ")
ans = input ("History: Name of the first president of USA: ")
while ans.upper() != "GEORGE" and lives > 1:
	lives -= 1
	ans = input("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Perfect. Keep going!")
print (" ")
ans = input ("Literature: Who wited 'Romeo and Juliet'?: ")
while ans.upper() != "SHAKESPEARE" and lives > 1:
	lives -= 1
	ans = input("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Awesome. Keep going!")
print (" ")
ans = input ("Chemistry: Chemical formula of hydrochloric acid: ")
while ans.upper() != "HCL" and lives > 1:
	lives -= 1
	ans = input("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Excellent. Keep going!")
print (" ")
ans = input ("Geography: What state is the city of Sacramento? ")
while ans.upper() != "CALIFORNIA" and lives > 1:
	lives -= 1
	ans = input("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now() - st
	print ("You lose!")
	print ("Time {0}".format(now))
	exit()
print ("Good. Keep going!")
print (" ")
ans = input ("Physics: Who explored the Gravitation Law? ")
while ans.upper() != "NEWTON" and lives > 1:
		lives -= 1
		ans = input ("Wrong. Be careful you've only {0} lives. ".format(lives))
if lives <= 1:
	now = datetime.now() - st
	print ("Unfortunately, you lose! Try again.")
	print ("Time: {0}".format(now))
else:
	now = datetime.now() - st
	print (" ")
	print ("You win! Great job! Your time is {0} and you still have {1} lives".format(now, lives))

# Created by h4cktivist