from datetime import datetime,timedelta,timezone

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now=datetime.now()
print(now)
print(now.strftime('%a, %b %d %H:%M'))
print(now+timedelta(hours=12))
print(now-timedelta(days=2))
print(now+timedelta(days=13,hours=23))

tz_utc_8=timezone(timedelta(hours=8))
dt=now.replace(tzinfo=tz_utc_8)
print(dt)

utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=0)))
print(tokyo_dt)
