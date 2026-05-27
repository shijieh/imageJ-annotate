import os
import numpy as np
import matplotlib.pyplot as plt
# %% load manual clicking data
X_manual = np.loadtxt('manual_clicking_data.csv', 
                      delimiter=',')[:, 0]

Y_manual = np.loadtxt('manual_clicking_data.csv', 
                      delimiter=',')[:, 1]

# %% load data generated from Fiji
X_fiji  = np.genfromtxt('Fiji_data.csv',
                     delimiter=',', 
                     skip_header=1)[:, 3]

Y_fiji  = np.genfromtxt('Fiji_data.csv',
                     delimiter=',', 
                     skip_header=1)[:, 4]

Area    = np.genfromtxt('Fiji_data.csv',
                     delimiter=',', 
                     skip_header=1)[:, 2]

# %% visualize
fig, ax = plt.subplots(figsize=(15, 15))
plt.rc('font', size=20) 
# the raw picture used in Fiji
image_raw = plt.imread('raw_picture.jpg')
ax.imshow(image_raw,
          alpha = 1)

# manual data
ax.scatter(X_manual, Y_manual , 
           s         = 20     , 
           c         = 'blue' ,
           marker    = 'o'    ,
           alpha     = 1      ,
           label = 'Manual'
           )

# Fiji data
ax.scatter(X_fiji, Y_fiji      , 
           s         =  20     ,
           # s         = Area/5  , 
           edgecolor = 'red'   ,
           facecolor = 'none'  ,
           alpha     = 0.5     ,
           label='Cell Counter'
           )

# cosmetics
ax.set_xlim(0,    2300)
ax.set_ylim(2300, 0)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

lgd = ax.legend()
# 
fig.savefig('annotation.png')
plt.show()
