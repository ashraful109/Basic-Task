# year = int(input("enter your year :"))
# if year % 400 ==0:
#     print("leap year")
# elif year % 100 ==0:
#     print("not a leap year")
# elif year % 4 ==0:
#     print("leap year")
# else:
#     print("not a leap year")


# year = int(input("enter your year :"))
# if year % 400 == 0:
#     print("leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("leap year")
# else:
#     print("nor a leat year")

year = int(input("enter year :"))
if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
    print("leap year")
else:
    print("not a leap year")