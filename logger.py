__author__ = 'Josh'
from datetime import datetime

from client import FitBitScrapper

date_from_results = lambda d: datetime.strptime(d, '%Y-%m-%d')
last_grabbed_date = datetime(2014, 1, 1)
log_date = lambda d: d.strftime('%Y-%m-%d')

print "Grabbing Fitbit steps and sleep since %s..." % log_date(last_grabbed_date)

client = FitBitScrapper(u'ychian@gmail.com', u'6gUQnCDifEkaHGqdTsSLZtxvIYlAuB9ROjbohPcmWe', verbose=True)
data_by_day = client.get_steps_since_date(last_grabbed_date)

with open('fitbit.json', 'a') as f:
    for date_str in sorted(data_by_day.keys(), key=date_from_results):
        log_line = data_by_day[date_str]
        f.write(log_line.strip() + '\n')