from src.user.user import User
from src.config.config import CATEGORY_FROM_STRING, TOPUP_TYPE_FROM_STRING
# RENEWAL_REMINDER MUSIC 10-03-2022
# RENEWAL_REMINDER VIDEO 10-05-2022
# RENEWAL_REMINDER PODCAST 10-03-2022
# RENEWAL_AMOUNT 750


class Output_writer:
    user: User

    def __init__(self,user: User) -> None:
        self.user = user

    def print_details(self):

        for subscription in self.user.subscriptions:
            subscription_type = {key for key, value in CATEGORY_FROM_STRING.items() if value == subscription.type_of_subscription}
            str = f"RENEWAL_REMINDER {', '.join(subscription_type)} {subscription.notification_date.strftime('%d-%m-%Y')}"
            print(str)
        
        for topup in self.user.top_ups:
            topup_type = {key for key, value in TOPUP_TYPE_FROM_STRING.items() if value == topup.type_of_top_up}
            str = f"RENEWAL_REMINDER {', '.join(topup_type)} {topup.notification_date.strftime('%d-%m-%Y')}"
            print(str)