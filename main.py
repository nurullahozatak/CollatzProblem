#Collatz Problem
#even number / 2 and odd number*3+1


correction = True
while correction:
    while correction:
        def query():
            number = int(input("Hello please pick a positive and integer number to verify Collatz Problem's : \n"))
            while correction:

                if (number % 2 == 0 and number != 1):
                    number = number / 2
                    print(int(number))
                elif (number % 2 == 1 and number != 1):
                    number = (number * 3) + 1
                    print(int(number))
                else:
                    print('The number you have been picked is proper with Collatz Problem')
                    break

        query()
        print("Do you want to calculate another number ?")
        answer = input("Answer (y/n)")
        if answer == "n":
            correction = False
        elif answer == "y":
            query()

print("\nIs this problem really imposible ?")
