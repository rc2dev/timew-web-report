from timew import timewarrior
from datetime import date, datetime, timedelta

def calculate_totals():
    date_format = '%Y%m%dT%H%M%SZ'

    tw = timewarrior.TimeWarrior()
    summary = tw.summary('1970-01-01', datetime.now())

    totals = {}
    for entry in summary:
        start = datetime.strptime(entry['start'], date_format)
        if 'end' in entry:
            end = datetime.strptime(entry['end'], date_format)
        else:
            end = datetime.utcnow()

        elapsed = end - start
        week = start.strftime('%Y-%U')
        if week not in totals:
            totals[week] = {}

        for tag in entry['tags']:
            if tag in totals[week]:
                totals[week][tag] += elapsed
            else:
                totals[week][tag] = elapsed

    for week in totals:
        for tag in totals[week]:
            totals[week][tag] = str(totals[week][tag])

    return totals
