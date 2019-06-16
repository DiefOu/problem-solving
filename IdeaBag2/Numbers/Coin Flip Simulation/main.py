import random

# Ask user the number of times the "coins" should be flipped
while True:
    try:
        numCoinsFlip = int(input("How many times do you want the coin to be flipped?: "))
        if numCoinsFlip < 1:
            print("Please enter a natural number")
        break
    except ValueError:
        print("Please enter a whole, positive number of at least 1")

# number of heads and tails var init
heads = 0
tails = 0

# use for loop through the coin flips and record number of heads and tails
for i in range(numCoinsFlip):
    # actually generating either heads or tails
    temp = random.randint(1,2)
    # add 1 to respective counter var
    if temp == 1:
        heads += 1
    else:
        tails += 1

# Output result to user
print("Outcome after {} coins flips: {} heads and {} tails".format(numCoinsFlip, heads, tails))
