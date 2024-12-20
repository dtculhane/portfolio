Image Classification with CNN README
David Culhane

This project looks to create a Convolutional Nueral Network (CNN) to classify images from MNIST. The script uses the torch and torchvision libraries in Python and follows a template from Machine Learning with Python Cookbook by Kyle Gallatin and Chris Albon. It has been the only work, so far, I have done with respect to neural network models.

The script begins by printing some of the images from the MNIST dataset containing numbers. The dataset is a sample dataset included with the torchvision library. The convolutional layers in the model learn the features of the numbers in the images. The poling layer reduces dimensiolaity by filtering. Then the fully connected layer uses a softmax activation to rank the possible classifications for the image fed into the CNN.