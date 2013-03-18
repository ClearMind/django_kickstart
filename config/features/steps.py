# -*- coding: utf-8 -*-

# Usage:
# python manage.py harvest [--no-server] -a config
#

from lettuce import step, world
from django.test import Client

@step(u'Given site page with URL "([^"]*)"')
def given_url(step, url):
    world.given_url = url


@step(u'When we send GET-request to given page')
def when_get(step):
    c = Client()
    world.status_code = c.get(world.given_url).status_code


@step(u'Then response must have code equals (\d+)')
def server_response_code(step, code):
    assert world.status_code == int(code), u'Get code %s, but %s' % (world.status_code, code)



