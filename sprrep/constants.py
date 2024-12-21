import re

HEADER = re.compile('.*# (\d+)\. (.+)\.')
NAME_MAP = {
    'Prolific_ID': 'subject',
    'Order number of item': 'sentid',
    'id': 'subject',
    'Value': 'word',
    'Parameter': 'sentpos',
    'EventTime': 'time',
    'Reading time': 'RT'
}
IBEX_DIR = 'ibex'
DATA_DIR = 'data'
PARTICIPANT_COL = 'subject'
ITEM_COL = 'sentid'