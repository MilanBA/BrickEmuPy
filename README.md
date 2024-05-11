# BrickEmuPy
Brick Game (aka Tetris) emulator in Python with PyQt6.<br/>

The following handheld games are currently emulated: 
* E-23 PLUS MARK II 96 in 1
* GA888 (Tetris Jr. clone)
* Space Intruder TK-150I
* Radio Shack Stack Challenge

An [article](https://habr.com/ru/articles/773040/) describing the reverse engineering.

## Compiling
Tested with Ubuntu 24.
```
sudo apt install pip
pip install pyqt6 --break-system-packages
git clone https://github.com/azya52/BrickEmuPy && cd BrickEmuPy
python3 main.py
```

<img src="https://github.com/azya52/BrickEmuPy/assets/31337838/65dc8c6c-7998-48c9-b351-383522dd8171" width=100%>
<img src="https://github.com/azya52/BrickEmuPy/assets/31337838/d8c25a9f-c2df-4ae0-add2-3d3134eb6a5e" width=100%>
