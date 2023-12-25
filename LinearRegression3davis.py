# Common imports
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib import cm
import numpy as np
import pandas as pd
import os

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

print(data) #this line prints the data




from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import axes3d
import numpy as np


fig = plt.figure(figsize=[15,15])

#create figure DONE

#add on the 4 subplots
#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1=plt.subplot(221, projection='3d')
ax2=plt.subplot(222, projection='3d')
ax3=plt.subplot(223, projection='3d')
ax4=plt.subplot(224, projection='3d')



#create a list of subplots
xdata=[x]
ydata=[y]
zdata=[z]

ax=[ax1,ax2,ax3,ax4]

#loop through each element in list and perform the same actions

#adds on points with jet color described in the first code block for cmap
#adds labels with color
ax1.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')
ax2.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')
ax3.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')
ax4.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')

#correct angle per subplot
ax1.set_xlabel("x",size=15,color="red")
ax2.set_xlabel("x",size=15,color="red")
ax3.set_xlabel("x",size=15,color="red")
ax4.set_xlabel("x",size=15,color="red")
ax1.set_ylabel("y",size=15,color="red")
ax2.set_ylabel("y",size=15,color="red")
ax3.set_ylabel("y",size=15,color="red")
ax4.set_ylabel("y",size=15,color="red")

ax1.view_init(0,90)
ax2.view_init(40,0)
ax3.view_init(35,45)
ax4.view_init(10,20)

plt.tight_layout() #this is here to ensure it fits in the box below

save_fig("data scatter")
plt.show()


from sklearn.linear_model import LinearRegression
model=LinearRegression().fit(X,Y)

print(f"Model Coefficients: {model.coef_}")
print("Model Intercept: ", model.intercept_,)
print()

# Plot Curve Fit
x_fit = np.linspace(0,21,1000)
y_fit = x_fit

z_fit = model.predict(np.array([x_fit, y_fit]).T) ##must pass both features as Data Frame

print(z_fit)




fig2 = plt.figure(figsize=[15,15])
#fig = plt.figure()
ax1=plt.subplot(221, projection='3d')
ax2=plt.subplot(222, projection='3d')
ax3=plt.subplot(223, projection='3d')
ax4=plt.subplot(224, projection='3d')
### ENTER CODE HERE ###
xline = x_fit
yline = y_fit
zline = z_fit

ax1.plot3D(xline, yline, zline, 'black')
ax2.plot3D(xline, yline, zline, 'black')
ax3.plot3D(xline, yline, zline, 'black')
ax4.plot3D(xline, yline, zline, 'black')

ax1.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')
ax2.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')
ax3.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')
ax4.scatter3D(xdata, ydata, zdata, c=zdata, cmap='jet')

#correct angle per subplot
ax1.set_xlabel("x",size=15,color="red")
ax2.set_xlabel("x",size=15,color="red")
ax3.set_xlabel("x",size=15,color="red")
ax4.set_xlabel("x",size=15,color="red")
ax1.set_ylabel("y",size=15,color="red")
ax2.set_ylabel("y",size=15,color="red")
ax3.set_ylabel("y",size=15,color="red")
ax4.set_ylabel("y",size=15,color="red")

ax1.view_init(0,90)
ax2.view_init(40,0)
ax3.view_init(35,45)
ax4.view_init(10,20)

##rotations of each subplot



plt.tight_layout() #this is here to ensure it fits in the box below

save_fig("Multiple Linear Regression") #name of file
plt.show()

print("True Model Coefficients: ", np.round(model.coef_))
print("True Model Intercept : ", np.round(model.intercept_))