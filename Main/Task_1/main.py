import argparse
from utils import normalize_df,download_images
from cleaner import master_cleaner
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from batchGenerator import GetTensor
from media_proc import embed_df
import os

def main(dataset_path):
    # name = "time" #

    df = pd.read_excel(dataset_path)
    # df = df.iloc[:10]
    og_df = df.copy()

    working_df = df.copy()
    working_df = master_cleaner(working_df)
    download_images(working_df)
    working_df = embed_df(working_df)

    working_df = normalize_df(working_df)
    test_gen = GetTensor(working_df)

    saved_model_path = "Clip_model_62k.h5"
    model = load_model(saved_model_path)

    predictions = model.predict(test_gen)

    og_df['predicted_likes'] = predictions
    os.mkdir("results",exist_ok = True)
    og_df.to_csv("outputs/results.xlsx", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process dataset and make predictions.")
    parser.add_argument("dataset_path", type=str, help="Path to the dataset in Excel format.")
    args = parser.parse_args()

    main(args.dataset_path)
