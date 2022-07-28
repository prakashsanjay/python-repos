price_house= 1000000
good_credit= True
bad_credit= False

if good_credit:
    down_payment = 0.1 * price_house
    
else:
    down_payment = 0.2 * price_house

print (f"Down Payment ${down_payment}")

# suppose price of a house is $1M if you have good credit you need to give 10% 
# down payment else you need to give 20% down payment



