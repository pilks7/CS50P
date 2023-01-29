import re

months = {
    "january": "1",
    "february": "2",
    "march": "3",
    "april": "4",
    "may": "5",
    "june": "6",
    "july": "7",
    "august": "8",
    "september": "9",
    "october": "10",
    "november": "11",
    "december": "12"
}


while True:
    try:
        user_in = re.split("/|, | ", input("enter any date:\n").lower())  
        for month in months:
            if user_in[0] == month:
                user_in[0] = months.get(month, user_in[1]) #replace (written) month with corresponding numerical value for month in user_in, else if month is numerical, keep numerical value
        user_in = [eval(i) for i in user_in]  #turns numerical strings into integers
        assert isinstance(user_in[2], int) and isinstance(user_in[1], int) and user_in[1] < 32 and user_in[0] < 13

        myorder = [2, 0, 1]
        user_in = [user_in[i] for i in myorder]

        if 1000 < int(user_in[0]) < 2999:
            break 

    except:
        print("Try formatting your date: MM/DD/YYYY, or like 'September 8, 1988'")
        continue


print(f"{user_in[0]}-{user_in[1]:02}-{user_in[2]:02}")




    #     while True:
    # # try:
    # #     user_in = re.split("/|, | ", input("enter any date:\n").lower())
    # try:
    #     user_in[0] = [months.get(month) for month in months if user_in[0] == month]
    #     print(user_in[0])
    #     for month in months:
    #         if user_in[0] == month:
    #             user_in[0] = months.get(month)
    #             print(user_in[0])              
    #     if 1000 < int(user_in[2]) < 2999:
    #         break

    # except:
    #     print("Try formatting your date: MM/DD/YYYY, or like 'September 8, 1988'")
    #     print(user_in[0])
    #     print(user_in)
    #     continue