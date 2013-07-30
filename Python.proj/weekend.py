def weekend(day):
    t=True
    f=False
    day1='Saturday'
    day2='Sunday'
    if day == day1:
        return (t)
    if day == day2:
        return (t)
    else:
        return (f)
      
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False