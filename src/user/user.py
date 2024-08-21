from src.config.config import Category, Plan, TopUpType
from src.subscriptions.Subscription import Subscription
from src.subscriptions.topup import  Topup
from src.subscriptions.subscription_factory import subscription_factory
from src.subscriptions.topup import Topup
from datetime import datetime
from typing import List

class User:
    subscriptions: List[Subscription]
    top_ups: List[Topup]
    total_price: int

    def __init__(self):
        self.subscriptions = []
        self.top_ups = []
        self.total_price = 0

    def add_subscription(self, *,category: Category,plan: Plan, start_date:datetime)-> Subscription | None:
        try:
            subscription = subscription_factory(category,plan,start_date)
            self.subscriptions.append(subscription)
            
            #adding up to the total_price
            self.total_price += subscription.subscription_price

            return subscription
        except Exception as e:
            print(f'something happened during subscribing {e}')
            return None

    def remove_subscription(self,subscription):
        if subscription in self.subscriptions:
            self.subscriptions.remove(subscription)

    def add_top_up(self, *,top_up_type: TopUpType, duration: int, start_date:datetime) -> None | str:
        try:
            if len(self.subscriptions) <= 0:
                return "There are no subscriptions to top up for!"
            top_up = Topup(top_up_type=top_up_type,
                           duration=duration,
                           start_date=start_date)
            self.top_ups.append(top_up)

            #adding up to the total_price
            self.total_price += top_up.top_up_price

        except Exception as e:
            print(f"something happened during toping up {e}")
    
    def remove_top_up(self,top_up):

        if top_up in self.top_ups:
            self.top_ups.remove(top_up)