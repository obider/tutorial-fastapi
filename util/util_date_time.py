from datetime import datetime


def convert_datetime_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def convert_str_date(dt_str: str) -> datetime:
    return datetime.strptime(dt_str, "%d-%m-%Y")
