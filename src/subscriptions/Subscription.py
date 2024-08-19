from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from src.config.config import Category, Plan, PLAN_DURATION, SUBSCRIPTION_PRICES, RENEWAL_REMINDER_DAYS


class Subscription:
    type_of_subscription: Category
    start_date: datetime
    end_date: datetime
    time_remaining: timedelta
    subscription_price: int


    def __init__(self, *, subscription_type: Category, plan: Plan, start_date: datetime):
        self.type_of_subscription = subscription_type
        self.start_date = start_date
        self.end_date = self._calculate_end_date(plan)
        self.subscription_price = self._get_subscription_price(subscription_type,plan)

    def __calculate_end_date(self,plan:Plan) -> datetime:
        months = PLAN_DURATION[plan]
        return self.start_date + relativedelta(months=months)
    
    def __get_subscription_price(self, subscription_type: Category, plan: Plan) -> int:
        return SUBSCRIPTION_PRICES.get(subscription_type, {}).get(plan, 0)
   
    @property
    def time_remaining(self) -> timedelta:
        return self.end_date - datetime.now()
    
    @property
    def notification_date(self) ->timedelta:
        return self.end_date - relativedelta(days=RENEWAL_REMINDER_DAYS)

    def __eq__(self, other):
        if not isinstance(other,Subscription):
            return False
        return (
            self.type_of_subscription == other.type_of_subscription and
            self.start_date == other.start_date and
            self.end_date == other.end_date and
            self.subscription_price == other.subscription_price
        )

#child Classes
class Music(Subscription):
    def __init__(self, *, plan: Plan, start_date: datetime):
        super().__init__(subscription_type=Category.MUSIC, plan=plan, start_date=start_date)


class Video(Subscription):
    def __init__(self, *, plan: Plan, start_date: datetime):
        super().__init__(subscription_type=Category.VIDEO, plan=plan, start_date=start_date)


class Podcast(Subscription):
    def __init__(self, *, plan: Plan, start_date: datetime):
        super().__init__(subscription_type=Category.PODCAST, plan=plan, start_date=start_date)
