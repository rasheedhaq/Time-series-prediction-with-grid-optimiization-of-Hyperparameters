"""
Module: experiment_window_size.py
Description: Runs window size experiments for time-series prediction, following the structure of 1_3Wz.ipynb.
All configuration is loaded from src/config.py.
"""
import logging
import os
import sys
from src.config import LEARNING_RATE, EPOCHS, WINDOW_SIZE, BATCH_SIZE, OPTIMIZER, DATA_PATH, RESULTS_DIR, SEED

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def set_seeds(seed):
    np.random.seed(seed)
    tf.random.set_seed(seed)

def load_data(path):
    try:
        data = pd.read_csv(path)
        logger.info(f"Loaded data from {path} with shape {data.shape}")
        return data
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        sys.exit(1)

def build_model(input_shape, window_size):
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=input_shape),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE), loss='mse')
    return model

def run_window_size_experiment():
    set_seeds(SEED)
    data = load_data(DATA_PATH)
    # TODO: Add preprocessing, splitting, and experiment logic for window size
    logger.info("Experiment logic for window size goes here. Implement data split, model training, and result saving.")

if __name__ == "__main__":
    run_window_size_experiment()
