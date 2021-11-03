print("select your oparator")
print("1.add")
print("2.subtrect")
print("3.multiply")
print("4.divide")
operator =input()
if operator =="1":
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The sum is :"+ str(int(numb1)+int(numb2)))
elif operator =="2":
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The sbtrect is :"+ str(int(numb1)-int(numb2)))
elif operator =="3":
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The multiply is :"+ str(int(numb1)*int(numb2)))
else:
    numb1=input("enter your value")
    numb2=input("enter your value")
    print("The divide2 is :"+str(int(numb1)/int(numb2)))
