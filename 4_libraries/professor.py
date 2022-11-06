import random

level = 0
while True:
    try:
        level = int(input("pick a level\n"))
        if 0 < level < 4:
            break
    except ValueError:
        continue 

def main():
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for i in range(3):
                if int(input(f"{x} + {y} = ")) == x + y:
                    break
                else:
                    if i < 3:
                        print("EEE")
                        continue
                    else:
                        print(f"{x} + {y} = {x+y}")



def generate_integer(l):
    low = 1*10**(l-1)
    high = 1*10**l
    return random.randint(low, high)




if __name__ == "__main__":
    main()