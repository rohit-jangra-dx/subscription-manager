from typing import List
from src.config.config import CATEGORY_FROM_STRING, TOPUP_TYPE_FROM_STRING
# RENEWAL_REMINDER MUSIC 10-03-2022
# RENEWAL_REMINDER VIDEO 10-05-2022
# RENEWAL_REMINDER PODCAST 10-03-2022
# RENEWAL_AMOUNT 750


class Output_writer:
    logs: List[str]

    def __init__(self,logs: List[str]) -> None:
        self.user = logs

    def print_details(self):
        for log in self.logs:
            print(log)