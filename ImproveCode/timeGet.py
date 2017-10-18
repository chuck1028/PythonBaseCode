import datetime

d = datetime.datetime.now()


def get_prev_day(cur_day, num):
    gap_days = datetime.timedelta(days=num)
    prev_day = cur_day - gap_days
    date_from = datetime.datetime(prev_day.year, prev_day.month, prev_day.day, 0, 0, 0)
    date_to = datetime.datetime(prev_day.year, prev_day.month, prev_day.day, 23, 59, 59)
    return (date_from, date_to)


def get_prev_week(cur_day):
    week_days = datetime.timedelta(days=d.isoweekday())
    week_end = cur_day - week_days
    gap_days = datetime.timedelta(days=6)
    week_start = week_end - gap_days
    date_from = datetime.datetime(week_start.year, week_start.month, week_start.day, 0, 0, 0)
    date_to = datetime.datetime(week_end.year, week_end.month, week_end.day, 23, 59, 59)
    return (date_from, date_to)


def get_prev_month(cur_day):
    gap_days = datetime.timedelta(days=cur_day.day)
    month_end = cur_day - gap_days
    date_from = datetime.datetime(month_end.year, month_end.month, 1, 0, 0, 0)
    date_to = datetime.datetime(month_end.year, month_end.month, month_end.day, 23, 59, 59)
    return (date_from, date_to)
