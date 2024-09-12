def main():
    ask = input("Calculate\n1)[Max Risk]\nor\n2)[Best Selling Conditions]?")
    if ask == "1":
        digit=float(input("What is coin price now?"))
        risk = int(digit)/100
        whentoStop = float(digit)-risk
        print("Max Risk (1%) = ",risk,"\nSell coin to avoid losses when price reaches:",whentoStop)
        riskChange = input("Change default max risk?")
        if riskChange.isdigit():
            prChng = int(riskChange)
            risk = digit*prChng/100
            whentoStop = digit - float(risk)
            print("Max Risk (",prChng,"%)=",risk,"\nSell coin to avoid losses when price reaches:",whentoStop)
    if ask == "2":
        price = float(input("Price of coin when u bought it :"))
        amount = float(input("Amount of coin you have bought : "))
        calcAmount = 0.3*amount
        calcPrice = price*0.7+price
        print("You should sell", calcAmount," of coin\nFor",calcPrice)
main()






