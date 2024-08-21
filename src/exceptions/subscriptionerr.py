
class SubscriptionError(Exception):
    pass


#for now let's gather all error classes in one file

#when there are no subscriptions and print command occurs
class SubscriptionsNotFoundError(SubscriptionError):
    
    def __init__(self, message="SUBSCRIPTIONS_NOT_FOUND") -> None:
        super().__init__(message)
    

#base class for error that occurs during adding subscription
class AddSubscriptionFailedError(SubscriptionError):
    
    def __init__(self, message:str) -> None:
        base_msg = "ADD_SUBSCRIPTION_FAILED"
        full_msg = base_msg + " " + message
        super().__init__(full_msg)


#when wrong date i.e 07-19-2022 is given
class InvalidDateError(AddSubscriptionFailedError):
    
    def __init__(self, message="INVALID_DATE") -> None:
        super().__init__(message)
    

#when for the same user we have duplicate subscriptions of same category 
class DuplicateCategoryError(AddSubscriptionFailedError):

    def __init__(self, message="DUPLICATE_CATEGORY") -> None:
        super().__init__(message)
