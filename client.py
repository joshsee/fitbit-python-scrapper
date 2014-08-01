__author__ = 'Josh'

import requests
from datetime import datetime
from datetime import timedelta
from pyquery.pyquery import PyQuery as pq

result_date = lambda d: d.strftime('%Y-%m-%d')


class FitBitScrapper(object):

    def __init__(self, email, password, verbose=False):
        self._session = requests.session()
        self._verbose = verbose
        self._login(email, password)

    def _log(self, msg):
        if self._verbose:
            print "  %s" % msg

    def _login(self, email, password):
        self._log("Logging in...")
        login_page = self._session.get('https://www.fitbit.com/login')
        form = pq(login_page.content).find('#loginForm')
        action = form.attr('action')
        data = dict((i.name, i.value) for i in form.find('input'))
        data.update({'email': email, 'password': password})
        self._session.post(action, data)

    def get_steps_on_date(self, date):
        self._log("Requesting date %s..." % result_date(date))
        payload = dict()
        payload['request'] = '{"template":"/mgmt/ajaxTemplate.jsp","serviceCalls":[{"name":"activityTileData","args":{"dataTypes":"steps","date":"%s"},"method":"getIntradayData"}]}' % result_date(date)

        self._log(payload)

        steps = self._session.post('https://www.fitbit.com/ajaxapi', data=payload)
        result = steps.text
        return result

    def get_steps_since_date(self, last_date):
        yesterday = datetime.now() - timedelta(1)
        current = datetime(yesterday.year, yesterday.month, yesterday.day)
        result = {}
        while current > last_date:
            steps = self.get_steps_on_date(current)
            result[result_date(current)] = steps
            current = current - timedelta(days=1)
        return result