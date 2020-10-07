amount_min = int(input("enter the amount of minutes"))
if amount_min<=50 and amount_min>=0:
    print('100')
elif amount_min>50 and amount_min<=100:
    print('150')
elif amount_min>100 :
    dod_min=amount_min-100
    print(dod_min*2+150)
else:
    print('error')