from typing import List, Dict
from datetime import datetime
from src.config.config import DATE_FORMAT
from src.exceptions.subscriptionerr import InvalidDateError

def validate_date(date_string):
        try:
            date_object = datetime.strptime(date_string, DATE_FORMAT)
            if date_object.strftime(DATE_FORMAT) != date_string:
                raise InvalidDateError()
            return date_object
        except ValueError as e:
              raise InvalidDateError()

def findDuplicatesInList(key: str,value,list: List[Dict]) -> bool:
      
    for item  in list:
        item_value = getattr(item,key,None)
        if item_value == value:
             return True
    return False