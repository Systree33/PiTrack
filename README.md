# PiTrack

This is for use with [Sense hat B](https://www.waveshare.com/wiki/Sense_HAT_(B))

## Instructions:

Install:

Follow instructions to enable I2C [Here](https://www.waveshare.com/wiki/Sense_HAT_(B)#Open_I2C_Interface)

```
sudo apt update

sudo apt install python3-pip 
sudo apt install python3-spidev
sudo apt install python3-smbus

pip install scipy
pip install numpy
pip install matplotlib
pip install pygame
```

Run:
```
python3 Logger.py
python3 Visualise.py
```
