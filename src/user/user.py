from datetime import datetime

from src.config.config import Category, Plan
from src.subscriptions.Subscription import Subscription
from src.subscriptions.topup import  Topup
from src.subscriptions.subscription_factory import subscription_factory
from datetime import datetime
from typing import List

class User:
    subscriptions: List[Subscription]
    top_ups: List[Topup]

    def __init__(self):
        self.subscriptions = []
        self.top_ups = []

    def add_subscription(self, *,category: Category,plan: Plan, start_date:datetime):
        try:
            subscription = subscription_factory(category,plan,start_date)
            self.subscriptions.append(subscription)
        except Exception as e:
            print(f'something happened during subscribing {e}')

    def remove_subscription(self,subscription):
        if subscription in self.subscriptions:
            self.subscriptions.remove(subscription)
