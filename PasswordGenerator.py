import random
num_password = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
characters_password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

all_choices = num_password + characters_password

length = int(input("How many characters do you want in your password: "))
C_choice = ""
for i in range(length):
    C_choice += str(random.choice(all_choices))

print(f"This is your password {C_choice}")    