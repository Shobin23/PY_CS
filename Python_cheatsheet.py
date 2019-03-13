#datetime-----------------------------------------------
#Naive datetime
import datetime
today = datetime.date(2015,5,20)
tday=datetime.date.today()
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())
print(today)

#timedelta--------------------------------------------
tdelta = datetime.timedelta(days=7)
# adding dates to current date
print(tdelta + tday)



