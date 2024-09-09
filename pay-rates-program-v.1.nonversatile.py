salary = input("How much did you get this month?\n")
day = int(input("How many weeks did you work in the daytime?\n"))
night = int(input("How many weeks did you work in the night time?\n"))
hours = 5*7*day + 40*night

rate = float(salary) / hours
print("So your hourly rate nowadays is", rate, "\n and your total basic hours are", hours)

xtraweek = input("\nHow many extra shifts did you have during week days?\n")
xtraweekends = input("\nHow many extra shifts did you have during weekends?\n")

xtraSalary = 7*float(rate)*(int(xtraweek)*1.5 + int(xtraweekends)*2)
print("The estimated bonus would be:\n",xtraSalary)

response = input("\nAnything else? Want me to 'check' your extras?")
if response == "check":
    diffBonus = int(input("How much bonus did you get?"))
    extraBonus = float(diffBonus) - xtraSalary
    print("So you got this much extra:", extraBonus)
    print("Thank you for using the program")
else:
    print("Exiting")