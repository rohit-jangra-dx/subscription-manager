from typing import Union

from src.user.user import User
from src.inputoutput.outputwriter import OutputWriter
from src.util.utilfunctions import validate_date, has_instance
from src.config.config import CATEGORY_FROM_STRING, PLAN_FROM_STRING, TOPUP_TYPE_FROM_STRING
#exceptions
from src.exceptions.subscriptionerr import SubscriptionError, InvalidDateError, InvalidDateErrorDuringSubscription, SubscriptionsNotFoundError
from src.exceptions.topuperr import TopUpError , InvalidDateErrorDuringTopUp

#used for formatting logs
To_Print = {
    'renewal_reminder':"RENEWAL_REMINDER",
    'renewal_amount':'RENEWAL_AMOUNT'
}

class SubscriptionManager:

    def __init__(self,user: User,output_writer: OutputWriter) -> None:
        self.__user = user
        self.__output_writer = output_writer
        self.__start_date = None
    
    def handle_set_date(self, date: str):
        try:
            self.__start_date = validate_date(date)
        except SubscriptionError as e:
            self.__output_writer.set_error_logs(e)

    #tried to reduce the code redundancy
    def __check_for_invalid_date_before_action(self,exception: Union[SubscriptionError,TopUpError]) -> bool:
        try:
            if has_instance(InvalidDateError,self.__output_writer.get_error_logs()):
                raise exception()
            return True
        except (SubscriptionError, TopUpError) as e:
            self.__output_writer.set_error_logs(e)
            return False

    def handle_add_subscription(self,category: str, plan: str):
            if self.__check_for_invalid_date_before_action(InvalidDateErrorDuringSubscription):    
                try:
                    subscription = self.__user.add_subscription(category=CATEGORY_FROM_STRING[category],plan=PLAN_FROM_STRING[plan],start_date=self.__start_date)
                    self.__output_writer.set_output_logs(f"{To_Print['renewal_reminder']} {category} {subscription.notification_date}")          
                except SubscriptionError as e:
                    self.__output_writer.set_error_logs(e)

    def handle_add_top_up(self,top_up_type:str, duration: int):
        if self.__check_for_invalid_date_before_action(InvalidDateErrorDuringTopUp):    
            try:
                self.__user.add_top_up( top_up_type=TOPUP_TYPE_FROM_STRING[top_up_type],duration= int(duration),start_date=self.__start_date)
            except TopUpError as e:
                self.__output_writer.set_error_logs(e)
    
    def handle_print_details(self):
        """
        adds the renewal amount as final statement to output_writer,
        then prints the statement
        """
        try:
            if len(self.__user.subscriptions) == 0:
                raise SubscriptionsNotFoundError()                
            self.__output_writer.set_output_logs(f"{To_Print['renewal_amount']} {self.__user.total_price}")

        except SubscriptionError as e:
            self.__output_writer.set_error_logs(e)
        finally:
            self.__output_writer.print_logs()
            
    