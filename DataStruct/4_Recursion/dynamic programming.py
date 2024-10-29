# 找零问题
# num_coins = min(1 + num_coins(original_amount - 1),
#                 1 + num_coins(original_amount - 5),
#                 1 + num_coins(original_amount - 10),
#                 1 + num_coins(original_amount - 25))

def recMC(coins_value_list, change):
    min_coins = change
    if change in coins_value_list:
        return 1
    else:
        for i in [c for c in coins_value_list if c <= change]:
            num_coins = 1 + recMC(coins_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


# 添加查询表(记忆化)
def recDC(coins_value_list, change, known_results):
    min_coins = change
    if change in coins_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coins_value_list if c <= change]:
            num_coins = 1 + recDC(coins_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


# 动态规划解决找零问题(非递归)
def dpMakeChange(coins_value_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coins_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
        min_coins[cents] = coin_count
    return min_coins[change]


# 修改可回溯找零方案
def dpMakeChange2(coins_value_list, change, min_coins, coins_used):
    for cents in range(change+1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coins_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]

def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


if __name__ == '__main__':
    test1 = recMC([1, 5, 10, 25], 63)
    print(test1)
    test2 = recDC([1, 5, 10, 25], 63, [0]*64)
    print(test2)
    c1 = [1, 5, 10, 21, 25]
    coins_used = [0]*64
    coins_count = [0]*64
    print(dpMakeChange2(c1, 63, coins_count, coins_used))
    print_coins(coins_used, 63)
    print_coins(coins_used, 52)
    print(coins_used)