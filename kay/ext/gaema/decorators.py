# -*- coding: utf-8 -*-

"""
kay.ext.gaema.decorators

:Copyright: (c) 2009 Takashi Matsuo <tmatsuo@candit.jp>
                     All rights reserved.
:license: BSD, see LICENSE for more details.
"""

import logging
from functools import update_wrapper

from werkzeug import redirect
from werkzeug.urls import url_quote_plus

from kay.utils import url_for
from kay.utils.decorators import auto_adapt_to_methods
from kay.ext.gaema.utils import (
  get_gaema_user, create_gaema_login_url
)
from kay.ext.gaema.services import (
  GOOG_OPENID, GOOG_HYBRID, TWITTER, FACEBOOK,
)

def create_inner_func_for_auth(func, *targets):
  def inner(request, *args, **kwargs):
    for service in targets:
      if get_gaema_user(service):
        return func(request, *args, **kwargs)
    return redirect(url_for('gaema/select_service', targets='|'.join(targets),
                            next_url=url_quote_plus(request.url)))
  return inner

def gaema_login_required(*targets):
  def outer(func):
    inner = create_inner_func_for_auth(func, *targets)
    update_wrapper(inner, func)
    return inner
  return auto_adapt_to_methods(outer)
