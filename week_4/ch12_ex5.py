def cost_phone_call(call_duration):
    """
    computes the cost of a phone call
    call_duration: length of phone call in minutes
    return: total cost of phone call after all fees applied
    """
    print('line 7 call_duration: ', call_duration)
    # base cost of call
    cost = 0.35 ; print('line 9, cost: ', cost)

    # compute cost of call in first ten minutes
    cost = cost + min(call_duration, 10.0) * 0.50 ; print('line 12, cost: ', cost)
    remaining_duration = max(call_duration - 10.0, 0.0)

    # compute cost of call after first ten minutes
    # (only counts full minutes)   # changed / to //
    cost = cost + remaining_duration // 1 * 0.25 ; print('line 17, cost: ', cost)

    # discount from plan deducts 10% from total cost
    cost = cost * 0.9   ; print('line 20, cost: ', cost)

    return cost


# should be 5.04 (expected), this number is NOT computed by using the code above (again, we do not trust the code, hence testing it)
# we worked out this number by reviewing billing policy from the telecompany
print(cost_phone_call(11.15))
