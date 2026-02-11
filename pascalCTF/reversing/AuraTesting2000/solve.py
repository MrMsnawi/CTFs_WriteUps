import random
import os

# Original words used for the secret phrase
words = ["tungtung", "trallalero", "filippo boschi", "zaza", "lakaka", "gubbio", "cucinato"]

# Challenge generation logic
phrase = " ".join(random.sample(words, k=random.randint(3, 5)))
steps = random.randint(2, 5)
flag = os.getenv("FLAG", "pascalCTF{REDACTED}")

def encoder(phrase, steps):
    encoded_phrase = ""
    for i in range(0, len(phrase)):
        if phrase[i] == " ":
            encoded_phrase += phrase[i]
        elif i % steps == 0:
            encoded_phrase += str(ord(phrase[i]))
        else:
            encoded_phrase += phrase[i]
    return encoded_phrase

def questions(name):
    gained_aura = 0
    questions_list = [
        "Do you believe in the power of aura? (yes/no)",
        "Do you a JerkMate account? (yes/no)",
        "Are you willing to embrace your inner alpha? (yes/no)",
        "Do you really like SHYNE from Travis Scott? (yes/no)",
    ]
    # Aura values: (Yes result, No result)
    aura_values = [(150, -50), (-1000, 50), (450, -80), (-100, 50)]
    
    for i in range(len(questions_list)):
        print(f"{name}, {questions_list[i]}")
        answer = input("> ").strip().lower()
        if answer == "yes":
            gained_aura += aura_values[i][0]
        elif answer == "no":
            gained_aura += aura_values[i][1]
    return gained_aura

def aura_test(name):
    print(f"{name}, you have reached the final AuraTest!")
    # The encoded phrase is displayed here
    print("Decode this secret phrase:", encoder(phrase, steps))
    guess = input("Type the decoded phrase:\n> ")
    if guess == phrase:
        print(f"Congratulations {name}!\n{flag}")
        exit()
    else:
        print("You failed the AuraTest.")

# Interaction Loop
print("Welcome to the AuraTester2000!")
name = input("Name?\n> ")
aura = 0

while True:
    print("\n1. Answer questions\n2. Check aura\n3. Final AuraTest\n4. Exit")
    choice = input("> ")
    if choice == "1":
        aura += questions(name)
    elif choice == "2":
        print(f"Your current aura is {aura}.")
    elif choice == "3":
        # Threshold for the final test is 500 points
        if aura < 500:
            print("You need more aura to even try the final AuraTest.")
        else:
            aura_test(name)
    elif choice == "4":
        exit()
