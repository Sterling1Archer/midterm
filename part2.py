import time

if __name__ == '__main__':
    #Obtain the DOB of the User
    year = int(input("Enter your year of birth: "))
    month = int(input("Enter your month of birth: "))
    day = int(input("Enter your day of birth: "))
    t = (year, month, day,0,0,0,0,0,0)
    dob_seconds = time.mktime(t)
    #Obtain the current date
    current_seconds = time.time()
    #Substract curent date with DOB and convert to seconds
    seconds_alive = current_seconds - dob_seconds
    print("You've been alive for",seconds_alive,"seconds.")
    
