import calendar

for week in caledar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue

        print(day)
