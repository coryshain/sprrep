import os
try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources
import pandas as pd

from sprrep.constants import *
from sprrep.data import get_df_from_ibex_dir
from sprrep import resources


# Get experiment data by munging horrible Ibex output
df = get_df_from_ibex_dir(IBEX_DIR)
df = df.sort_values([PARTICIPANT_COL, 'time', ITEM_COL, 'sentpos'])

# Timestamp things
# Events are timestamped relative to the END of each SPR trial. Fix this.
# 1. Get trial durations
df['item_end'] = df.time
df['item_duration'] = df.groupby([PARTICIPANT_COL, ITEM_COL])['RT'].transform('sum')
# 2. Subtract trial durations from timestamps
df.time -= df.item_duration
# 3. Compute word onsets from RT cumsums
df.time += df.groupby([PARTICIPANT_COL, ITEM_COL]).RT.\
    transform(lambda x: x.cumsum().shift(1, fill_value=0))
# 4. Subtract out the minimum timestamp to make timestamps relative to expt start
df['expt_start'] = df.groupby(PARTICIPANT_COL)['time'].transform('min')
df.time -= df.expt_start
df.question_response_timestamp -= df.expt_start
df.item_end -= df.expt_start
# 5. Get question RTs
df['question_RT'] = df.question_response_timestamp - df.item_end
# 6. Rescale to seconds
df.time /= 1000
df.question_response_timestamp /= 1000

# Add acquisition date (useful for catching repeat participants)
df.acquisition_date = pd.to_datetime(df.acquisition_date, unit='ms')

# Add repetition index
df_by_item = df[[PARTICIPANT_COL, ITEM_COL, 'item_unique']].drop_duplicates([PARTICIPANT_COL, 'item_unique'])
df_by_item['repetition_index'] = df_by_item.groupby([PARTICIPANT_COL, ITEM_COL]).cumcount() + 1
df = pd.merge(df, df_by_item, on=[PARTICIPANT_COL, ITEM_COL, 'item_unique'], how='left')

# Merge in modelblocks predictors
df['sentid'] = df[ITEM_COL] - 1
with pkg_resources.as_file(pkg_resources.files(resources).joinpath(
        'repetition.wsj02to21-gcg15-nol-prtrm-3sm-synproc-+c_+u_+b5000_parsed.unigram.5-kenlm.all-itemmeasures'
)) as path:
    df_items = pd.read_csv(path, sep=' ')[MB_COLS]
df = pd.merge(df, df_items, on=['sentid', 'sentpos'], how='left')

df = df[COLS]

if not os.path.exists('data'):
    os.makedirs('data')
df.to_csv(os.path.join('data', 'words.csv'), index=False)



