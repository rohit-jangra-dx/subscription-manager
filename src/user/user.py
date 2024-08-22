from src.config.config import Category, Plan, TopUpType, MAX_TOPUP_LIMIT
from src.subscriptions.Subscription import Subscription
from src.subscriptions.topup import  Topup
from datetime import datetime
from typing import List, Union
from src.util.utilfunctions import find_duplicates_in_list, remove_item_in_list

#exceptions
from src.exceptions.subscriptionerr import DuplicateCategoryError
from src.exceptions.topuperr import DupilicateTopUpError, SubscriptionNotFoundDuringTopUp

class User:
    def __init__(self):
        self.__subscriptions = []
        self.__top_ups = []
        self.__total_price = 0

    def add_subscription(self, *,category: Category,plan: Plan, start_date:datetime)-> Subscription:
        """
        this one will raise exception in case if same category
        plan already exists!
        """
        if find_duplicates_in_list("type_of_subscription",category,self.__subscriptions):
            raise DuplicateCategoryError()
            
        subscription = Subscription(subscription_type=category,plan=plan,start_date=start_date)
        self.__subscriptions.append(subscription)
            
        #adding up to the total_price
        self.__total_price += subscription.subscription_price
        return subscription

    def remove_subscription(self,subscription) -> Union[Subscription,None]:
        return remove_item_in_list(subscription, self.__subscriptions)

    def add_top_up(self, *,top_up_type: TopUpType, duration: int, start_date:datetime) -> Topup:
        """
        it will raise error if user tops up when there is no active subscription
        and when there is another top up active  during toping up (more than one not allowed)
        """
        if len(self.__subscriptions) == 0:
            raise SubscriptionNotFoundDuringTopUp()
        elif len(self.__top_ups) == MAX_TOPUP_LIMIT:
            raise DupilicateTopUpError()
            
        top_up = Topup(top_up_type=top_up_type, duration=duration, start_date=start_date)
        self.__top_ups.append(top_up)

        #adding up to the total_price
        self.__total_price += top_up.top_up_price
        return top_up

    def remove_top_up(self,top_up) -> Union[Topup, None]:
        return remove_item_in_list(top_up, self.__top_ups)
        
    @property
    def total_price(self)-> int:
         return self.__total_price
     
    @property
    def subscriptions(self) -> List[Subscription]:
        return self.__subscriptions
    
    @property
    def top_ups(self) -> List[Topup]:
        return self.__top_ups