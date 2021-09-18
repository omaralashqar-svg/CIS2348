print("Birthday Calculator")
print("Current day")
print("Month:")
cMonth = int(input())
print("Day:")
cDay = int(input())
print("Year:")
cYear = int(input())
print("Birthday")
print("Month:")
Month = int(input())
print("Day:")
Day = int(input())
print("Year:")
Year = int(input())
Fyear = cYear - Year
if Month > cMonth:
    Fyear = Fyear - 1
elif Month == cMonth:
    if Day > cDay:
        Fyear = Fyear -1

print("You are",Fyear,"years old.")