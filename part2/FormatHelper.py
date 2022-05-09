from datetime import datetime


def format_date_for_api(date: datetime) -> str:
    return f"{date.year}-{__format_with_zero(date.month)}-{__format_with_zero(date.day)}"


def format_date_for_ui(date: datetime) -> str:
    return f"{__format_with_zero(date.day)}.{__format_with_zero(date.month)}"


def __format_with_zero(value) -> str:
    return '{:02d}'.format(value)
