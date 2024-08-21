from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from src.config.config import TopUpType, TOPUP_PRICES, RENEWAL_REMINDER_DAYS

class Topup:
    type_of_top_up: TopUpType
    top_up_price: int
    start_date: datetime
    end_date: datetime

    def __init__(self,*,top_up_type: TopUpType,duration: int, start_date:datetime):

        self.type_of_top_up = top_up_type

        #setting up the dates
        self.start_date = start_date
        self.end_date =  self._calculate_end_date(duration)

        #duration is in months
        self.top_up_price = self._get_subscription_price(top_up_type,duration)


    def _calculate_end_date(self,duration: int) -> datetime:
        return self.start_date + relativedelta(months=duration)
    
    def _get_subscription_price(self, top_up_type: TopUpType, duration: int) -> int:
        return TOPUP_PRICES.get(top_up_type, 0) * duration
   
    @property
    def time_remaining(self) -> timedelta:
        return self.end_date - datetime.now()
    
    @property
    def notification_date(self) -> timedelta:
        return self.end_date - relativedelta(days=RENEWAL_REMINDER_DAYS)


    def __eq__(self, other):
        if not isinstance(other, Topup):
            return False
        
        return (
            self.start_date == other.start_date and
            self.type_of_top_up == other.type_of_top_up and
            self.top_up_price == other.top_up_price and
            self.end_date == other.end_date
        )