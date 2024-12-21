import re

HEADER = re.compile('.*# (\d+)\. (.+)\.')
NAME_MAP = {
    'Prolific_ID': 'subject',
    'Order number of item': 'itemunique',
    'Value': 'word',
    'Parameter': 'sentpos',
    'EventTime': 'time',
    'Reading time': 'RT',
    'Item': 'item',
}
IBEX_DIR = 'ibex'
DATA_DIR = 'data'
PARTICIPANT_COL = 'subject'
ITEM_COL = 'item'

MB_COLS = [
    'sentid',
    'sentpos',
    'discid',
    'discpos',
    'startofsentence',
    'endofsentence',
    'rolled',
    'wlen',
    'unigramsurp',
    'totsurp',
    'fwprob5surp'
]
COLS = list(NAME_MAP.values()) + [
    'repetition_index', 'correct', 'question_response_timestamp', 'question_RT'
] + MB_COLS