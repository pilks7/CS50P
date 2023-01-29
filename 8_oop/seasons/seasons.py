from datetime import date
import sys


def main():
    try:
        print(nums_to_words(minutes_born(date.fromisoformat(input('Date of birth: ').strip()))))
    except:
        sys.exit('DOB must be of format YYYY-MM-DD')

def minutes_born(dob):
    today = date.today()
    daysborn = today - dob
    return daysborn.days * 60 * 24

def nums_to_words(minutes):
    order_of_magnitude = {
    1: '', 2 : 'thousand', 3:'million', 4: 'billion', 5: 'trillion'
    }

    word_units = {
    '1': 'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine',
    }
    word_teens = {
    '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', 
    }

    word_tens = {
    '1':'ten', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'
    }

    string_mins = f"{minutes:,}"
    clods = string_mins.split(',')
    final = ""
    i = 0
    for n in clods:     
        if len(n) == 3:
            if n[0] != '0':
                final += word_units[n[0]]+' '
                final += 'hundred '
                if n[1] == '1' and n[2] !='0':
                    final += word_teens[n[1]+n[2]]+' '
                    if i < 2:
                        final +=  str(order_of_magnitude[len(clods) - i]+', ')
                        i+=1
                    else:
                        final +=  str(order_of_magnitude[len(clods) - i])
                        i+=1                
                if n[1] != '0' and n[2] !='0':
                    final += word_tens[n[1]]+'-'
                    final += word_units[n[2]]+' '
                    if i < 2:
                        final +=  str(order_of_magnitude[len(clods) - i]+', ')
                        i+=1
                    else:
                        final +=  str(order_of_magnitude[len(clods) - i])
                        i+=1
                    
                elif n[1] == '0' and n[2] != '0':
                    final += word_units[n[2]]+' '
                    if i < 2:
                        final +=  str(order_of_magnitude[len(clods) - i]+', ')
                        i+=1
                    else:
                        final +=  str(order_of_magnitude[len(clods) - i])
                        i+=1
                    
                elif n[1] != '0' and n[2] == '0':
                    final += word_tens[n[1]]+' '
                    if i < 2:
                        final +=  str(order_of_magnitude[len(clods) - i]+', ')
                        i+=1
                    else:
                        final +=  str(order_of_magnitude[len(clods) - i])
                        i+=1
                    
               
            elif n[0] == '0':
                if n[1] == '1':    
                    final += word_teens[n[1]+n[2]]+' '
                    if i < 2:
                        final +=  str(order_of_magnitude[len(clods) - i]+', ')
                        i+=1
                    else:
                        if i < 2:
                            final +=  str(order_of_magnitude[len(clods) - i]+', ')
                            i+=1
                        else:
                            final +=  str(order_of_magnitude[len(clods) - i])
                            i+=1
                    
                else:
                    final += word_tens[n[1]]+'-'+word_units[n[2]]+' '
                    if i < 2:
                        final +=  str(order_of_magnitude[len(clods) - i]+', ')
                        i+=1
                    else:
                        final +=  str(order_of_magnitude[len(clods) - i])
                        i+=1
                    

        elif len(n) == 2:
            if n[1] == '0':
                final += tens_units[n[0]]+' '
            elif n[0] == '1':
                final += word_teens[n[0]+n[1]]+' '
                if i < 2:
                    final +=  str(order_of_magnitude[len(clods) - i]+', ')
                    i+=1
                else:
                    final +=  str(order_of_magnitude[len(clods) - i])
                    i+=1
                
            else:
                final += word_tens[n[0]]+'-'+word_units[n[1]]+' '
                if i < 2:
                    final +=  str(order_of_magnitude[len(clods) - i]+', ')
                    i+=1
                else:
                    final +=  str(order_of_magnitude[len(clods) - i])
                    i+=1  
                           
        elif len(n) == 1:
            final += word_units[n]+' '
            if i < 2:
                final +=  str(order_of_magnitude[len(clods) - i]+', ')
                i+=1
            else:
                final +=  str(order_of_magnitude[len(clods) - i])
                i+=1
            
    return final.capitalize().strip()+' minutes'


if __name__ == "__main__":
    main()

 