# Starting kit Chalearn LAP Inpainting Competition Track 3 - Fingerprint Denoising and Inpainting

This starting kit contains the baseline model for this track to help you get started. A deep learning based baseline was used for reconstructing/enhancing the (degraded) fingerprint images with a standard deep neural network (DNN). To this end, a DNN was trained on the synthetic training set by minimizing the MSE loss function with Adam. The DNN comprises four convolutional layers, five residual blocks, two deconvolutional layers and another convolutional layer. Each of the five residual blocks comprises two convolutional layers. All of the layers except for the last layer are followed by batch normalization and rectified linear units. The last layer is followed by hyperbolic tangent units. The model is implemented in Chainer. **utils.py** contains the implementation of the model. See the raminder of this README for detailed instructions on how to use it.

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

Once the installation is complete, you can run the notebooks to train and validate the baseline model. That is:

**training-demo.ipynb** shows how to train a model by reconstructing training fingerprint images.
**validation-demo.ipynb** shows how to use a trained model to reconstruct validation fingerprint images.

Finally, we provide a sample submission file that can be used used as a reference for real submissions: **sample.zip**
