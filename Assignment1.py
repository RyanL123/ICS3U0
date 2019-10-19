import datetime
import random
import sys

# initialize coins and portfolio
coins = ["BTC", "ETH", "XRP", "LTC"]

holdings = {
    "BTC": 0.0,
    "ETH": 0.0,
    "XRP": 0.0,
    "LTC": 0.0,
    "CAD": 10000.0
}

conversion_rate = {
    "BTC": 15000.0,
    "ETH": 300.0,
    "XRP": 0.30,
    "LTC": 90.0,
}

# initialize date
time = datetime.datetime.now()
year = int(time.year)
month = int(time.month)
day = int(time.day)
days_past = 0

# displays instructions
def init():
    print("Welcome to CryptoSim, a game where you can lose all your money in crypto without actually losing anything!")
    print("The rules of the game are simple. Buy low, sell high and don't go broke.")
    print("Every day, you'll get a chance to either buy and sell crypto, or simply make no transactions")
    print("To see a list of all commands, type the word command when you're in game")
    print("To start the game, type Y. To exit the program, type N")
    choice = input()
    if choice.capitalize() == "Y":
        return True
    return False


# increase date by 1 every turn
def increment_date():
    global day, month, year, days_past
    day += 1
    days_past += 1
    # checks for months with 31 days
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 9 or month == 11) and day > 31:
        day = 0
        month += 1

    # checks for february and leap years
    if month == 2:
        if year % 4 == 0 and day > 29:
            day = 0
            month += 1
        elif day > 28:
            day = 0
            month += 1

    # check for months with 30 days
    if (month == 4 or month == 6 or month == 10 or month == 12) and day > 30:
        day = 0
        month += 1

    if month > 12:
        month = 0
        year += 1


# buy/sell crypto
def transaction():
    repeat = True

    # repeat until stopped by user
    while repeat:
        option = input("Enter B to buy, S to sell")
        option = option.capitalize()

        if option == "B":
            crypto = input("Please enter the crypto you would like to buy")
            amount = float(input("Please enter the amount you would like to buy in CAD"))
            crypto = crypto.upper()
            confirm = input("1 %s is worth %i CAD, do you want to continue? Y | N" % (crypto, conversion_rate[crypto]))
            if confirm.upper() == 'N':
                print("Canceling")
                return

            # not enough money
            if holdings["CAD"] < amount:
                print("Sorry, you do not have enough money to buy %d %s" % (amount, crypto))
            else:
                # add the crypto to wallet according to conversion rate
                holdings[crypto] += amount/conversion_rate[crypto]
                holdings["CAD"] -= amount
                buy_again = input("Would you like to make another transaction? Enter Y for yes, N for no")
                buy_again = buy_again.capitalize()
                if buy_again == "N":
                    repeat = False

        elif option == "S":
            crypto = input("Please enter the crypto you would like to sell")
            amount = float(input("Please enter the amount you would like to sell in %s" % (crypto.upper())))
            crypto = crypto.upper()
            confirm = input("1 %s is worth %i CAD, do you want to continue? Y | N" % (crypto, conversion_rate[crypto]))
            if confirm.upper() == 'N':
                print("Canceling")
                return
            # not enough crypto
            if holdings[crypto] < amount:
                print("Sorry, you do not have enough %s to sell" % crypto)
            else:
                # add CAD to wallet according to conversion rate
                holdings[crypto] -= amount
                holdings["CAD"] += amount*conversion_rate[crypto]
                buy_again = input("Would you like to make another transaction? Enter Y for yes, N for no")
                if buy_again == "N":
                    repeat = False


# TODO
# Modify prices based on seed
def modify_prices():
    # randomizes the chances of good and bad news
    random.seed(datetime.datetime.now())
    decider = random.randint(1, 1000)


# display the player's portfolio
def check_portfolio():
    for i in holdings:
        print("%s: %.2f" % (i, holdings[i]))


# display the current conversion rate
def check_conversion_rate():
    for i in conversion_rate:
        print("1 %s is worth %.2f CAD" % (i, conversion_rate[i]))


# returns the total asset the player has
def total_asset():
    total = 0
    for i in holdings:
        if i != "CAD":
            total += holdings[i]*conversion_rate[i]
        else:
            total += holdings[i]
    return total


def command():
    print("PORT: Show portfolio")
    print("RATE: Show conversion rates")
    print("END: Move on to next day")
    print("EXIT: Exit program")


if init():
    while total_asset() >= 0:
        print("The date is %d/%d/%d" % (year, month, day))
        increment_date()
        action = input()
        action = action.upper()
        while action != "END":
            if action == "BUY" or action == "SELL":
                transaction()
            elif action == "PORT":
                check_portfolio()
            elif action == "RATE":
                check_conversion_rate()
            elif action == "COMMAND":
                command()
            elif action == "EXIT":
                print("Exiting...")
                sys.exit(0)
            action = input()
            action = action.upper()
    print("You went broke! Game Over!")

else:
    print("Exiting...")