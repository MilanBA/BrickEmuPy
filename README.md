# BrickEmuPy
Handheld LCD games emulator in Python with PyQt6.<br/>

The following handheld games are currently emulated: 
* Brick Games
  * Brick Game E-23 PLUS MARK II 96 in 1 (HT-943D0) (An [article](https://habr.com/ru/articles/773040/) describing the reverse engineering.)
  * Brick Game E-88 8 in 1 (HT-943E5)
  * Brick Game E-33 2 in 1 (SC6383)
  * Block Game & Echo Key GA888 (Tetris Jr. clone) (HT-943I0)
  * Radio Shack Stack Challenge (C6246D2E)
  * Keychain 55 in 1 (HT-943I0)
  * Keychain GA-878 (BJ6220A)
  * Micon KC-32 (BJ6220A)
  * Apollo 128 in 1 B0202 (SPL02)
  * Apollo 18 in 1 B0302 (SPL03)
* Virtual Pets
  * Tamagotchi P1 (distributed without ROM)
  * Tamagotchi P2 (distributed without ROM)
  * Tamagotchi Mothra (distributed without ROM)
  * Tamagotchi Angel (distributed without ROM)
  * Tamagotchi Umino (distributed without ROM)
  * Tamagotchi Morino (distributed without ROM)
  * Tamagotchi Genjintch (distributed without ROM)
  * Tamagotchi Yasashii (distributed without ROM)
  * Digimon Ver. 1 (distributed without ROM)
  * Digimon Ver. 2 (distributed without ROM)
  * Digimon Ver. 3 (distributed without ROM)
  * Nikko virtual pet
  * Pocket Pikachu (distributed without ROM)
  * Mickey Deluxe Virtual Game virtual pet (HTGT43N0)
  * Apollo 2 in 1 virtual pet
  * Elfin Twins GM-021
* Other LCD Games
  * Epoch Chibi Pachi Alien Fever
  * Formel 1 (Hartung Spiele Berlin/Epoch)
  * The Legend of Zelda Game Watch (distributed without ROM)
  * Super Mario Bros. Game Watch (distributed without ROM)
  * Space Intruder TK-150I (HTB943R0)
  * Mame Game Tamagotch (HTGL43Q0) (distributed without ROM)
  * Mame Galaxian (HTB943R0) (distributed without ROM)
  * Keychain Pin Ball (HT-943I0)
  * Hiro Pocket Boy No.2
  * Gundam Space Combat 3 in 1 (Toshiba 6770S)
  * Epoch Monster Panic
  * Bandai Pengo (Toshiba 6941)
  * Gakken Jumping Boy / Pyonkichi / Lansay La Traversée (Toshiba T6813)
  * Bandai Power Fishing, 1984 (Toshiba 7790)
  * Gakken Soccer LCD Card Game, 1981 (Toshiba 6814)
  * Popy (Bandai) Animest Dorayaki House DO-01, 1983 (Toshiba 6922)
  * Popy (Bandai) Animest Parman Dai-Pinch PA-01, 1983 (Toshiba 6923)
  * Popy (Bandai) Animest Isoge! Doraemon DO-02, 1983 (Toshiba 6981)
  * Gakken Tom & Jerry Prank, 1983 (Toshiba 6909)
  * Animest (Bandai) Dr. Slump Arale Ncha! Bycha AR-03, 1982 (Toshiba 6815)

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
