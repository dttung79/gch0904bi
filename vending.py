PEPSI = 1
COFFEE = 2
LEMONADE = 3
PEPSI_PRICE = 10000
COFFEE_PRICE = 20000
LEMONADE_PRICE = 15000
ADMIN_CODE = 1234
running = True
while running:
    print('Automatic Vending Machine')
    print('1. Pepsi')
    print('2. Coffee')
    print('3. Lemonade')
    choice = int(input('Enter your choice: '))
    if choice == ADMIN_CODE:
        print('Shutdown ...')
        break
    if choice != PEPSI and choice != COFFEE and choice != LEMONADE:
        print('Invalid choice')
    else:
        payment = PEPSI_PRICE if choice == PEPSI else COFFEE_PRICE if choice == COFFEE else LEMONADE_PRICE
        print('Price is', payment)
        invalid_payment = True 
        while invalid_payment:
            amount = int(input('Enter payment amount: '))
            invalid_payment = amount < payment
            print('Invalid payment') if invalid_payment else print('Change is', amount - payment)