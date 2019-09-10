#This problem was asked by Google.
#Find the coins required to make n pounds and pence.
#You can use standard British denominations.
#For example, given n = 0.16, return 0.10p, 0.05p, and 0.01p.

def return_change(n, coins = [0.01,0.05,0.10,0.25,0.50,1.00]):
    flag = None
    for c in coins:
        if c == n:
            flag = c
            return [flag]
        
        if c < n:
            flag = c
    balance = round(n - flag,2)
    return [flag] + [return_change(balance)]

change = return_change(0.16)

def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item

print (list(flatten(change)))