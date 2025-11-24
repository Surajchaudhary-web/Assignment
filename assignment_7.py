# # Loop
# # continuous iteration, a block executing multiple times

# # while loop: if the condition is true, then the block of code inside while loop is executed
# # after the execution of all the statements inside while loop, the condition is checked again
# # if the condition is still true, the block of code is executed again

# # syntax:
# # while contition:
# #    print("Statement")

# a = 0
# b = 3

# # while a < b:
# #    print("Inside while loop")
# #    print("A is smaller")
   
# #    a += 1


# # break : loop ends and read next statement that are present after loop
# while a < b:
#    if a == 2:
#       break
#    print("Inside while loop")
#    print("A is smaller")
#    a += 1

# print("After break")

# # continue : skips the current iteration and jumps to the next iteration
# while a < b:
#    a += 1
#    if a == 2:
#       continue
#    print(a)



#calulator using if-else
# get two numbers from user
# get the operator from user(+,-,*,/)
# perform the operation based on the operator
# ask if the user want to continue the calculation, if yes repeat the process, else exit
# while True:
#  num1 = float(input("Enter the first number: "))
#  num2 = float(input("Enter the second number: "))
#  operator = input("Enter the operator: ")
#  if operator == "+":
#   print("The sum is: ", num1 + num2)
#  elif operator == "-":
#   print("The difference is: ", num1 - num2)
#  elif operator == "*":
#   print("The multiply is: ", num1 * num2)
#  elif operator == "/":
#   print("The division is: ", num1 / num2)
#  repeat = input("Do you want to continue the calculation? ")
#  if repeat != "yes":
#   print("Thankyou for using this calculator")
#   break



# day 6 assignment modification 
# implement while loop in rock paper scissor game
# while True:
#    player1 = input("Enter your choise: ")
#    player2 = input("Enter your choise: ")
#    if player1 == player2:
#       print("It's a tie! ")
#    elif (player1 == "rock" and player2 == "scissor") or (player1 == "paper" and player2 == "rock") or (player1 == "scissor" and player2 == "paper"):
#      print("Player 1 wins!")
#    else:
#      print("player2 wins!")


# implement while loop in
# get two numbers form user
# while True:
#    user1 = float(input("Enter the first number: "))
#    user2 = float(input("Enter the second number: "))
#    if user1>user2:
#       print("The greatest number is :" , user1)
#    elif user1<user2:
#       print("The greatest  number is: ", user2)

# get the greater number from the list
# list = [43, 65, 3, 54, 23,100, 3]
# greatest = list[0]
# i = 0
# while i<len(list):
#    if list[i] > greatest:
#         greatest = list[i]
#    i += 1

# print("The greatest number in the list is:", greatest)

# for loop