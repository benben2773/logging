import logging
# from requests import Request
import string
import random
import time
# from Request import Request
from fastapi import FastAPI, Request
from uicheckapp.services import EchoService
from check.services import EchoService as EchoService1

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.

app = FastAPI()

ins = EchoService()
ins1 = EchoService1()

# seen = set()
# for name in [
#     *logging.root.manager.loggerDict.keys(),
#     "gunicorn",
#     "gunicorn.access",
#     "gunicorn.error",
#     "uvicorn",
#     "uvicorn.access",
#     "uvicorn.error",
# ]:
#     in_logger = logging.getLogger(name)
#     print(in_logger.name)
#     if name == "uvicorn":
#         in_logger.info(" Here we are")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response

@app.get("/")
async def root():
    logger.info("logging from the root logger")
    ins.echo("hi")
    ins1.echo(" I am here")
    return {"status": "alive"}
