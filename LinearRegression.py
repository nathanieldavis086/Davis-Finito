# Common imports
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib import cm
import numpy as np
import pandas as pd
import os as os
%matplotlib inline

mpl.rc('axes', labelsize= 14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

cmap = mpl.colormaps.get_cmap("jet")

# Where to save the figures
PROJECT_ROOT_DIR = "."
FOLDER = "figures"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, FOLDER)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

import pandas as pd

fileName = "MultipleLinearRegression.csv"

data = pd.read_csv(fileName) #read data

X = data[['x', 'y']].values.reshape(-1,2)
Y = data['z']

#range for each dimension

x = X[:, 0]
y = X[:, 1]
z = Y

data #this line prints the data

from mpl_toolkits import mplot3d

fig = plt.figure(figsize=[15,15]) 
#create figure

### ENTER CODE HERE ###

#add on the 4 subplots


#create a list of subplots


#loop through each element in list and perform the same actions
#adds on points with jet color described in the first code block for cmap
#adds labels with color


#correct angle per subplot



plt.tight_layout() #this is here to ensure it fits in the box below

save_fig("data scatter")
plt.show()
