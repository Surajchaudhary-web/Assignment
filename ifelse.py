user_name = ["officialanilnepali@gmail.com","brocode@gmail.com"]
password = ["firstgeneration","secondgeneration"]

user_input = input(f"Enter the user name:")
if user_input in user_name:
    print("username exist")
else:
    print("user name not found")