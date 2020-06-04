# Copyright 2016 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf import settings
# bypass the djangooidc provided page and go directly to the keycloak page

# These URLs should be imported by the full Django app's settings and set
# LOGIN_URL and LOGOUT_URL, respectively.
#BOSSOIDC_LOGIN_URL = "/openid/openid/KeyCloak"
BOSSOIDC_LOGIN_URL = "/openid/authenticate"
BOSSOIDC_LOGOUT_URL = "/openid/logout/"

# DRF-OIDC-AUTH Configuration - Token based authentication
OIDC_AUTH = {
    'OIDC_ENDPOINT': None,
    'OIDC_AUDIENCES': [],
    'OIDC_RESOLVE_USER_FUNCTION': 'bossoidc.backend.get_user_by_id',
    'OIDC_BEARER_TOKEN_EXPIRATION_TIME': 4 * 10, # 4 minutes
}

def configure_oidc(auth_uri, client_id, public_uri, scope=None, client_secret=None):
    global OIDC_AUTH
    OIDC_AUTH['OIDC_ENDPOINT'] = auth_uri
    OIDC_AUTH['OIDC_AUDIENCES'] = [client_id]
