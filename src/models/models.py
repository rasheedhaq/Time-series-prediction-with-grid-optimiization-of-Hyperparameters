"""
Module: models.py
Description: Contains model definitions for all DL/ML models used in the experiments, following the structure of 3.io_Models_Order.ipynb.
"""
import tensorflow as tf
from tensorflow import keras

def build_dense_model(input_shape, learning_rate):
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=input_shape),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate), loss='mse')
    return model


def build_lstm_model(input_shape, learning_rate):
    model = keras.Sequential([
        keras.layers.LSTM(64, activation='tanh', input_shape=input_shape, return_sequences=False),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate), loss='mse')
    return model

def build_gru_model(input_shape, learning_rate):
    model = keras.Sequential([
        keras.layers.GRU(64, activation='tanh', input_shape=input_shape, return_sequences=False),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate), loss='mse')
    return model

def build_bilstm_model(input_shape, learning_rate):
    model = keras.Sequential([
        keras.layers.Bidirectional(keras.layers.LSTM(64, activation='tanh', return_sequences=False), input_shape=input_shape),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate), loss='mse')
    return model

def build_cnn_model(input_shape, learning_rate):
    model = keras.Sequential([
        keras.layers.Conv1D(64, kernel_size=3, activation='relu', input_shape=input_shape),
        keras.layers.Flatten(),
        keras.layers.Dense(1)
    ])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate), loss='mse')
    return model
