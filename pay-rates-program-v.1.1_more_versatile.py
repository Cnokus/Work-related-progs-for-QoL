try :
    salary = int(input("How much did you get this month?\n"))
    hyperMode = 0
except:
    hyperMode = 1
if hyperMode == 1:
    print("Shush")
#Hypermode enabled --- jump to another mode with less words and more action!
else:

    day = int(input("How many weeks did you work in the daytime?\n"))
    night = int(input("How many weeks did you work in the night time?\n"))

    optQ = input("Enable the optional questions related to the working hours? \n >'Yes'\n >'No'")
    if optQ == "Yes":
        dHours = float(input("How many hours do you work per day?"))
        wDays = int(input("How many days do you work per week?"))
        nHours = float(input("How many hours do you work per night?"))
        wNights = int(input("How many nights do you work per week?"))
        list = [dHours, wDays, nHours, wNights]
        def hours():
            hourcalc = list[0]*list[1]*day + list[2]*list[3]*night
            return hourcalc
    elif optQ == "No":
        def hours():
            hourcalc = 5*7*day + 40*night
            return hourcalc

    invhours = hours()

    rate = float(salary) / invhours
    print("So your hourly rate nowadays is", rate, "\n and your total basic hours are", invhours)

    xtraweek = int(input("\nHow many extra shifts did you have during week days?\n"))
    xtraweekends = int(input("\nHow many extra shifts did you have during weekends?\n"))

    if optQ == "Yes":
        xtraSalary = list[0]*float(rate)*(xtraweek*1.5 + xtraweekends*2)
        # return xtraSalary cant use outside function
    else:
        xtraSalary = 7*float(rate)*(xtraweek*1.5 + xtraweekends*2)
        # return xtraSalary
    print("The estimated bonus would be:\n",xtraSalary)

    response = input("\nAnything else? Want me to 'check' your extras?")
    if response == "check" or "Yes":
        diffBonus = int(input("How much bonus did you get?"))
        extraBonus = float(diffBonus) - xtraSalary
        print("So you got this much extra:", extraBonus)
        print("Thank you for using the program")
        exit()
    else:
        print("Exiting")
        exit()
