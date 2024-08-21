from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from src.config.config import TopUpType, TOPUP_PRICES, RENEWAL_REMINDER_DAYS
from src.util.utilclasses import NotificationManager
class Topup:
    def __init__(self,*,top_up_type: TopUpType,duration: int, start_date:datetime):

        self.__type_of_top_up = top_up_type
        #setting up the dates
        self.__start_date = start_date
        self.__end_date =  self.__calculate_end_date(duration)
        self.__notification_date = NotificationManager.get_notification_date(self.__end_date)
        self.__top_up_price = self._get_price(top_up_type,duration)


    def __calculate_end_date(self,duration: int) -> datetime:
        return self.start_date + relativedelta(months=duration)
    
    def _get_price(self, top_up_type: TopUpType, duration: int) -> int:
        return TOPUP_PRICES.get(top_up_type, 0) * duration
    
    @property
    def type_of_top_up(self) -> TopUpType:
        return self.__type_of_top_up
    
    @property   
    def start_date(self) -> datetime:
        return self.__start_date
    
    @property
    def end_date(self) -> datetime:
        return self.__end_date
    
    @property
    def notification_date(self) -> str:
        return self.__notification_date
    
    @property
    def top_up_price(self) -> int:
        return self.top_up_price


    def __eq__(self, other):
        if not isinstance(other, Topup):
            return False
        
        return (
            self.__start_date == other.__start_date and
            self.__type_of_top_up == other.__type_of_top_up and
            self.__top_up_price == other.__top_up_price and
            self.__end_date == other.__end_date
        )