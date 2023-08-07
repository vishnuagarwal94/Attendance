code = input("Enter code")
if len(code)==8:
    c = list(code)
    #print(c)
    if c[0]=='0':
        print("Organic Egg")
    elif c[0]=='1':
        print("Free Range Egg")
    elif c[0]=='2':
        print("Barn Egg")
    elif c[0]=='3':
        print("Cage Egg")
    else:
        print("Invalid code")
    cc = c[1]+c[2]
    #print(cc)
    if cc=='IN':
        print("Country Of Origin : INDIA")
    elif cc=='UK':
        print("Country Of Origin : United Kingdom")
    elif cc==FR:
        print("Country Of Origin : France")
    elif cc==ES:
        print("Country Of Origin : Spain")
    else:
        print("Invalid code")
    Farm_Id = c[3]+c[4]+c[5]+c[6]+c[7]
    print("Farm Id : "+Farm_Id)
    # if c[0]=='0':
    #     print("Organic Egg")
    # elif c[0]=='1':
    #     print("Free Range Egg")
    # elif c[0]=='2':
    #     print("Barn Egg")
    # elif c[0]=='3':
    #     print("Cage Egg")
    # else:
    #     print("Invalid code")
else:
    print("Invalid code")    