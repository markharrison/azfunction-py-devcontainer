import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python Random Color function processed a request.')

    str='blue lightblue darkblue'
    x=str.split()
    randcol = random.choice(x)
    print(randcol)


    return func.HttpResponse(f"{randcol}")
 
