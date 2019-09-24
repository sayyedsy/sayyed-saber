a="yes"
while  a=="yes":
    try:
        name=input("enter file name=")
        file1=open(name,"r")
        data=file1.read()
        print(data)
    except:
        print("file is not available")
        print("please create new file")
        name=input("enter file name=")
        file1=open(name,"w")
        data=input("enter your data=")
        file1.write(data)
        print("yesssssssss")
    finally:
        print("operation is done")
        a=input("do you want see   another file(YES/NO)=")
