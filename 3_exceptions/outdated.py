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
        # try:
            #user_in[0] = [months.get(month) for month in months if user_in[0] == month]
        print(user_in[0])
        for month in months:
            if user_in[0] == month:
                user_in[0] = months.get(month)
                print(user_in[0])              
        if 1000 < int(user_in[2]) < 2999:
            break

    except:
        print("Try formatting your date: MM/DD/YYYY, or like 'September 8, 1988'")
        print(user_in[0])
        print(user_in)
        continue