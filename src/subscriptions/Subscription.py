from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from src.util.utilclasses import NotificationManager
from src.config.config import Category, Plan, PLAN_DURATION, SUBSCRIPTION_PRICES, RENEWAL_REMINDER_DAYS,DATE_FORMAT

#custom exceptions
from src.exceptions.subscriptionerr import *

class Subscription:
    def __init__(self, *, subscription_type: Category, plan: Plan, start_date: datetime):
        self.__type_of_subscription = subscription_type
        self.__start_date = start_date
        self.__end_date = self._calculate_end_date(plan)
        self.__subscription_price = self._get_subscription_price(subscription_type,plan)
        self.__notification_date = NotificationManager.get_notification_date(self.__end_date)

    def __calculate_end_date(self,plan:Plan) -> datetime:
        months = PLAN_DURATION[plan]
        return self.start_date + relativedelta(months=months)
    
    def __get_subscription_price(self, subscription_type: Category, plan: Plan) -> int:
        return SUBSCRIPTION_PRICES.get(subscription_type, {}).get(plan, 0)
    
    @property
    def type_of_subscription(self) -> Category:
        return self.__type_of_subscription
    
    @property
    def start_date(self) -> datetime:
        return self.__start_date
    
    @property
    def end_date(self) -> datetime:
        return self.__end_date
    
    @property
    def subscription_price(self) -> int:
        return self.__subscription_price

    @property
    def notification_date(self) ->str:
        return self.__notification_date
    

    def __eq__(self, other):
        if not isinstance(other,Subscription):
            return False
        return (
            self.type_of_subscription == other.type_of_subscription and
            self.start_date == other.start_date and
            self.end_date == other.end_date and
            self.subscription_price == other.subscription_price
        )

    def __repr__(self) -> str:
        return (f"<Subscription(type={self._subscription_type}, plan={self._plan}, "
                f"start_date={self._start_date}, end_date={self._end_date}, "
                f"price={self._subscription_price})>")
