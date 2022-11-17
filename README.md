# OPENGUI
This repository contains the necessary files
to use the OPENGUI with the OPEN package.

Development log: https://gregorjmathieson.github.io/OPEN_GUI_Devlog/

Video Tutorials: https://gregorjmathieson.github.io/OPEN_GUI_Devlog/webhelp.html

OPEN Platform for Energy Networks: https://open-platform-for-energy-networks.readthedocs.io/en/latest/

## Requirements
--------------------------------------------------
* Python 3
* numba
* numpy
* pandapower
* pandas
* PICOS
* scikit-learn
* scipy
* spyder
* spyder-kernels
* cvxopt
* matplotlib
* wxpython

(See requirements.txt)

If using conda:

```
conda config --add channels invenia
conda config --add channels picos
conda config --add channels conda-forge
```

Creating a virtual environment:

```
conda create --name <env_name> --file requirements.txt python=3.6
```

## Installation
--------------------------------------------------
If installing into an existing installation of OPEN,
the OPENGUI files must be dragged and dropped into the directory where OPEN is.

Note that the "System" directory must REPLACE the System directory in OPEN.

## QuickStart
--------------------------------------------------
To open the GUI, run the OPENGUI_main.py file.
