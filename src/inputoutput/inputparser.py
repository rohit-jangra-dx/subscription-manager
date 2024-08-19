import traceback
from src.user.user import User
from src.config.config import CATEGORY_FROM_STRING, PLAN_FROM_STRING, TOPUP_TYPE_FROM_STRING
from datetime import datetime

commands = {
    'start_date':"START_SUBSCRIPTION",
    'add_subscription': "ADD_SUBSCRIPTION",
    'add_topup':'ADD_TOPUP',
    'print_details':'PRINT_RENEWAL_DETAILS'
}


class InputParser:
    filename: str
    user: User

    def __init__(self,filename: str):
        self.filename = filename
        self.user = User()

    def parse(self) -> User | None:
            try:
                with open(self.filename, 'r') as file:
                    for line in file:
                        line = line.strip()  # Remove any extraneous whitespace
                        if line.startswith(commands['start_date']):
                            self._handle_start_date(line)
                        elif line.startswith(commands['add_subscription']):
                            self._handle_add_subscription(line)
                        elif line.startswith(commands['add_topup']):
                            self._handle_add_topup(line)
                        elif line.startswith(commands['print_details']):
                            self._handle_print_details()
                        else:
                            raise ValueError(f"Unknown command found during parsing: {line}")

                return self.user
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Traceback details:")
                traceback.print_exc()
                return None

    def _handle_start_date(self, line: str):
        _, startdate = line.split()
        self.subscription_start_date = datetime.strptime(startdate, "%d-%m-%Y")

    def _handle_add_subscription(self, line: str):
        _, category, plan = line.split()
        self.user.add_subscription(
            category=CATEGORY_FROM_STRING[category],
            plan=PLAN_FROM_STRING[plan],
            start_date=self.subscription_start_date
        )

    def _handle_add_topup(self, line: str):
        _, topup, duration = line.split()
        self.user.add_top_up(
            top_up_type=TOPUP_TYPE_FROM_STRING[topup],
            duration=int(duration),
            start_date=self.subscription_start_date
        )

    def _handle_print_details(self):
        print("Work in progress")
            