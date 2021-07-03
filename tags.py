from timew import timewarrior
from datetime import date, datetime, timedelta
import subprocess


def calculate_totals():
    date_format = '%Y%m%dT%H%M%SZ'

    tw = timewarrior.TimeWarrior()
    summary = tw.summary('1970-01-01', datetime.now())
    unproductive_tags = get_unproductive_tags()

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
            totals[week] = {
                '_all': timedelta(0),
                '_prod': timedelta(0)
            }

        for tag in entry['tags']:
            if tag in totals[week]:
                totals[week][tag] += elapsed
            else:
                totals[week][tag] = elapsed

        totals[week]['_all'] += elapsed

        if is_productive(entry['tags'], unproductive_tags):
            totals[week]['_prod'] += elapsed

    for week in totals:
        for tag in totals[week]:
            totals[week][tag] = timedelta_format(totals[week][tag])

    return totals


def timedelta_format(delta):
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    return f'{hours:02}:{minutes:02}:{seconds:02}'


def get_unproductive_tags():
    config_key = 'custom.unproductive_tags'

    result = subprocess.run(
        ['timew', 'get', f'dom.rc.{config_key}'], capture_output=True, text=True)
    tags = result.stdout.strip().split(',')
    return tags


def is_productive(entry_tags, unproductive_tags):
    for tag in entry_tags:
        if tag not in unproductive_tags:
            return True

    return False
