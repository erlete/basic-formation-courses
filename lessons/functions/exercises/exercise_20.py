def can_buy(cost, balance=0):
    if cost > balance:
        return bool(0)
    else:
        return bool(1)
