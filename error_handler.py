from fastapi import Request
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette import status


def validation_exception_handler(response, exc):
    return PlainTextResponse(str(response) + str(exc), status_code=400)

# @app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):

    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    # or logger.error(f'{exc}')
    print(request, exc_str)
    content = {'status_code': 10422, 'message': exc_str, 'data': None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)