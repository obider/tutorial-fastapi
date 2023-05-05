from datetime import datetime


def convert_datetime_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")
