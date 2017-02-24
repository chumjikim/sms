import json
import os

CUR_PATH = os.path.abspath(__file__)
SMS_TEST_PATH = os.path.dirname(CUR_PATH)
ROOT_PATH = os.path.dirname(SMS_TEST_PATH)
ROOT_ROOT_PATH = os.path.dirname(ROOT_PATH)
ROOT_ROOT_ROOT_PATH = os.path.dirname(ROOT_ROOT_PATH)
CONF_PATH = os.path.join(ROOT_ROOT_ROOT_PATH, '.conf')
REAL_CONF_PATH = os.path.join(CONF_PATH, 'settings_local.json')



def get_config():
    return json.loads(open(REAL_CONF_PATH).read())
