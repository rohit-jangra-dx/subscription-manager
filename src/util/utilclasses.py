from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.config.config import RENEWAL_REMINDER_DAYS, DATE_FORMAT


class NotificationManager:
    @staticmethod
    def get_notification_date(end_date: datetime) -> str:
        notification_date = end_date - relativedelta(days=RENEWAL_REMINDER_DAYS)
        return notification_date.strftime(DATE_FORMAT)