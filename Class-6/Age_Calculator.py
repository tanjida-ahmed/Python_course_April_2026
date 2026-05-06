day = int(input("enter a day"))
        month = int(input("Enter a month"))
        year = int(input("Enter a year"))
        current_month=int(input("Enter current month: "))
        current_year=int(input("Enter current year: "))
        date=int(input("Enter today's date: "))
        if year > current_year:
            print("Invalid year")
        else:
            primary_age = current_year - year
        if month >current_month :
                  print("Your age is", primary_age)
        elif month == current_month and day >= date:
            print("Your age is", primary_age)
        elif current_month < month or (month == current_month and day < day):
            final_age = primary_age - 1
            print("Your age is", final_age)
