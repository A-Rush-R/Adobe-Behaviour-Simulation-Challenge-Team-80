df_company_path = r"problem_1_test_dataset\problem_1_test_dataset\behaviour_simulation_test_company.xlsx"

import pandas as pd
df_time = pd.read_excel(df_company_path)

from cleaner import master_cleaner

df_time = master_cleaner(df_time)

# df_time = df_time.iloc[6054:]
from utils import download_images
download_images(df_time,"time")
