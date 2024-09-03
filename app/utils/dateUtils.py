# dateUtils.py


from datetime import timedelta


class DateUtils:
    @staticmethod
    def days_to_seconds(days: int):
        return int(timedelta(days=days).total_seconds())
