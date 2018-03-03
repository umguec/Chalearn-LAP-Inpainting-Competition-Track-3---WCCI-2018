## Requirements

### System
* Pyhton 3.6 version
* A suitable NVIDIA GPU, CUDA Toolkit and optionally cuDNN to run the code on a GPU

### Python
* chainer
* cupy
* fptrack
* h5py
* jupyter
* pillow
* protobuf
* python
* scikit-image
* scipy
* tqdm

The easiest way to get the starting kit up and running is with [Anaconda](https://anaconda.org/) (Pyhton 3.6 version). Once it is installed, you can follow the following steps:

- Create an environment and install requirements:

```
conda create -n fptrack h5py jupyter pillow protobuf python scikit-image scipy tqdm
```

- Activate the environment:

```
source activate fptrack
```

- Install the remaining requirements:

```
pip install chainer cupy
```

Note: If you want to run the code on a GPU, you must have a suitable NVIDIA GPU and install the CUDA Toolkit and optionally cuDNN.
