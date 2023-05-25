def yes_no_checker():
    while True:
        response = input("Please enter 'yes' or 'no': ").lower()

        if response == 'yes':
            print("You entered 'yes'.")
        elif response == 'no':
            print("You entered 'no'.")
        else:
            print("Please enter either 'yes' or 'no'")

yes_no_checker()









