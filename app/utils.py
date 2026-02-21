from datetime import datetime

def to_dt(val):
    return datetime.strptime(val, "%Y-%m-%d %H:%M:%S")