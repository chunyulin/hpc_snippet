import numpy as np
import h5py as h5


#### Save H5
d1 = np.random.random(size = (1000,20))
d2 = np.random.random(size = (1000,200))
print (d1.shape, d2.shape)

hf = h5.File('data.h5', 'w')
hf.create_dataset('dataset_1', data=d1)
hf.create_dataset('dataset_2', data=d2)
hf.close()


#### Read H5
hf = h5.File('data.h5', 'r')
print(hf.keys())
n1 = hf.get('dataset_1')
n1 = np.array(n1)
print(n1.shape)

hf.close()