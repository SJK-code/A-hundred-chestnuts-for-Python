import numpy as np

data = np.random.randint(0,5,(10,10))
print(data)
n=3
i = 1+(data.shape[0]-3)
j = 1+(data.shape[1]-3)
c = np.lib.stride_tricks.as_strided(data,shape=(i,j,n,n),strides=data.strides+data.strides)
print(c)