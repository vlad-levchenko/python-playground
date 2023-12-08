python --version
jupyter --version
pip --version

# To create a virtual environment run venv. 
# This will create a new virtual environment in a local folder venv
python -m venv venv

# activate a virtual environment
source venv/bin/activate

# check activated virtual environment
which python

# deactivate a virtual environment
deactivate

python -m pip install --upgrade pip
pip install scikit-learn

# https://www.tensorflow.org/install
pip install tensorflow

pip install pydot
sudo conda install graphviz

# launch jupyter notebook
jupyter-notebook


