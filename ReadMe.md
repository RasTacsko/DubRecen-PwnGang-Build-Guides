# Pwnagotchi Build Guide

## Description:
Notes for building my pwnagotchis
Last Updated: 2023 June

**Content:**
- Build instructions
- Plugin list
- Hardware list
- My setups

## Build Instructions

[**PLEASE REFER TO THE UNOFICCIAL PWNAGOTCHI SITE!**](http://https://pwnagotchi.org/ "PLEASE REFER TO THE UNOFICCIAL PWNAGOTCHI SITE!")

- **Step 1) Download the pwnagotchi image**
I use [**Jayofelonys repo**](https://github.com/jayofelony/pwnagotchi/releases/tag/v2.8.9 "Jayofelonys repo"). It is under active development based on the community feedback and updated frequently with bugfixes, new features, and supports more than 80 screens.

- **Step 2) Flash pwnagotchi image to microSD**
*Note: Recommended to use **[Raspberry Imager](https://www.raspberrypi.com/software/ "Raspberry Imager")** to flash the image.*
Several tutorials exist online (Google or YouTube) that provide instructions for flashing an image to a microSD.
Before flashing the image I use the Raspberry Imager, to set the timezone, and change the default user/password for the OS.

- **Step 3) Build your initial config.toml**
Your initial config.toml will contain the baseline configuration for your pwnagotchi, such as the name of the device. It is recommended to avoid trying to configure all of your plugins at this stage, and only focus on the essential plugins, such as bt-tether.

		#start of config.toml
		#end of config.toml

- **Step 4) Copy config.toml to MicroSD (boot)**
*Note: If you removed, insert the microSD card flashed in Step 3.*
Open the new drive titled "boot", and copy over your config.toml

- **Step 5) If you are using an SPI LCD screen with Pi3 or Pi0, you may have to modifiy the config.txt.**
For jays image since 2.8.7 until now, there is some issue with the SPI chip select stuff.
If your screen is not showing any image, but the backlight is on, you should modify the **/boot/firmware/config.txt**, and change ***dtoverlay=spi0-0cs*** to ***dtoverlay=spi0-1cs*** under the necessary pi settings.
*Note: if you are sure that you need to modify the config.txt, you can do it after flashing the card. The config.txt is directly in the cards boot partition.*

- **Step 6) Boot pwnagotchi for the first time WARNING: BE PATIENT.**
The First boot will take longer than average due to key generation.
NOTE: If you specified settings for bt-tether plugin, ensure your mobile device is nearby and listening for new bluetooth devices to pair. Ensure Internet sharing via Personal Hotspot is enabled. Your mobile device will be prompted to pair with your pwnagotchi.

- **Step 7) Bluetooth connection manually**
SSH in (default login: pi, pw: raspberry)
		sudo bluetoothctl
		scan on
	Wait until your phones mac address shows up
	Copy your phoes mac address
		pair MA: CA: DD: RE: SS
		trust MA: CA: DD: RE: SS
		exit

- **Step 8) Change all the default passwords**
If you haven't done it with the Raspberry Imager, change "pi" password. Default "raspberry"
*passwd*
Change "root" password:
*sudo passwd root*
If you haven't done it when creating your config.toml file, change pwnagotchi Web UI password. Default is "changeme"
*sudo nano /etc/pwnagotchi/config.toml*
Locate and update the values for:
ui.web.username = "changeme"
ui.web.password = "changeme"
Update bettercap password, if you want to. Default is "pwnagotchi"
*sudo nano /etc/pwnagotchi/config.toml*
locate and update the values for:
bettercap.username = "pwnagotchi"
bettercap.password = "pwnagotchi"
*sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-auto.cap*
modify the bettercap username & password to match config.toml
*sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-manual.cap*
modify the bettercap username & password to match config.toml
sudo systemctl restart pwnagotchi.service
reload pwnagotchi for config changes to apply.

- Step 9) Install plugins
Consider this step OPTIONAL, unless you would like these custom plugins. Otherwise, proceed to Step 10. 
Make custom-plugins directory defined in config.toml, if not done so already.
cd ~ sudo mkdir /usr/local/share/pwnagotchi/installed-plugins/

- Step - 9.1) Default plugins I use:
	- 	auto-update
	- 	bt-tether
	- 	fix-services
	- 	gdrivesync*
	- 	gpio_buttons*
	- 	grid
	- 	logtail
	- 	memtemp
	- 	onlinehashcrack
	- 	session-stats
	- 	webcfg
	- 	webgpsmap
	- 	wpa-sec

- Step 9.2) 3rd party plugins:
	- Clock
	- PiSugar3
	- Poweruitls
	- Pwnmenu
	- Custom Faces
	- Tweak View
	- Fancygotchi*
	- GPSD Easy
	- Wardriver
	- Aircrackonly
	- Enable deauth / Enable Assoc / Touch UI*
	- Instattack
	- EXP V2
	- Achievement*
	- Shower Thoughts*

Plugins marked with * are not tested by me yet, or needs some tweaking to work on my setup.
Details soon


