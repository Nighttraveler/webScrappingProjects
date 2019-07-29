# -*- coding: utf-8 -*-

HOST_URL	= ''
EMAIL 		= ''
PASSWORD	= ''

'''
From https://mechanize.readthedocs.io/en/latest/advanced.html#logging

“mechanize”: Everything.
“mechanize.cookies”: Why particular cookies are accepted or rejected and why they are or are not returned. Requires logging enabled at the DEBUG level.
“mechanize.http_responses”: HTTP response body data.
“mechanize.http_redirects”: HTTP redirect information.

'''
LOG_EVERYTHING 		= 'mechanize'

LOG_COOKIES			= 'mechanize.cookies'

LOG_RESPONSE_BODY	= 'mechanize.http_responses'

LOG_REDIRECTS		= 'mechanize.http_redirects'