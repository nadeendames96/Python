# prob 2
# The problem check if password safe or not safe !
password=input("Enter a Password : ")
#RPS
RPS=len(password)
if len(password)<=15 and len(password)>=5:
    count_upper = 0
    count_lower = 0
    count_symbol = 0
    count_digit = 0
    #count_char=0
    for c in password:
        if c.isdigit():
          count_digit += 1
        elif c.isupper():
            count_upper+=1
        elif c.islower():
            count_lower+=1        
        else:
            count_symbol += 2
    x=50/(count_upper/count_lower)
    if x==0:
        print("Error")
    else:
            RPS+=x
    RPS+=count_symbol
    if ',' in password:
        RPS-=40
    if RPS > 50  and RPS<=100: 
       print("RPS : %d - is safe !"%RPS)
    else:
       print("RPS : %d - is not safe !"%RPS)

    pass
else:
    print("Password Length Must Be Between 15 And 5,Please Re-again Enter Password")
    pass


    # Nadeen Dames


  #elif c.isalpha():
        #    count_char += 1