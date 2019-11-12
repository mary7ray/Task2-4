from datetime import timedelta
def date_time():
    a = timedelta(hours=12, minutes=10, seconds=50)
    b = timedelta(hours=14, minutes=45, seconds=30)
    delta = b-a
    print(delta)

print(date_time())