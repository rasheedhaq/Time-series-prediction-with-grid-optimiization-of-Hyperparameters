# Configuration file for time-series prediction project

# Data paths
DATA_PATH = "data/dataieee.csv"
RESULTS_DIR = "results/"

# Model hyperparameters (default values, can be overridden)
LEARNING_RATE = 0.0008
EPOCHS = 10
WINDOW_SIZE = 10
BATCH_SIZE = 64
OPTIMIZER = "Adam"
TRAIN_TEST_SPLIT = 0.8

# Random seed
SEED = 42

# Logging
LOG_LEVEL = "INFO"

# Add more config variables as needed
