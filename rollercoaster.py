print("Welcome to the rollercoaster!")
bill = 0
height = int(input("Please enter your height in cm: ")) 
if height >= 120: 
    print("You're tall enough to ride!")
    age = int(input("Please enter your age: "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Midlife Crisis tickets are free! Enjoy your ride.")
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Do you want a photo taken? Y/N ").strip().upper()
    if wants_photo == 'Y':
        bill += 3
    print(f"Your final bill is now ${bill}. Enjoy your ride!")
else:
    print("Sorry, you have to be taller to ride.")