from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from src.config.config import Category, Plan, PLAN_DURATION, SUBSCRIPTION_PRICES


class Subscription:
    type_of_subscription: Category
    start_date: datetime
    end_date: datetime
    time_remaining: timedelta
    subscription_price: int

    def __init__(self, *, subscription_type: Category, plan: Plan, start_date: datetime):
        self.type_of_subscription = subscription_type
        self.start_date = start_date

        #adding the duration to the start date
        if not isinstance(plan, Plan):
            raise TypeError("plan must be a Plan enum number!")
        months = PLAN_DURATION[plan]
        self.end_date = self.start_date + relativedelta(months=months)
        self.time_remaining = self.end_date - self.start_date
        
        #plan have calculated amount already!
        self.subscription_price = SUBSCRIPTION_PRICES[subscription_type][plan]

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