- Step 10) Back up all your hard work! Download the Backup script from Github.
Link: https://github.com/evilsocket/pwnagotchi/blob/master/scripts/backup.sh
Append the "FILES_TO_BACKUP" section of the backup script to include the following additional files that have been added or modified as a result of this guide:

	FILES_TO_BACKUP="/root/brain.nn \
	  /root/brain.json \
	  /root/.api-report.json \
	  /root/.ssh \
	  /root/.bashrc \
	  /root/.profile \
	  /root/handshakes \
	  /root/peers \
	  /etc/pwnagotchi/ \
	  /etc/ssh/ \
	  /var/log/pwnagotchi.log \
	  /var/log/pwnagotchi*.gz \
	  /home/pi/.ssh \
	  /home/pi/.bashrc \
	  /home/pi/.profile \
	  /root/.api-report.json \
	  /root/.auto-update \
	  /root/.bt-tether* \
	  /root/.net_pos_saved \
	  /root/.ohc_uploads \
	  /root/.wigle_uploads \
	  /root/.wpa_sec_uploads \
	  /usr/bin/pwnlib \
	  /etc/systemd/system/pwngrid-peer.service \
	  /usr/local/share/pwnagotchi/custom-plugins \
	  /usr/local/lib/python3.11/dist-packages/pwnagotchi"
Note: The last entry in the list must include an end quotation mark. Be sure to relocate this to the end of the list before saving.
sudo chmod +x backup.sh # make backup.sh executable sudo ./backup.sh

Enjoy your new Pwnagotchi, and please support the Pwnagotchi community on Reddit and Discord!

### Hardware list:
- **Boards:**
	- Raspberry Pi
		- 0W
		- 0W2
		- 3B
		- 3A+
- **Screens:**
	- [Waveshare](https://www.waveshare.com/ "Waveshare"):
		- [Eink 2,13"](https://www.waveshare.com/2.13inch-e-paper-hat.htm "Eink 2,13) (250x122)
		- [OLED/LCD](https://www.waveshare.com/oled-lcd-hat-a.htm "OLED/LCD") (OLEDs: 128x64; SSD1306; LCD: 320x240; 4 GPIO Buttons)
	- [Adafruit](https://www.adafruit.com/ "Adafruit"):
		- [Pitft 2,8"](https://www.adafruit.com/product/2298 "Pitft 2,8") (320x240; Resistive touch; 4 GPIO Buttons; GPIO Header)
		- [Pitft 2,4"](https://www.adafruit.com/product/2455 "Pitft 2,4") (320x240; Resistive touch; 5 GPIO Buttons; GPIO Header)
		- [Mini Pi tft 1,3"](https://www.adafruit.com/product/4484 "Mini Pi tft 1,3) (240x240; 2 GPIO Buttons; Stemma QT)
		- [TFT Bonnet](https://www.adafruit.com/product/4506) (240x240; 7 GPIO Buttons/Joystick; Stemma QT)
	- [Pimoroni](https://shop.pimoroni.com/ "Pimoroni"):
		- [Displayhatmini](https://shop.pimoroni.com/products/display-hat-mini?variant=39496084717651 "Displayhatmini") (320x240; 4 GPIO Buttons; Stemma QT; Breakout Garden / I2C header)
		- [Pirateaudio line-out](https://shop.pimoroni.com/products/pirate-audio-line-out?variant=31189750546515 "Pirateaudio line-out") (240x240; 4 GPIO Buttons; PCM5100A DAC chip with 3,5mm jack)
		- [GFX Hat 128x64](https://shop.pimoroni.com/products/gfx-hat?variant=12828343631955 "GFX Hat 128x64") (128x64; RGB Backlight; 6 capacitive touch buttons)
		- [Hyperpixel Touch](https://shop.pimoroni.com/products/hyperpixel-4?variant=12569485443155 "Hyperpixel Touch") (800x480; Breakout Garden / I2C header)
	- [Sparkfun](https://www.sparkfun.com/ "Sparkfun"):
		- [I2C OLED](https://www.sparkfun.com/products/24606 "I2C OLED") (128x32; SSD1306)
- **Power:**
	- [PiSugar 3](https://www.tindie.com/products/pisugar/pisugar-3-battery-for-raspberry-pi-zero/ "PiSugar 3")
	- [Pisugar 3 Plus](https://www.tindie.com/products/pisugar/pisugar-3-plus-battery-for-raspberry-pi-3b3b4b/ "Pisugar 3 Plus")
	- [Adafruit Qi Charger receiver module](https://www.adafruit.com/product/1901 "Adafruit Qi Charger receiver module")
- **GPS:**
	- [USB GPS Dongle](https://thepihut.com/products/usb-gps-receiver-compatible-with-raspberry-pi-lattepanda-jetson-nano "USB GPS Dongle") (U-blox 7 copy)
	- PA1010D I2C GPS boards
		- [Adafruit](https://www.adafruit.com/product/4415 "Adafruit")
		- [Pimoroni](https://shop.pimoroni.com/products/pa1010d-gps-breakout?variant=32257258881107 "Pimoroni")
- **Sandisk Ultra 32Gb micro SD**
- **Micro USB OTG cables and adapters**
- **USB Ethernet adapter**

