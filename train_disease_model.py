import os
import random
import shutil
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

# Paths
original_dataset = "ml_models/train"
sampled_dataset = "ml_models/sample_dataset"

# Limit images per class
MAX_IMAGES = 300

print("Preparing dataset...")

# Create sampled dataset
if os.path.exists(sampled_dataset):
    shutil.rmtree(sampled_dataset)

os.makedirs(sampled_dataset)

for class_name in os.listdir(original_dataset):

    class_path = os.path.join(original_dataset, class_name)

    if not os.path.isdir(class_path):
        continue

    new_class_path = os.path.join(sampled_dataset, class_name)

    os.makedirs(new_class_path)

    images = os.listdir(class_path)

    selected_images = random.sample(
        images,
        min(MAX_IMAGES, len(images))
    )

    for img in selected_images:

        src = os.path.join(class_path, img)

        dst = os.path.join(new_class_path, img)

        shutil.copy(src, dst)

print("Dataset prepared")

# Image settings
IMG_SIZE = (224, 224)
BATCH_SIZE = 16

datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    sampled_dataset,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

val_data = datagen.flow_from_directory(
    sampled_dataset,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)

print("Building model...")

base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False

model = models.Sequential([
    base_model,

    layers.GlobalAveragePooling2D(),

    layers.Dense(128, activation="relu"),

    layers.Dense(
        train_data.num_classes,
        activation="softmax"
    )
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("Training started...")

model.fit(
    train_data,
    validation_data=val_data,
    epochs=5
)

model.save(
    "ml_models/disease_model/model.h5"
)

print("Training completed")