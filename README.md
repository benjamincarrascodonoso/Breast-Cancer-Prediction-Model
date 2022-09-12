# Patch Neural Network

## Datasets
Datasets available at: [Google Drive](https://drive.google.com/drive/folders/1Tp4iTFuz15J-UO11qs8TGPjHelQ1SVtk?usp=sharing).

We used the CBIS-DDSM dataset to get annotated images of mammography exams. There are 3101 annotated images for 1566 different patients, that can have calcification or masses, and these can be either benign or malignant.

The images were separated in a 85:15 rate to create independant training and test sets. The training data was further split in a 90:10 ratio to create an independant validation set. These splits were done in a stratified fashion to keep the same proportion of cancer cases in the trainig, validation and test sets.

Patch datasets were created by sampling images from ROIs and background regions. All patches were classified into one of the five categories: background, benign calcification, malignant calcification, benign mass and malignant mass.

### S1
The first dataset, S1, consisted of two patches of 224x224 per image, in which one was centered on the ROI and one is a random background patch from the same image

### S1-Big
S1-Big dataset follows the same rules as S1, but the patches now have size of 512x512, as we found that the mean size of the ROIs was bigger than 224x224.

### S10
The S10 dataset consisted of 10 patches randomly sampled from around each ROI, with a minimum overlapping ratio of 0.9 with the ROI, allowing for the inclusion of some background. It also sampled 10 patches from outside the ROI to get background images.


## Neural Network
A 3-stage training strategy was employed to train a Resnet using ImageNet pre-trained weights. The parameters learning start all frozen except for the FC layers at the end, and we progressively unfreeze the rest of the network as we train.

1. Set learning rate to 10^-3 and train the last layer for 3 epochs.
2. Set learning rate to 10^-4, unfreeze the top layers and train for 10 epochs. (Top layer number is set to 46 for Resnet)
3. Set learning rate to 10^-5, unfreeze all layers and train for 37 epochs for a total of 50 epochs.

In the above, an epoch is defined as a sweep through the training set. For both S1 and S1-Big datasets the number of epochs was increased to 200 epochs because it were much smaller datasets than S10. Adam was used as the optimizer and the batch size was set as 32.

## Weights
Trained weights are available at: [Google Drive](https://drive.google.com/drive/folders/1yfLSB6SSZougTDIc6-37pcZmPNBeVtmz?usp=sharing).

## Results 
Results can be found in the corresponding Notebook for Testing.
