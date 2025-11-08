"""
Module: experiment_run_all.py
Description: Main entry point to run all experiments, following the structure of 1.run_all.ipynb.
All configuration is loaded from src/config.py.
"""
import logging
from src.experiments import experiment_learning_rate, experiment_epochs, experiment_window_size, experiment_batch_size, experiment_optimizer

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def run_all_experiments():
    logger.info("Running learning rate experiment...")
    experiment_learning_rate.run_learning_rate_experiment()
    logger.info("Running epochs experiment...")
    experiment_epochs.run_epochs_experiment()
    logger.info("Running window size experiment...")
    experiment_window_size.run_window_size_experiment()
    logger.info("Running batch size experiment...")
    experiment_batch_size.run_batch_size_experiment()
    logger.info("Running optimizer experiment...")
    experiment_optimizer.run_optimizer_experiment()
    logger.info("All experiments completed.")

if __name__ == "__main__":
    run_all_experiments()
