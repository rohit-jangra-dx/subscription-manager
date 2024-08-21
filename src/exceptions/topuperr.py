class TopUpError(Exception):
    pass


#base class for errors while adding top ups
class AddTopUpFailedError(TopUpError):
    
    def __init__(self, message:str) -> None:
        base_msg = "ADD_TOPUP_FAILED"
        full_msg = base_msg + " " + message
        super().__init__(full_msg)

#when u are adding top up and there is no active subscriptions.
class SubscriptionNotFoundDuringTopUp(AddTopUpFailedError):

    def __init__(self, message="SUBSCRIPTIONS_NOT_FOUND") -> None:
        super().__init__(message)
        