# -*- coding: utf-8 -*-

"""
kay.ext.gaema.views

:Copyright: (c) 2009 Takashi Matsuo <tmatsuo@candit.jp> All rights reserved.
:license: BSD, see LICENSE for more details.

"""

from kay import exceptions
from kay.ext.gaema import (
  GoogleAuth, TwitterAuth, FacebookAuth, YahooAuth
)

GOOG_OPENID = 'goog_openid'
GOOG_HYBRID = 'goog_hybrid'
TWITTER = 'twitter'
FACEBOOK = 'facebook'
YAHOO = 'yahoo'

available_services = [
  GOOG_OPENID,
  GOOG_HYBRID,
  TWITTER,
  FACEBOOK,
  YAHOO,
]

auth_modules = {
  GOOG_OPENID: GoogleAuth,
  GOOG_HYBRID: GoogleAuth,
  TWITTER: TwitterAuth,
  FACEBOOK: FacebookAuth,
  YAHOO: YahooAuth,
}

verbose_names = {
  GOOG_OPENID: u'Google OpenID',
  GOOG_HYBRID: u'Google OpenID(Hybrid)',
  TWITTER: u'Twitter',
  FACEBOOK: u'Facebook',
  YAHOO: u'Yahoo OpenID',
}

def get_auth_module(service_name):
  return auth_modules[service_name]

def get_service_verbose_name(service_name):
  return verbose_names[service_name]

def register_gaema_service(key, auth_module, verbose_name):
  global available_services, auth_modules, verbose_names
  if key in available_services:
    raise exceptions.ImproperlyConfigured(
      'Service "%s" is already registered.' % key)
  available_services.append(key)
  auth_modules[key] = auth_module
  verbose_names[key] = verbose_name