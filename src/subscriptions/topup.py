from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from src.config.config import TopUpType, TOPUP_PRICES

class Topup:
    type_of_top_up: TopUpType
    top_up_price: int
    start_date: datetime
    end_date: datetime
    time_remaining: timedelta

    def __init__(self,*,top_up_type: TopUpType,duration: int, start_date:datetime,):

        self.type_of_top_up = top_up_type

        #setting up the dates
        self.start_date = start_date

        self.end_date =  self.start_date + relativedelta(months=duration)

        self.time_remaining = self.end_date - self.start_date

        #duration is in months
        self.top_up_price = TOPUP_PRICES[top_up_type] * duration

