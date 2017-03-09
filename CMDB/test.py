from saltjob.salt_https_api import salt_api_token
from saltjob.salt_token_id import token_id
from ops.settings import SALT_REST_URL

rs = salt_api_token({'fun': 'grains.items', 'tgt': '*'},
                    SALT_REST_URL, {'X-Auth-Token': token_id()}).CmdRun()['return']
print rs

