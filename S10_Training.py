import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pickle
from PIL import Image
from glob import glob

print('[INFO] Successfully imported libraries. Tensorflow version:', tf.__version__)
print('[DEBUG] Checking for GPU...', tf.config.list_physical_devices('GPU'))


# Get the dataset images to perform featurewise-centering (Zero mean images)
print('[INFO] Loading dataset images into memory')
X_train = []

dirs = glob('./datasets/S10/train/*/', recursive=True)
for dir in dirs:
    # Get only one patch from each image to not run out of memory for the .fit
    for infile in glob(dir + '*.png')[::10]:
        im = Image.open(infile)         # Loads in PIL format L (grayscale 8 bit)
        im = im.convert('RGB')          # Convert to RGB for fitting 
        X_train.append(np.array(im))

X_train = np.array(X_train)
print('[INFO] Dataset images loaded successfully. Training shape:', X_train.shape)


ROTATION_RANGE = 25
ZOOM_RANGE = 0.2
BRIGHTNESS_RANGE = [-20, 20]

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    featurewise_center=True,                 # Substract mean value of the training dataset
    rotation_range = ROTATION_RANGE,         # Rotations between [-25, 25] degrees
    zoom_range = ZOOM_RANGE,                 # Zooms in [0.8, 1.2] ratio
    brightness_range = BRIGHTNESS_RANGE,     # Intensify shift in [-20, 20] pixels
    horizontal_flip = True,
    vertical_flip = True
)
# Fit the train_datagen to calculate the training data mean rgb value
train_datagen.fit(X_train)

validation_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    featurewise_center=True,                 # Substract mean value of the training dataset
)
# Fit the validation_datagen on the training data
validation_datagen.fit(X_train)

train_generator = train_datagen.flow_from_directory(
    './datasets/S10/train/',
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical'
)
print('[INFO] Loaded Training Generator. Length:', len(train_generator))

validation_generator = validation_datagen.flow_from_directory(
    './datasets/S10/validation/',
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical'
)
print('[INFO] Loaded Validation Generator. Length:', len(validation_generator))

print('[INFO] Creating Resnet model')
resnet_model = tf.keras.models.Sequential()

pretrained_model = tf.keras.applications.ResNet50(
    include_top=False,          # Wether to include the fully-connected layer at the top of the network.
    input_shape=(224,224,3),    # Input shape tuple
    pooling='avg',              # Optional pooling mode for feature extraction when include_top is False. Average means that global average pooling will be applied to the output of the last convolutional block
    classes=5,                  # Number of classes to be classified
    weights='imagenet'          # Use pretrained ImageNet weights
    )

# Freeze the pre_trained model layers 
# From 0 to 175 layers
for layer in pretrained_model.layers:
    layer.trainable=False

resnet_model.add(pretrained_model)

# Connect the top layers (FC)
resnet_model.add(tf.keras.layers.Flatten())
resnet_model.add(tf.keras.layers.Dense(512, activation='relu'))
resnet_model.add(tf.keras.layers.Dense(5, activation='softmax'))

print('[INFO] Resnet model created. Summary:')
print(resnet_model.summary())

METRICS = [
    'accuracy',
    tf.keras.metrics.TruePositives(name='tp'),
    tf.keras.metrics.FalsePositives(name='fp'),
    tf.keras.metrics.TrueNegatives(name='tn'),
    tf.keras.metrics.FalseNegatives(name='fn'), 
    tf.keras.metrics.Precision(name='precision'),
    tf.keras.metrics.Recall(name='recall'),
    tf.keras.metrics.AUC(name='auc'),
    tf.keras.metrics.AUC(name='prc', curve='PR'), # precision-recall curve
]

resnet_model.compile(
    loss='categorical_crossentropy',
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=METRICS
    )

print('[INFO] Starting 3 epochs training')
history1 = resnet_model.fit(
    train_generator,
    steps_per_epoch = len(train_generator),
    epochs = 3,
    validation_data = validation_generator,
    validation_steps = len(validation_generator)
)
with open('./files/S10/History1Dict', 'wb') as file:
    pickle.dump(history1.history, file)


for layer in pretrained_model.layers[-46:]:
    layer.trainable=True

resnet_model.compile(
    loss='categorical_crossentropy',
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001),
    metrics=METRICS
    )

print('[INFO] Starting 10 epochs training')
history2 = resnet_model.fit(
    train_generator,
    steps_per_epoch = len(train_generator),
    epochs = 10,
    validation_data = validation_generator,
    validation_steps = len(validation_generator)
)

with open('./files/S10/History2Dict', 'wb') as file:
    pickle.dump(history2.history, file)


# Some Batch Normalization parameters depend on the median and std, so they are never trainable
# Set the whole model as trainable
resnet_model.trainable = True

# Change the learning rate to 10^-5
resnet_model.compile(
    loss='categorical_crossentropy',
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.00001),
    metrics=METRICS
    )
    
checkpoint = tf.keras.callbacks.ModelCheckpoint(
    filepath='./models/S10_model.h5',
    monitor='val_loss',
    save_best_only=True,
    verbose=1
)

print('[INFO] Starting 37 epochs training')
# Change number of epochs to 187, for a total of 200 epochs
history3 = resnet_model.fit(
    train_generator,
    steps_per_epoch = len(train_generator),
    epochs = 37,
    validation_data = validation_generator,
    validation_steps = len(validation_generator),
    callbacks=[checkpoint]
)

with open('./files/S10/History3Dict', 'wb') as file:
    pickle.dump(history3.history, file)
