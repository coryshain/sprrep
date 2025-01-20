import re

HEADER = re.compile('.*# (\d+)\. (.+)\.')
NAME_MAP = {
    'Prolific_ID': 'subject',
    'Results reception time': 'acquisition_date',
    'Order number of item': 'item_unique',
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
    'repetition_index', 'correct', 'question_response_timestamp', 'question_RT', 'comp_q_bugfix'
] + MB_COLS