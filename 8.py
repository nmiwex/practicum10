def print_datetime(date_time: str):
    """
    outputs the date and time in a different format
    """
    try:
        date, time = date_time.split(' ')
        month, day, year = map(int, date.split('/'))
        hour, minute, second = map(int, time.split(':'))
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not (1 <= month <= 12 and
                1 <= day <= 31 and
                0 <= hour <= 23 and
                0 <= day <= days_in_month[month - 1]):
            print('дата введена неверно 😧')
        else:
            year %= 100
            date = f'{day:02d}.{month:02d}.{year:02d}'

            am_pm = 'AM' if hour < 12 else 'PM'
            hour %= 12
            if hour == 0:
                hour = 12
            time = f'{hour:02d}:{minute:02d}:{second:02d} {am_pm}'

            print(date, time)
    except ValueError:
        print('дата введена неверно 😧')