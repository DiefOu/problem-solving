# global vars for if the value of coins change
QUARTER_VALUE = 25
DIME_VALUE = 10
NICKEL_VALUE = 5
PENNY_VAlUE = 1

# Have user enter cost of the item
while True:
    try:
        itemCost = float(input("How much is the item?: "))
        if (len(str(itemCost)) - str(itemCost).index(".") > 3):
            print("Please enter a valid price")
            continue
        break
    except ValueError:
        print("Please enter a number")

# Have user enter how much they payed for it
while True:
    try:
        amountPaid = float(input("How much did you pay for it?: "))
        if (len(str(amountPaid)) - str(amountPaid).index(".") > 3):
            print("Please enter a valid price")
            continue
        break
    except ValueError:
        print("Please enter a number")

# Figure out change
change = amountPaid - itemCost
if change < 0:
    print("You didn't pay enough")
# Figure out the number of individual coins required for each coin type
# Coin types: quarters, dimes, nickels, pennies
elif change == 0:
    print("No change")
else:
    print(str(change) + " is the change.")
    # Make change in terms of only cents for easier calculation
    change *= 100
    # Calculate number of quarters needed
    numQuarters = change // QUARTER_VALUE
    change = change % QUARTER_VALUE
    # Calculate number of dimes needed
    numDimes = change // DIME_VALUE
    change = change % DIME_VALUE
    # Calculate number of nickels needed
    numNickels = change // NICKEL_VALUE
    change = change % NICKEL_VALUE
    # Calculate number of pennies needed
    numPennies = change // PENNY_VAlUE
    change = change % PENNY_VAlUE
    # Tell user the coins recieved as change
    print("In terms of coins, it results to " + str(numQuarters) + " quarters, " + str(numDimes) + " dimes, "
          + str(numNickels) + " nickels, " + str(numPennies) + " pennies, and " + str(change) + " left over.")
