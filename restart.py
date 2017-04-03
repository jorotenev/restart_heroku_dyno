"""

"""
from os import getenv
from requests import delete
import logging

logging.basicConfig(level=logging.INFO)

# reference https://devcenter.heroku.com/articles/platform-api-reference#dyno-restart
heroku_api_url_template = "https://api.heroku.com/apps/{app_id}/dynos/{dyno_name}"
heroku_headers = {
    "Content-Type": "application/json",
    "Accept": "application/vnd.heroku+json; version=3"
}
heroku_successful_http_code = 202

token_api = getenv("TOKEN_API")
dyno_name = getenv("DYNO_NAME")
app_id = getenv("APP_ID")
assert token_api and dyno_name and app_id, "Mandatory env variables not set"

try:
    # construct the url for the request
    url = heroku_api_url_template.format(
        app_id=app_id,
        dyno_name=dyno_name
    )
    # make the HTTP request to heroku
    response = delete(url, headers=heroku_headers)
    # see if it was successful
    if response.status_code == heroku_successful_http_code:
        logging.info("API call for restart of dyno [{dyno}] successful")
        exit(0)
    else:
        error_msg = "API call failed with code {status_code}. Msg: {err_text}".format(status_code=response.status_code,
                                                                                      err_text=response.text)
        logging.critical(error_msg)
        exit(1)
except Exception as ex:
    logging.critical(str(ex))
    exit(1)
