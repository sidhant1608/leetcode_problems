def compound_interest(principle, rate, time):
 
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    ci =  principle + round(Amount - principle, 2)

    return ci
 
# Driver Code
compound_interest(1, 4, 3)

