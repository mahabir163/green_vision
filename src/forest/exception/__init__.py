import os
import sys          #System module to help expose all information about exception

def error_message_detail(error,error_details):
    try:
        _,_,exc_tb = error_details.exc_info()

        if exc_tb is None:
            return f"Error Occurred : {str(error)}"

        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        error_message = f"Error Occurred in: {0} ,Line Number: {1}, And Error message {2} ".format(
            file_name,exc_tb.tb_lineno,str(error)
        )

        return error_message
    except Exception as e:
        return f"error occurred: {str(error)}, additionaly, error in exception handling: {str(e)}"

class ForestException(Exception):
    def __init__(self,error_message,error_detail=sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message,error_detail)
    
    def __str__(self):              
        return self.error_message