import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^([0-9]+):?([0-9]*) ([A-Z])M to ([0-9]+):?([0-9]*) ([A-Z])M$", s): # a3, b3 capture 'A' for AM and 'P' for PM. Don't ask why.
        a1, a2, a3, b1, b2, b3 = match.groups()
        if a2 and b2:
            if int(a2) > 59 or int(b2) > 59:
                raise ValueError('Incorrect time format: hours cannot exceed 12, minutes cannot exceed :59')
        if int(a1.lstrip('0')) > 12 or int(b1.lstrip('0')) > 12:
                raise ValueError('DEBUG 1: Incorrect time format: hours cannot exceed 12, minutes cannot exceed :59')

        #convert to 24h format
        if a1 == '12' and a3 == 'A':            #convert special case 12am to 00
            a1 = '00'       
        if a3 == 'P' and int(a1) < 12:               #PM and == 12 remains unchanged
            a1 = str(int(a1) + 12)

        if b1 == '12' and b3 == 'A':
            b1 = '00'
        if b3 == 'P' and int(b1) < 12:
            b1 = str(int(b1) + 12)
        #add leading zero to single digit hour
        if len(a1) == 1:
            a1 = f"0{a1}"
        if len(b1) == 1:
            b1 = f"0{b1}"
        #check if a2 and b2 are empty. if so replace empty string with ":00"
        if not a2:
            a2 = "00"
        if not b2:
            b2 = "00"
    else:
        raise ValueError('DEBUG2: Incorrect format. Must be real times (colon spearated if using minutes) followed by AM or PM')
    return f"{a1}:{a2} to {b1}:{b2}"


if __name__ == "__main__":
    main()
