
year = int(input("Enter the year"))
def Leap_Year():
    if (year % 400 == 0 and year % 100 !=0) or (year % 4 == 0):
        print("Leap year: ", year)

    else:
        print("Not a Leap year: ", year)

Leap_Year()