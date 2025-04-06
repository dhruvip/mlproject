import sys

def error_messgae_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occured in the python script [{filename}] \
        line number [{exc_tb.tb_lineno}] and error details [{str(error)}]"
    
    return error_message


class CustomException(Exception):

    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_messgae_detail(error_message, error_detail=error_details)
    
    def __str__(self):
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e,sys)