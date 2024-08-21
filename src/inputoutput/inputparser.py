from src.user.user import User
from src.inputoutput.outputwriter import OutputWriter
from src.subscriptions.subscriptionmanager import SubscriptionManager
#exceptions
from src.exceptions.subscriptionerr import SubscriptionError


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
    '''
    it initializes user and output writer needed for subscription manager
    it parses over each line and according to command found, subscription manager 
    handles the task
    '''
    def __init__(self,filename: str):
        self.filename = filename
        self.__user = User()
        self.__output_writer = OutputWriter()
        self.__subscription_manager = SubscriptionManager(self.__user,self.__output_writer)

    def parse(self):
            try:
                with open(self.filename, 'r') as file:
                    for line in file:
                        line = line.strip()  # Remove any extraneous whitespace
                        
                        if line.startswith(INPUT_COMMANDS['start_date']):
                            _, startdate = line.split()
                            self.__subscription_manager.handle_set_date(startdate)
                        
                        elif line.startswith(INPUT_COMMANDS['add_subscription']):
                            _, category, plan = line.split()
                            self.__subscription_manager.handle_add_subscription(category,plan)
                        
                        elif line.startswith(INPUT_COMMANDS['add_topup']):
                            _, topup, duration = line.split()
                            self.__subscription_manager.handle_add_top_up(topup,duration)
                        
                        elif line.startswith(INPUT_COMMANDS['print_details']):
                            self.__subscription_manager.handle_print_details()
                        else:
                            raise ValueError(f"Unknown command found during parsing: {line}")
            except SubscriptionError as e:
                print(e)
