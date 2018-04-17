#!/usr/bin/python3.5
# Author: xiaojie

class BaseConfig(object):
    DEBUG = False
    SESSION_REFRESH_EACH_REQUEST = True


class TestConfig(BaseConfig):
    DEBUG = True
    secret_key = "helloworld"

class DevConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    pass

"""
{
'DEBUG':                                get_debug_flag(default=False),  是否开启Debug模式
'TESTING':                              False,                          是否开启测试模式
'PROPAGATE_EXCEPTIONS':                 None,                          
'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
'SECRET_KEY':                           None,
'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
'USE_X_SENDFILE':                       False,
'LOGGER_NAME':                          None,
'LOGGER_HANDLER_POLICY':               'always',
'SERVER_NAME':                          None,
'APPLICATION_ROOT':                     None,
'SESSION_COOKIE_NAME':                  'session',
'SESSION_COOKIE_DOMAIN':                None,
'SESSION_COOKIE_PATH':                  None,
'SESSION_COOKIE_HTTPONLY':              True,
'SESSION_COOKIE_SECURE':                False,
'SESSION_REFRESH_EACH_REQUEST':         True,
'MAX_CONTENT_LENGTH':                   None,
'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
'TRAP_BAD_REQUEST_ERRORS':              False,
'TRAP_HTTP_EXCEPTIONS':                 False,
'EXPLAIN_TEMPLATE_LOADING':             False,
'PREFERRED_URL_SCHEME':                 'http',
'JSON_AS_ASCII':                        True,
'JSON_SORT_KEYS':                       True,
'JSONIFY_PRETTYPRINT_REGULAR':          True,
'JSONIFY_MIMETYPE':                     'application/json',
'TEMPLATES_AUTO_RELOAD':                None,
}
"""