from typing import List,TypeVar, Union
from datetime import datetime
from src.config.config import DATE_FORMAT
from src.exceptions.subscriptionerr import InvalidDateError

#used in validation for dates incoming from input
def validate_date(date_string):
        try:
            date_object = datetime.strptime(date_string, DATE_FORMAT)
            if date_object.strftime(DATE_FORMAT) != date_string:
                raise InvalidDateError()
            return date_object
        except (ValueError, InvalidDateError )as e:
              raise InvalidDateError()


T = TypeVar("T")

#used for finding duplicates in subscriptions list and topups
def find_duplicates_in_list(key: str,value,list: List[T]) -> bool:
      
    for item  in list:
        item_value = getattr(item,key,None)
        if item_value == value:
             return True
    return False

#used to remove items from a list of class instances eg. topups and subscriptions
def remove_item_in_list(item:T,list: List[T])-> Union[T,None]:
    if item in list:
        list.remove(item)
        return item
    else:
        return None     