R = int(input("enter your score: "))
if R>=0 and R<=59:
    print("Unsatisfactory")
elif R>=60 and R<=64:
    print("Marginal")
elif R>=65 and R<=74:
    print("Satisfactory")
elif R>=75 and R<=84:
    print("Good")
elif R>=85 and R<=94:
    print("Very good")
elif R>=95 and R<=100:
    print("Exellent")
else:
    print('error')