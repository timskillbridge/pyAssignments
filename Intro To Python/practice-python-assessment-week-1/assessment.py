

def exact_change(item_cost, money_paid):

    answer = []
    if item_cost > money_paid:
        return "You can't afford this item."
    if item_cost == money_paid:
        return "Your total is 0.00."
    runningChange = int((money_paid*100)-(item_cost*100))
    
    moneyList = [
        [10000,"One Hundred Dollar Bill","One Hundred Dollar Bills"],
        [5000,"Fifty Dollar Bill","Fifty Dollar Bills"],
        [2000,"Twenty Dollar Bill","Twenty Dollar Bills"],
        [1000,"Ten Dollar Bill","Ten Dollar Bills"],
        [500,"Five Dollar Bill","Five Dollar Bills"],
        [200,"Two Dollar Bill","Two Dollar Bills"],
        [100,"One Dollar Bill","One Dollar Bills"],
        [25,"Quarter","Quarters"],
        [10,"Dime","Dimes"],
        [5,"Nickle","Nickles"],
        [1,"Penny","Pennies"]
    ]

    for x,y in enumerate(moneyList):
        ammountCheck = int(runningChange/y[0])
        if ammountCheck >=1:
            if ammountCheck >=2:
                if len(answer) == 0:
                    answer.append(f" {ammountCheck} {y[2]}")
                else:
                    answer.append(f", {ammountCheck} {y[2]}")
            else:
                if len(answer) == 0:
                    answer.append(f" 1 {y[1]}")
                else:
                    answer.append(f", 1 {y[1]}")

            takingAmmount = ammountCheck*y[0]
            runningChange -= takingAmmount


            # print(f"taking {runningChange} and subtracting {takingAmmount}")
    if len(answer) >2:
        answer[-1] = f", and{answer[-1][1::]}"
    elif len(answer) ==2:
        answer[-1] = f" and{answer[-1][1::]}"
    else:
        answer[-1] = f" {answer[-1][1::]}"
    answer.append(".")
    answer.insert(0,f"Your total is {(money_paid-item_cost):.2f}:")
    return "".join(answer)

#done, what a pain in the ass...testing sucks