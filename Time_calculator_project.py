def add_time(start, duration, day = ''):
    start_mid_index = start.find(' ')
    time = start[:start_mid_index]
    meridian = start[start_mid_index + 1:]
    start_time_mid_index = time.find(':')
    start_time_hours = int(time[:start_time_mid_index])
    start_time_minutes = int(time[start_time_mid_index + 1:])
    duration_mid_index = duration.find(':')
    duration_hours = int(duration[:duration_mid_index])
    duration_minutes = int(duration[duration_mid_index + 1:])

    hours = start_time_hours + duration_hours 
    minutes = start_time_minutes + duration_minutes
    days = 0

    if minutes > 60:
        hours += 1
        minutes = minutes % 60
    else:
        pass
    
    for hour in range(1,hours + 1):
        if hour % 24 == 0:
            days += 1
        else:
            pass

    minutes = '0' + str(minutes) if len(str(minutes)) == 1 else minutes

    meridian1 = ''

    if meridian == 'AM':
        meridian1 = 'AM'
    else:
        meridian1 = 'PM'

    odd_or_even = days*24 + hours

    if meridian == 'AM' and odd_or_even % 24 >= 12:
        meridian = 'PM'
    elif meridian == 'AM' and odd_or_even % 24 < 12:
        meridian = 'AM'
    elif meridian == 'PM' and odd_or_even % 24 >= 12:
        meridian = 'AM'
    elif meridian == 'PM' and odd_or_even % 24 < 12:
        meridian = 'PM'
    
    if meridian1 == 'PM' and meridian == 'AM':
        days += 1
    else:
        pass

    if hours % 12 == 0:
        hours = 12 
    elif hours % 12 != 0:
        hours = hours % 12
    else:
        pass

    if day:
        day = [char.lower() for char in day]
        day[0] = day[0].upper()
        day = ''.join(day)
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        index = week_days.index(day) 
        final_day = week_days[((index + days)%7)]
        if days == 1:
            final_day = f', {final_day} (next day)'
        elif days == 0:
            final_day = f', {final_day}'
        else:
            final_day = f', {final_day} ({days} days later)'
    else:
        if days == 1:
            final_day = ' (next day)'
        elif days == 0:
            final_day = ''
        else:
            final_day = f' ({days} days later)'

    new_time = [str(hours),':', str(minutes), ' ', meridian, final_day]
    new_time = ''.join(new_time)
    print(new_time)
    return new_time

add_time('3:00 PM', '3:10')
add_time('11:30 AM', '2:32', 'Monday')
add_time('11:43 AM', '00:20')
add_time('10:10 PM', '3:30')
add_time('11:43 PM', '24:20', 'tueSday')
add_time('6:30 PM', '205:12')