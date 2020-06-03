import sys
import pdb
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
	print("To exit this game type 'exit'")
	pdb.set_trace()
	num1 = int(choice(random2))
	num2 = int(choice(random1))
	answer = input("What is {} times {}? ".format(num1, num2))

	# exit
	if answer == "exit":
		print("Now exiting game!")
		sys.exit()

		# determine if number is correct
		# test = choice(random2) * choice(random1)
		# print(test)
		# print(choice(random2))
		# print(choice(random1))

		#print(answer)
		#print(num1)
		#print(num2)

		# determine if number is correct

	elif int(answer) == num1 * num2:
		print("Correct!")
	else:
		print("Wrong!")