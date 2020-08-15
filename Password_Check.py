# we are going to check whether a password is strong or not and generate a strong pasword for the user
import random
def pass_suggestion(password1,num,schar,cap_letter):

    if schar==0:
        password1= password1 +  str(random.choice('@''&''%''*''!''$''#''^''?''|''/''\\'))
    if num==0:
        password1= password1 + str(random.randint(1,100))
  
    if cap_letter==0:
        # password1=  password1[:3] + password1[3].upper() + password1[4:]
        password1 = password1.title()

    
    return password1

password=input("Enter Your Password to check it is strong or not: ").strip()
num=0
schar=0
cap_letter=0
strong=f'Your password "{password}" is strong!!'
weak =f'Your password "{password}" is weak!! Change It'
medium = f'Your password "{password}" has medium security'
p=1
if len(password)<6:
    print(weak)

elif len(password)>=14:
    print(strong)
    p=0

elif '@123' in password:
    print(weak)
    password= password.replace('@123',str(random.choice('@''&''%''*''!''$''#''^''?''|''/''\\')) + str(random.randint(100,1000)))

    
else:
    for i in password:
        if ord(i)>=48 and ord(i)<=57:
            num=num+1
        elif ord(i)>=33 and ord(i)<=47 or ord(i)>=58 and ord(i)<=64 or ord(i)>=91 and ord(i)<=96:
            schar=schar+1
        elif ord(i)>=65 and ord(i)<=90:
            cap_letter=cap_letter+1
    
    if num>0 and schar>0 and cap_letter>0:
        print(strong)
        p=0
    elif num>0 and schar>0 or cap_letter>0 and num>0 or schar>0 and cap_letter>0:
        print(medium)
    else:
        print(weak)


if p:  
    print(f"Password Suggestion: {pass_suggestion(password,num,schar,cap_letter)}")

if p:
    print("---------------------------------------------------")
    print("Tips for a Strong password: ")
    print(" 1. password should have a Number in it")
    print(" 2. password should have a special character in it")
    print(" 3. password should have a capital letter in it")
    print("---------------------------------------------------")


    