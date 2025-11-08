"""
Module: training.py
Description: Training utilities for model fitting and callbacks.
"""
import logging
from tensorflow import keras

logger = logging.getLogger(__name__)

def train_model(model, X_train, y_train, X_val=None, y_val=None, epochs=10, batch_size=32):
    callbacks = [
        keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
    ]
    validation_data = (X_val, y_val) if X_val is not None and y_val is not None else None
    history = model.fit(
        X_train, y_train,
        validation_data=validation_data,
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=1
    )
    logger.info("Model training complete.")
    return history

# TODO: Add more training utilities as needed
