import datetime, random

# initialize coins and portfolio
coins = ["BTC", "ETH", "XRP", "LTC"]

holdings = {
    "BTC": 0.0,
    "ETH": 0.0,
    "XRP": 0.0,
    "LTC": 0.0,
    "CAD": 0.0
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


def init():
    print("Welcome to CryptoSim, a game where you can lose all your money in crypto without actually losing anything!")
    print("The rules of the game are simple. Buy low, sell high and don't go broke.")
    print("Every day, you'll get a chance to either buy and sell crypto, or simply make no transactions")
    print("To start the game, please type Y. To exit the program, please type N")


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


def transaction():
    repeat = True

    # repeat until stopped by user
    while repeat:
        option = input("Enter B to buy, S to sell")

        if option == "B":
            crypto = input("Please enter the crypto you would like to buy followed by the amount in CAD")
            amount = float(input())
            crypto.capitalize()

            # not enough money
            if holdings["CAD"] < amount:
                print("Sorry, you do not have enough money to buy %d %s" %(amount, crypto))
            else:
                # add the crypto to wallet according to conversion rate
                holdings[crypto] += amount/conversion_rate[crypto]
                holdings["CAD"] -= amount
                buy_again = input("Would you like to make another transaction? Enter Y for yes, N for no")
                if buy_again == "N":
                    repeat = False

        elif option == "S":
            crypto = input("Please enter the crypto you would like to sell followed by the amount")
            amount = float(input())
            crypto.capitalize()

            # not enough crypto
            if holdings[crypto] < amount:
                print("Sorry, you do not have enough %s to sell" % (crypto))
            else:
                # add CAD to wallet according to conversion rate
                holdings[crypto] -= amount
                holdings["CAD"] += amount*conversion_rate[crypto]
                buy_again = input("Would you like to make another transaction? Enter Y for yes, N for no")
                if buy_again == "N":
                    repeat = False

def modify_prices():
    # randomizes the chances of good and bad news
    random.seed(datetime.datetime.now())
    decider = random.randint(1, 1000)

def check_portfolio():
    for i in holdings:
        print("%s: %.2f" %(i, holdings[i]))

def check_conversion_rate():
    for i in conversion_rate:
        print("1 %s is worth %.2f CAD" %(i, conversion_rate[i]))
