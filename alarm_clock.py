def alarm_clock(day,vacation):
    if 0 < day < 6 and not vacation:
        return '7:00'
    elif day == 0 or day == 6 and not vacation:
        return '10:00'
    elif 0 < day < 6 and vacation:
        return '10:00'
    elif day == 0 or day == 6 and vacation:
        return 'off'



print alarm_clock(1,False)
print alarm_clock(5,False)
print alarm_clock(0,False)
print alarm_clock(6,True)
