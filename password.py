#[{(project-3)}]
#This programme is based on the cryptsetup password enabling.
#This programme is the coded form of my laptop's system and the number of accounts.
    #print("     [cryptsetup]")
#there are 4 code names- "jammy","hello","world","chocopie"
def password1():
    print("     [cryptsetup]")
    while True:
        p1=int(input("Enter your cryptsetup password: "))
        if(p1 == 9954722871):
            print("     (cryptsetup seccessfully)!")
            break
        else:
            print("     (cryptsetup unseccessfully)!","\n","try again-")
    return p1
password1()
 
print("  ")

Marshad=9954722871
acconts=["Marshad","not listed"]
print("your accounts:",acconts)

def password2():
    print("     [System entry password]")
    a=str(input("Do you wnat to access 'Marshad' account?(yes/no) "))
    if(a.lower() != "yes"):
        print("Then feel free to create another account if you like to...")
        quit()
    else:
        print("     ","\n","Enter your password below for the accesstion-")

    while True:
        p2=int(input("Enter your account's system password: "))
        if(p2 == Marshad):
            print("     ","\n","     {Welcome Marshad}!")
            break
        else:
            print("wrong input(password)","\n","try again-")
    return p2
password2()

#Now here i have used the def because to show that it is the third part of the programme.
def verify():
    print("     ")
    print("verify it is you-")
    print("codenames must be different")
# 4 different code names are written at the top.
# user of the account and including the computer device are very importent as the user is top secret agent!
    c=str(input("Enter your code name: "))
    d=str(input("Enter your code name: "))
    e=str(input("Enter your code name: "))
    f=str(input("Enter your code name: "))

    if(c == "jammy" and  c == "j"):
        print("verification complete")
        if(d != "hello"):
            print("wrong password,try again")
            if(e != "world"):
                print("wrong password,try again")
                if(f != "chocopie"):
                    print("wrong password,try again") 
                    quit()
                else:
                    print("verification complete")
            else:
                print("verification complete")
        else:
            print("verification complete")
    else:
        print("wrong answer, try agian") 
        #print("verification complete")
        #quit()
verify()
print("     ")
print("welcome boss! The system has been completely accessed by you.")
print("your face recognition is also perfect.")

#second verification
def verify34():
    v=int(1)
    while(v <= 3): #There is no need to mention the <True> because while loop depends upon when bool itself.
        v2=str(input("Enter your secret code: "))
        if(v2 == "hello_world"):
            print("Final verification completed")
            break
        else:
            print("Wrong code, try again")
        v += 1
    return v2
verify34()
#print("Your current directory is home directory")
#-end-