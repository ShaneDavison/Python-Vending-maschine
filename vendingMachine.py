
def give_change(amount):
    coins = [100, 200, 20, 50, 10, 5]
    change = []

    for coin in sorted(coins, reverse=True):
        while coin <= amount:
            amount -= coin
            change.append(coin)
            if amount >= 3:
                change.append(5)

    return 'You are owed ' + str(change.count(200)) + 'x 200 piece coins and ' + str(change.count(100)) + 'x 100 piece coins and ' + str(change.count(50)) + 'x 50 piece coins and ' + str(change.count(20)) + 'x 20 piece coins and '  + str(change.count(10)) + 'x 10 piece coins and '  + str(change.count(5)) + 'x 5 piece coins and ' + str(change.count(2)) + 'x 2 piece coins and ' + str(change.count(1)) + 'x 1 piece coins'

print give_change(103)