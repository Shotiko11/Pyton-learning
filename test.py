def main ():
    number = get_input()
    print(f"your input is {number}")


def get_input():
    while True:
        try:
            number = int(input("number: "))
        except ValueError:
            print("it is not number")
        else:
            break
        
    return number
    
main()