import os
import json
import random

legendary = [1922, 6273, 6242, 8597]

images = os.listdir(f"./output/")

# run random
random.seed(232403)
random.shuffle(legendary)
random.shuffle(images)

for key in range(len(legendary)):
    print(f"Legendary {legendary[key]} : picture {images[key]}")