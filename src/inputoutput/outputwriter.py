from typing import List,TypedDict

class Logs(TypedDict):
    output:List[str]
    errors: List[Exception]

class OutputWriter:
    def __init__(self) -> None:
        self.__logs: Logs = {'output':[], 'errors':[]}

    def set_error_logs(self,e:Exception):
        self.__logs['errors'].append(e)
    
    def get_error_logs(self):
        return self.__logs['errors']

    def set_output_logs(self, output: str):
        self.__logs['output'].append(output)
    
    def get_output_logs(self):
        return self.__logs['output']

    def print_logs(self):
        """
        first print error logs if any
        then print output logs
        """
        for error in self.__logs['errors']:
            print(error)
        for output in self.__logs['output']:
            print(output)