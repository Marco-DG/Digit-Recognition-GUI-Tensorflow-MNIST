# Digit Recognition on Tensorflow using MNIST with GUI

![Here a Screenshot!!](https://github.com/Marco-DG/Tensorflow-MNIST-digit_recognition/blob/master/Screenshot.png)

### Hi
Hi, I'm a 17-year-old student in florence, Italy; my IT professor ask to the class to find a project to develop during the year            and I've chosen this one. I love programming in Python and C++ and is a year now since I began to study machine-learning and  neural networks.

### License
 
The software is distribuited under an Apache 2 license so feel free to use it as you want :)

### Requirements

The script has been written with Python3 but shoud be compatible with Python2 too, the list of used packages that you have to install can be found in `install_requirements.bat`, if you are using Windows you can just execute the script, but I recommend you to use a `virtual-env` to ensure safety.

```
pip3 install tensorflow
pip3 install opencv-python
pip3 install pillow
pip3 install pygame
pip3 install numpy
```

## Running the script

```
python3 Main.py
```

### Running the script for the first time

The first time you will run the script, the **training will start** this **could take a couple of hours**, once finished the Tensorflow model will be saved in the same folder of the script, 3 or 4 file will be saved: `checkpoint`, `model.ckpt.index`, `model.ckpt.meta` and `model.ckpt.data-00000-of-00001`.

**Note:** As long as the `model.ckpt` is stored in the folder, the next time you will run the `Main.py` the training will be avoided.

## Project Tree

```
- Main.py
- whoDaresWins.py
- generateClassifier.py
- performRecognition.py
- prepareImage.py
- install_requirements.bat
- /font/FreeSans.ttf
```
