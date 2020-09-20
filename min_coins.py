"""
This program finds the minimum number of coins to be provided
to the user as blance. The returns are in coins and not in notes.
"""

eur_coins = [1, 2, 5, 10, 20, 50, 100, 200]


def get_min_coins(amount):
    """
    The minimum coins is found using dynamic programming.
    The argument passed to this function is the balance to be given.
    This method creates a matrix and populates the matrix index with the
    euro coins (see the global list). We make the matrix as large as amount.
    If the index of first loop is same as coins in euro_coins then we set
    the matrix's index as 1. Else pick each coins from euro_coins and
    then check for the min(matrix[i - coin], min_coins).
    """
    matrix = [0] * (amount + 1)

    for i in range(1, amount + 1):
        if i in eur_coins:
            matrix[i] = 1
            continue

        min_coins = float("inf")
        for coin in eur_coins:
            if i - coin >= 0:
                min_coins = min(matrix[i - coin], min_coins)
            else:
                break

        matrix[i] = min_coins + 1

    if matrix[-1] == float("inf"):
        return -1

    return matrix[-1]


def get_exact_change(balance: int, min_coins=-1):
    """
    This method gives the coins to be delivered to user.
    The return is a dict with key as coin and value as number of coins.
    So coffee machine has to give 90 cents then the return would be:
    {50 : 1, 20 : 2}. Meaning one coin of 50 and 2 coins of 20.
    """
    if min_coins < 0:
        return {}

    if balance in eur_coins:
        return {balance: 1}

    coins_deliver = {}

    while balance >= eur_coins[-1]:
        prev_coin = eur_coins[-1]
        coins_deliver[prev_coin] = coins_deliver.get(prev_coin, 0) + 1
        balance -= eur_coins[-1]

    while balance > 0:
        for index, coin in enumerate(eur_coins):
            if balance < coin:
                # take the previous coin
                prev_coin = eur_coins[index - 1]
                coins_deliver[prev_coin] = coins_deliver.get(prev_coin, 0) + 1
                balance -= eur_coins[index - 1]
                break

    return coins_deliver


def return_coins(coffee_price, eur_inserted):
    """
    Return the minimum exact change to the user
    The coffee price and eur_inserted are the arguments
    which are converted to coins by multiplying with 100.
    """
    # convert the euros to coins
    coffee_price *= 100
    eur_inserted *= 100
    balance = int(eur_inserted) - int(coffee_price)

    if balance < 0:
        return {}

    coins = get_min_coins(balance)

    exact_change = get_exact_change(balance, coins)
    return exact_change


if __name__ == "__main__":
    return_coins(1.2, 7)
