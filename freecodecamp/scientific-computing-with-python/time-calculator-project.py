def add_time(start, duration, current_day=''):

    # variables
    start_hour = int(start[:-6])
    start_min = int(start[-5:-3])
    start_period_day = start[-2:]
    duration_hour = int(duration[:-3])
    duration_min = int(duration[-2:])
    n_days = 0
    final_day = ''
    days_of_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

    # calculations
    result_hour = start_hour + duration_hour
    result_min = start_min + duration_min

    # minute calculations
    if result_min >= 60:
        result_hour += 1
        result_min -= 60

    # hour calculations
    while result_hour >= 12:
        if start_period_day == 'AM':
            start_period_day = 'PM'
        elif start_period_day == 'PM':
            start_period_day = 'AM'
            n_days += 1

        if result_hour == 12:
            break

        result_hour -= 12
    if current_day:
        start_period_day += ','

    # analyze how many n days
    if n_days == 1:
        result_n_days = '(next day)'
    elif n_days > 1:
        result_n_days = f'({n_days} days later)'

    # calculate days of the week
    if current_day:
        day = n_days + days_of_week.index(current_day.lower())
        while day >= 7:
            day -= 7

        final_day = days_of_week[day].capitalize()

    # final result
    new_time = [
        f'{result_hour}:{result_min:02}',
        start_period_day, 
        final_day if final_day else '',
        result_n_days if n_days else ''
    ]

    return ' '.join(part for part in new_time if part)

print(add_time('2:59 AM', '24:00', 'saturDay'))
