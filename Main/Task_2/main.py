## Importing packages
import pandas as pd
from DataCleaning import master_clean
from master import master_try
from utils import get_prompt
from captioning import get_captions

### Loading the dataset
dataset_path = "content_simulation_train.xlsx"
df = pd.read_excel(dataset_path)
df = master_clean(df)

df['caption'] = get_captions(df)
df['prompt'] = df.apply(get_prompt,axis = 1)

df = master_try(df)

df.to_csv("Submission.csv")