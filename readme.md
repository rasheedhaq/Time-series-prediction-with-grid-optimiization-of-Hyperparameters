
# Water Quality Prediction for Smart Aquaculture Using Hybrid Deep Learning Models

This repository implements the experiments from the paper:

**K. P. Rasheed Abdul Haq and V. P. Harigovindan, "Water Quality Prediction for Smart Aquaculture Using Hybrid Deep Learning Models," IEEE Access, vol. 10, pp. 60078-60098, 2022.**  
DOI: [10.1109/ACCESS.2022.3180482](https://ieeexplore.ieee.org/document/9789166)

## Project Structure

- `src/` — All core Python modules (data, models, training, evaluation, experiments, config)
- `data/` — Input datasets (e.g., `dataieee.csv`)
- `notebooks/` — Original Jupyter notebooks for reference
- `results/` — Output results, plots, and CSVs
- `tests/` — Unit and integration tests
- `docs/` — Documentation and paper mapping

## Setup Instructions

1. Install Python 3.9.6 and required libraries:
	```bash
	pip install -r requirements.txt
	```
2. Place the dataset (`dataieee.csv`) in the `data/` folder.
3. Run experiments from the `src/experiments/` folder, e.g.:
	```bash
	python src/experiments/experiment_run_all.py
	```

## Code-to-Paper Mapping

| Paper Section / Experiment | Code Module / Script |
|---------------------------|----------------------|
| Learning Rate             | `experiment_learning_rate.py` |
| Epochs                    | `experiment_epochs.py` |
| Window Size               | `experiment_window_size.py` |
| Batch Size                | `experiment_batch_size.py` |
| Optimizer                 | `experiment_optimizer.py` |
| Model Definitions         | `src/models/models.py` |
| Data Handling             | `src/data/data_utils.py` |
| Training/Evaluation       | `src/training/training.py`, `src/evaluation/evaluation.py` |
| Main Orchestration        | `experiment_run_all.py` |

## Dataset

The dataset is from:
Liu J, Yu C, Hu Z, et al. "Accurate prediction scheme of water quality in smart mariculture with deep Bi-S-SRU learning network." IEEE Access, 2020, 8: 24784-24798.  
GitHub: https://github.com/xthzhjwzyc/Dataset-of-Prediction-of-Water-Quality

## Citation

If you use this code, please cite:
```
@ARTICLE{RA_HDL_WQP,
  author={Rasheed Abdul Haq, K. P. and Harigovindan, V. P.},
  journal={IEEE Access},
  title={Water Quality Prediction for Smart Aquaculture Using Hybrid Deep Learning Models},
  year={2022},
  volume={10},
  pages={60078-60098},
  doi={10.1109/ACCESS.2022.3180482}
}
```

## Environment

- Windows 10 (64-bit), Visual Studio Code IDE
- Python 3.9.6, Keras 2.6.0, Tensorflow 2.6.0
- Install dependencies from `requirements.txt`

---
For questions or contributions, please open an issue or pull request.


