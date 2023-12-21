def non_constructible_change(coins=list):
    coins.sort()
    potential_change = 0
    for coin in coins:
        if coin > potential_change + 1:
            return potential_change + 1
        potential_change += coin
    return potential_change + 1


if __name__ == '__main__':
    coins = [5, 7, 1, 1, 2, 3, 22]
    min_amnt_of_change_that_cannot_be_created = non_constructible_change(coins)
    print(min_amnt_of_change_that_cannot_be_created)
