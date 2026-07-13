import random
game = [1, 2, 3]
C_choice = random.choice(game)

print("\n<~you are in number guessing game~>")
your_choice = int(input("1, 2, 3 choose one: "))

print(f"\ncomputer choose: {C_choice}")
print(f"You choose: {your_choice}")

if (C_choice == your_choice):
    print("\nYou win!!")

else:
    print("\nWrong answer you loose")   