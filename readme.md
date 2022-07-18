This is time-series prediction work. In this work, we have a set of experiments starting by using different models, on various parameters, with different optimizers for each experiment. To do all these experiments together in single run. This code is divided into three layers. In level 1, we adjust the optimizers. In level 2, we input the specific parameter to be output, and in level 3, we implement all the models which need to be tested for this experiment. Level 0 is the code which is the starting point, and it's the only code which we have to run to complete this experiment.

Level 0 - 1.run_all.ipynb - This is the only code we have to run. All other codes will be called from inside this code.
Level 1 - 1_1Lr.ipynb, 1_2Epochs.ipynb, 1_3Wz.ipynb, 1_4Bz.ipynb, 1_5Opz.ipynb - These codes will be called by 1.run_all.ipynb one by one.
Level 2 - 2.io_Loop_4WQP.ipynb - This code gives the parameter to be used in that experiment. This code will be called from each of the codes in level 1 
Level 3 - 3.io_Models_Order.ipynb - All the DL/ML models are defined in this code. (Also, some code for plotting the figures, storing values to CSV, splitting of data etc is also done inside this code)

1.Lr_vs_RMSE, 2.Ep_vs_RMSE, 3.Wz_vs_RMSE, 4.Bz_vs_RMSE, 5.Opz_vs_RMS, n - These folders for saving the results of different experiments and codes inside them are used to plot the results of each experiment. n - is a folder for storing some of the common results. All the results, both plots in pdf and CSV files, are named properly, so calling the to a latex file is very easy.
For example, "1.ALL_Results_l0008_S8020_e10_wz10_b64_Adam_IEEE.csv" has all the results with l0008 indicating learning rate = 0.0008, S8020 - meaning data was split 80:20 for training and testing, wz10 - indicates the window size is 10, b64 - indicates the batch size is 64, Adam the optimizer used, IEEE suggests the dataset used. In our work, we have used two datasets. Naming is straightforward for all files and uses the same logic.

The code is not commented completly but its straigh forward and understandable. 

If you use this code, please cite our work: Water Quality Prediction for Smart Aquaculture Using Hybrid Deep Learning Models.
K. P. Rasheed Abdul Haq and V. P. Harigovindan, "Water Quality Prediction for Smart Aquaculture Using Hybrid Deep Learning Models," in IEEE Access, vol. 10, pp. 60078-60098, 2022.
@ARTICLE{RA_HDL_WQP,  author={Rasheed Abdul Haq, K. P. and Harigovindan, V. P.},   journal={IEEE Access},   title={Water Quality Prediction for Smart Aquaculture Using Hybrid Deep Learning Models},   year={2022},   volume={10},   number={},   pages={60078-60098},   doi={10.1109/ACCESS.2022.3180482}}

dataieee.csv provided here is the dataset used in this work which is an openly available dataset. If you are using this data, please cite their paper: An Accurate Prediction of Water Quality in Smart Mariculture with Improved SRU Deep Learning Network. Liu J, Yu C, Hu Z, et al. Accurate prediction scheme of water quality in smart mariculture with deep Bi-S-SRU learning network[J]. IEEE Access, 2020, 8: 24784-24798.

@article{liu2020accurate, title={Accurate prediction scheme of water quality in smart mariculture with deep Bi-S-SRU learning network}, author={Liu, Juntao and Yu, Chuang and Hu, Zhuhua and Zhao, Yaochi and Bai, Yong and Xie, Mingshan and Luo, Jian}, journal={IEEE Access}, volume={8}, pages={24784--24798}, year={2020}, publisher={IEEE} }

https://github.com/xthzhjwzyc/Dataset-of-Prediction-of-Water-Quality

The software environment Windows 10 (64-bit) operating system, Visual studio code IDE, and we have implemented the neural network model using Python 3.9.6, Keras 2.6.0 and Tensorflow 2.6.0. Please install the libraries in requirements.txt for the code to run without errors. Correct versions of python is available online and in the provided onedrive link :https://1drv.ms/u/s!AgUEZUwHCn6Bgr5OC99WbgyMFbDBJQ?e=beP0TK


