def seconds_since_year(date_time: str):
    """
    counts how many seconds have passed since 01/01/YYYY 00:00:00
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
            passed_days = sum(days_in_month[:month - 1]) + day - 1
            print(passed_days * 86400 + hour * 3600 + minute * 60 + second)

    except ValueError:
        print('дата введена неверно 😧')