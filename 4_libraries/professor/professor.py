import random

def get_level():
    while True:
        try:
            global level
            level = 0
            level = int(input("pick a level\n"))
            if 0 < level < 4:
                break
        except ValueError:
            continue 

def main():
    get_level()
    score = 0
    i=0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for i in range(3):
            if int(input(f"{x} + {y} = ")) == x + y:
                score += 1
                break
            else:
                print("EEE")
                i+=1
                if i < 3:
                    continue
                else:
                    print(f"{x} + {y} = {x+y}")
    print(score)

def generate_integer(l):
    low = 1*10**(l-1)
    high = (1*10**l) - 1
    if l == 1:
        return random.randint(0, 9)
    else:
        return random.randint(low, high)

if __name__ == "__main__":
    main()