def calculateDaysBetweenDates(begin, end):
    begin = begin.split("-")
    end = end.split("-")
    begin = [int(x) for x in begin]
    end = [int(x) for x in end]
    return (end[2] - begin[2]) * 365 + (end[1] - begin[1]) * 30 + (end[0] - begin[0])
def login(username, password):
    if username == "admin" and password == "password":
        return True
    else:
        return False
def main():
    print("Welcome to the Copilot System")
    print("Please login")
    username = input("Username: ")
    password = input("Password: ")
    if login(username, password):
        print("Login Successful")
        print("Please enter the dates you wish to calculate the number of days between")
        begin = input("Begin Date: ")
        end = input("End Date: ")
        print("The number of days between", begin, "and", end, "is", calculateDaysBetweenDates(begin, end))
    else:
        print("Login Failed")
if __name__ == "__main__":
    main()
#oh my god this github copilot is so cool