import os
import shutil
import csv
import numpy as np
import pandas as pd

from sprrep.constants import *
from sprrep.data import get_df_from_ibex_dir


# Global variables

# Get experiment data by munging horrible Ibex output
df = get_df_from_ibex_dir(IBEX_DIR)

if not os.path.exists('data'):
    os.makedirs('data')

df.to_csv(os.path.join('data', 'words.csv'), index=False)



