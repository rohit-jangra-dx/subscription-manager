from typing import List
from src.user.user import User
from src.config.config import CATEGORY_FROM_STRING, PLAN_FROM_STRING, TOPUP_TYPE_FROM_STRING
from datetime import datetime
from src.util import validate_date, findDuplicatesInList

#exceptions
from src.exceptions.subscriptionerr import SubscriptionError, SubscriptionsNotFoundError, DuplicateCategoryError
from src.exceptions.topuperr import TopUpError, DupilicateTopUpError, SubscriptionNotFoundDuringTopUp

#INPUT_COMMANDS 
INPUT_COMMANDS = {
    'start_date':"START_SUBSCRIPTION",
    'add_subscription': "ADD_SUBSCRIPTION",
    'add_topup':'ADD_TOPUP',
    'print_details':'PRINT_RENEWAL_DETAILS'
}
#to_be_printed
To_Print = {
    'renewal_reminder':"RENEWAL_REMINDER",
    'renewal_amount':'RENEWAL_AMOUNT'
}

class InputParser:
    filename: str
    user: User
    logs: List[str]

    def __init__(self,filename: str):
        self.filename = filename
        self.user = User()
        self.subscription_start_date = datetime.now()
        self.logs = []

    def parse(self) -> User | None:
            try:
                with open(self.filename, 'r') as file:
                    for line in file:
                        line = line.strip()  # Remove any extraneous whitespace
                        if line.startswith(INPUT_COMMANDS['start_date']):
                            self._handle_start_date(line)
                        elif line.startswith(INPUT_COMMANDS['add_subscription']):
                            self._handle_add_subscription(line)
                        elif line.startswith(INPUT_COMMANDS['add_topup']):
                            self._handle_add_topup(line)
                        elif line.startswith(INPUT_COMMANDS['print_details']):
                            self._handle_print_details()
                        else:
                            raise ValueError(f"Unknown command found during parsing: {line}")

                return self.user
            except SubscriptionError as e:
                print(e)
                return None

    def _handle_start_date(self, line: str):
        _, startdate = line.split()
        try:
            self.subscription_start_date = validate_date(startdate)
        except SubscriptionError as e:
            self.logs.append(e)

    def _handle_add_subscription(self, line: str):
        _, category, plan = line.split()
        try:
            if findDuplicatesInList("type_of_subscription",CATEGORY_FROM_STRING[category],self.user.subscriptions):
                raise DuplicateCategoryError()

            subscription = self.user.add_subscription(
                category=CATEGORY_FROM_STRING[category],
                plan=PLAN_FROM_STRING[plan],
                start_date=self.subscription_start_date
            )
            self.logs.append(f"{To_Print['renewal_reminder']} {subscription.notification_date}")
        except SubscriptionError as e:
            self.logs.append(e)

    def _handle_add_topup(self, line: str):
        _, topup, duration = line.split()
        try:
            if len(self.user.top_ups) == 1:
                raise DupilicateTopUpError()
            elif len(self.user.subscriptions) == 0:
                raise SubscriptionNotFoundDuringTopUp()
                
            self.user.add_top_up(
                top_up_type=TOPUP_TYPE_FROM_STRING[topup],
                duration=int(duration),
                start_date=self.subscription_start_date
            )
        except TopUpError as e:
            self.logs.append(e)

    def _handle_print_details(self):
        try:
            if len(self.user.subscriptions) == 0:
                raise SubscriptionsNotFoundError()
            else:
                self.logs.append(f"{To_Print['renewal_amount']} {self.user.total_price}")
                for log in self.logs:
                    print(log)
        except SubscriptionError as e:
            self.logs.append(e)
            