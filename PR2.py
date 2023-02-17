year = int(input("Введите год: "))

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and year % 100 == 0):
    vess = True
else:
    vess = False

month = 1
final = 0
i = 1
while month <= 13:
    if month % 2 == 0:
        maxday = 30
    elif month % 2 != 0:
        maxday = 31
    if(month == 2):
        if vess == True:
            maxday = 29
        else:
            maxday = 28
    if(month == 8):
        maxday = 31
        month += 1

    while i <= maxday:
        des = i // 10
        day = i % 10
        final = final + des + day
        i += 1
    i = 1
    month += 1
    
print(final)