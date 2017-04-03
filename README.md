# restart_heroku_dyno
Code to deploy to a  "service" dyno, so that it restart a "target" dyno on a given period of time

# How to
* install the oauth plugin
`heroku plugins:install heroku-cli-oauth`
* Get the token from:
`heroku authorizations:create -d "API to restart the <dyno-name>"`
* Set the following env variables on the "service" dyno
    * `TOKEN_API` - the token from the previous step
    * `DYNO_NAME` - name of the target dyno e.g. "web" or "scraper"
    * `APP_ID` - the name of your target heroku app (the one containing the target dyno)
* Deploy the code from this repo to the service dyno.
* Add the [Scheduler add-on](https://elements.heroku.com/addons/scheduler) to the "service" dyno
* Try to see if restarting works
`heroku run python restart.py --app=<SERVICE APP>`
* Add a task to the scheduler which will run the script
`python restart.py`
* Voila
