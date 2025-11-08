"""
Module: data_utils.py
Description: Data loading, preprocessing, and splitting utilities.
"""
import pandas as pd
import numpy as np
import logging
from sklearn.model_selection import train_test_split
from src.config import DATA_PATH, TRAIN_TEST_SPLIT, SEED

logger = logging.getLogger(__name__)

def load_data():
    try:
        data = pd.read_csv(DATA_PATH)
        logger.info(f"Loaded data from {DATA_PATH} with shape {data.shape}")
        return data
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        raise

def split_data(data, target_column):
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=1-TRAIN_TEST_SPLIT, random_state=SEED
    )
    logger.info(f"Split data: train {X_train.shape}, test {X_test.shape}")
    return X_train, X_test, y_train, y_test

# TODO: Add more preprocessing utilities as needed
