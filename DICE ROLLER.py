import random

dice_art = {
    
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
while True:
    dice = []
    total = 0
    num = int(input("How many Dice You Want: "))

    for die in range(num):
        dice.append(random.randint(1, 6))


    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        total += die
    print(f"total: {total}")

    cont=input("dou you want to continue \n 1.YES \n2. NO \n")
    while cont.lower() not in ("1","2"):
        cont=input("Please Enter the Correct Input \n 1.YES \n 2.NO\n")
    if cont == "2":
        print()
        print("!!!Thank You!!!")
        break
    