


# Table of contents

- [**Pwnagotchi Build Guide**](#pwnagotchi-build-guide)
  - [Build Instructions](#build-instructions)
    - [Step 1) Download the pwnagotchi image](#step-1-download-the-pwnagotchi-image)
    - [Step 2) Flash pwnagotchi image to microSD](#step-2-flash-pwnagotchi-image-to-microsd)
    - [Step 3) Build your initial config.toml](#step-3-build-your-initial-configtoml)
    - [Step 4) Copy config.toml to MicroSD (boot)](#step-4-copy-configtoml-to-microsd-boot)
    - [Step 5) If you are using an SPI LCD screen with Pi3 or Pi0, you may have to modifiy the config.txt.](#step-5-if-you-are-using-an-spi-lcd-screen-with-pi3-or-pi0-you-may-have-to-modifiy-the-configtxt)
    - [Step 6) Boot pwnagotchi for the first time WARNING: BE PATIENT.](#step-6-boot-pwnagotchi-for-the-first-time-warning-be-patient)
    - [Step 7) Bluetooth connection manually](#step-7-bluetooth-connection-manually)
    - [Step 8) Change all the default passwords](#step-8-change-all-the-default-passwords)
    - [Step 9) Install plugins](#step-9-install-plugins)
      - [Step - 9.1) Default plugins I use:](#step---91-default-plugins-i-use)
      - [Step 9.2) 3rd party plugins:](#step-92-3rd-party-plugins)
    - [Step 10) Back up all your hard work! Download the Backup script from Github.](#step-10-back-up-all-your-hard-work-download-the-backup-script-from-github)
- [**My Hardware:**](#my-hardware)
- [**My Setups:**](#my-setups)

# **Pwnagotchi Build Guide**

## **Build Instructions**

[**PLEASE REFER TO THE UNOFICCIAL PWNAGOTCHI SITE!**](http://https://pwnagotchi.org/ "PLEASE REFER TO THE UNOFICCIAL PWNAGOTCHI SITE!")

### **Step 1) Download the pwnagotchi image**

I use [**Jayofelonys repo**](https://github.com/jayofelony/pwnagotchi/releases/tag/v2.8.9 "Jayofelonys repo"). It is under active development based on the community feedback and updated frequently with bugfixes, new features, and supports more than 80 screens. Also you can skip most of these steps, if you can ssh in to your device, and use the wizard:

`sudo pwnagotchi --wizard`

### **Step 2) Flash pwnagotchi image to microSD**

*Note: Recommended to use **[Raspberry Imager](https://www.raspberrypi.com/software/ "Raspberry Imager")** to flash the image.*

Several tutorials exist online (Google or YouTube) that provide instructions for flashing an image to a microSD.

Before flashing the image I use the Raspberry Imager, to set the timezone, and change the default user/password for the OS.

### **Step 3) Build your initial config.toml**

Your initial config.toml will contain the baseline configuration for your pwnagotchi, such as the name of the device. It is recommended to avoid trying to configure all of your plugins at this stage, and only focus on the essential plugins, such as bt-tether, Modify as necessary!

```toml
main.name = "Pwnagotchi"
main.whitelist = [
 "your wifi here",
]

main.plugins.bt-tether.enabled = true
main.plugins.bt-tether.devices.android-phone.enabled = true
main.plugins.bt-tether.devices.android-phone.search_order = 1
main.plugins.bt-tether.devices.android-phone.mac = "MA:CA:DD:RE:SS"
main.plugins.bt-tether.devices.android-phone.ip = "192.168.44.44"
main.plugins.bt-tether.devices.android-phone.netmask = 24
main.plugins.bt-tether.devices.android-phone.interval = 1
main.plugins.bt-tether.devices.android-phone.scantime = 0
main.plugins.bt-tether.devices.android-phone.max_tries = 0
main.plugins.bt-tether.devices.android-phone.share_internet = true
main.plugins.bt-tether.devices.android-phone.priority = 1

main.plugins.bt-tether.devices.ios-phone.enabled = false
main.plugins.bt-tether.devices.ios-phone.search_order = 2
main.plugins.bt-tether.devices.ios-phone.mac = "MA:CA:DD:RE:SS"
main.plugins.bt-tether.devices.ios-phone.ip = "172.20.10.6"
main.plugins.bt-tether.devices.ios-phone.netmask = 24
main.plugins.bt-tether.devices.ios-phone.interval = 1
main.plugins.bt-tether.devices.ios-phone.scantime = 0
main.plugins.bt-tether.devices.ios-phone.max_tries = 0
main.plugins.bt-tether.devices.ios-phone.share_internet = true
main.plugins.bt-tether.devices.ios-phone.priority = 999

ui.display.enabled = true
ui.display.type = "waveshare_4"
ui.fps = 1
ui.invert = false

ui.web.enabled = true
ui.web.username = "changeme"
ui.web.password = "changeme"
```

### **Step 4) Copy config.toml to MicroSD (boot)**

*Note: If you removed, insert the microSD card flashed in Step 2.*
Open the new drive titled "boot", and copy over your config.toml

### **Step 5) If you are using an SPI LCD screen with Pi3 or Pi0, you may have to modifiy the config.txt.**

For jays image since 2.8.7 until now, there is some issue with the SPI chip select stuff.

If your screen is not showing any image, but the backlight is on, you should modify the **/boot/firmware/config.txt**, and change ***dtoverlay=spi0-0cs*** to ***dtoverlay=spi0-1cs*** under the necessary pi settings.

*Note: if you are sure that you need to modify the config.txt, you can do it after flashing the card. The config.txt is directly in the cards boot partition.*

### **Step 6) Boot pwnagotchi for the first time WARNING: BE PATIENT.**

The First boot will take longer than average due to key generation.

**NOTE**: If you specified settings for bt-tether plugin, ensure your mobile device is nearby and listening for new bluetooth devices to pair. Ensure Internet sharing via Personal Hotspot is enabled. Your mobile device will be prompted to pair with your pwnagotchi.

### **Step 7) Bluetooth connection manually**

SSH in (default login: pi, pw: raspberry)

`sudo bluetoothctl`

`scan on`

Wait until your phones mac address shows up and copy your phones mac address

`pair MA:CA:DD:RE:SS`

`trust MA:CA:DD:RE:SS`

`exit`

### **Step 8) Change all the default passwords**

If you haven't done it with the Raspberry Imager, change the user "pi" password. Default is "raspberry"

`passwd`

Change "root" password:

`sudo passwd root`

If you haven't done it when creating your config.toml file, change pwnagotchis Web UI password. Default is "changeme"

`sudo nano /etc/pwnagotchi/config.toml`

Locate and update the values for:

```toml
ui.web.username = "changeme"
ui.web.password = "changeme"
```

Update bettercap password, if you want to, I usually leave it as-is. Default is "pwnagotchi"

`sudo nano /etc/pwnagotchi/config.toml`

locate and update the values for:

```toml
bettercap.username = "pwnagotchi"
bettercap.password = "pwnagotchi"
```

For the new bettercap password to work yoyu have to modify these two files as well to match config.toml:

`sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-auto.cap`

`sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-manual.cap`

reload pwnagotchi for config changes to apply.

`sudo systemctl restart pwnagotchi.service`

### **Step 9) Install plugins**

Consider this step OPTIONAL, unless you would like these custom plugins. Otherwise, proceed to Step 10.

Make custom-plugins directory defined in config.toml, if not done so already.

`cd ~ sudo mkdir /usr/local/share/pwnagotchi/custom-plugins/`

I usually use the default plugin directory.

*Plugins marked with &#42; are not tested by me yet, or needs some tweaking to work on my setup.*
Installation instruction and details soon!

#### **Step - 9.1) Default plugins I use:**
These plugins are provided in [**Jayofelonys repo**](https://github.com/jayofelony/pwnagotchi/releases/tag/v2.8.9 "Jayofelonys repo"), therefore if you have a full config.toml, the settings should be in your config.toml as well. 
- 	[auto-update](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/auto-update.py)
	I usually leave it turned off, and update after the new release seems stable.
- 	[bt-tether](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/bt-tether.py)
	See [Step 3](#step-3-build-your-initial-configtoml) and [Step 7](#step-7-bluetooth-connection-manually).
- 	[fix-services](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/fix_services.py)
	Updated watchdog plugin to avoid the blindbug issue.
- 	**[gdrivesync](https://github.com/jayofelony/pwnagotchi/blob/master/README-google.md)***
	Not tested, but I would like to use something like this, to backup my pwnys automatically to a server (preferably to one of my NAS).
- 	**[gpio_buttons](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/gpio_buttons.py)***
    There are some issues with GPIO in the latest builds, I use it to control the pwnmenu.
- 	[grid](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/grid.py)
    Sending data to [the grid](https://opwngrid.xyz/)
- 	[logtail](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/logtail.py)
    Useful tool in the webUI, to check your logs without ssh.
- 	[memtemp](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/memtemp.py)
    Shows system information on the screen (CPU temperature; load and memory load).
- 	[onlinehashcrack](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/onlinehashcrack.py)
    Automatically uploads handshakes to [onlinehashcrack.com](https://onlinehashcrack.com).
- 	[session-stats](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/session-stats.py)
    Displays stats of the current session in the webUI.
- 	[webcfg](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/webcfg.py)
    Editor for your config.toml file in the webUI.
- 	[webgpsmap](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/webgpsmap.py)
    Shows GPS location of your handshakes on a map.
- 	[wpa-sec](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/wpa-sec.py)
    Automatically uploads handshakes to [wpa-sec](https://wpa-sec.stanev.org).

#### **Step 9.2) 3rd party plugins and mods:**
- [Clock](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/clock.py)
	Clock/Calendar for pwnagotchi
- [PiSugar3](https://github.com/nullm0ose/pwnagotchi-plugin-pisugar3)
	The PiSugar 3 Plugin displays the battery percentage as well as the charging status on your Pwnagotchi's UI.
- [Powerutils](https://github.com/sn0wflakeAU/powerutils)
	The Powerutils plugin lets you run the Pwnagotchi's internal shutdown, restart, or reboot functions, instead of the system "shutdown" command. By using the internal functions, you can access other features such as syncing the AI data before shutdown, or switching between AUTO and MANU mode.
- [Pwnmenu](https://github.com/sn0wflakeAU/pwnmenu/)
	Pwnmenu is a plugin that lets you run scripts on a Pwnagotchi using the 2.13 inch Waveshare e-paper display. You can use it to select and call scripts to extend the functionality of the host Raspberry Pi Zero W.
To do this, the Pwnmenu can be controlled with terminal commands bound to GPIO pins.
- [Custom Faces](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD)
	A mod that allows you to use custom images as pwnagotchi Faces with transparency feature (.png) and themed plugins.
- [Tweak View](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/tweak_view.py)
	Editor for the UI layout.
- **[Fancygotchi](https://github.com/V0r-T3x/pwnagotchi-fancygotchi)***
	Theme manager for the Pwnagotchi. **NOT WORKING WITH JAYS IMAGE AT THE MOMENT!!!**
- [GPSD Easy](https://github.com/jayofelony/pwnagotchi-torch-plugins/blob/main/gpsdeasy.py)
	Uses gpsd to report lat/long on the screen and setup bettercap pcap gps logging. Better than the baked in GPS plugin. The plugin should install gpsd automatically, but it can take a long time, especially with BT internet sharing. Before enabling the plugin for the first time you can install GPSD manually from the terminal:
`sudo apt-get install gpsd gpsd-clients`
- [Wardriver](https://github.com/cyberartemio/wardriver-pwnagotchi-plugin)
	A simple plugin for wardriving on your pwnagotchi.
- [Enable deauth](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_deauth.py) / [Enable Assoc](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_assoc.py)
	Enable and disable **DEAUTH** and **ASSOC** attacks on the fly. Enabled when plugin loads, disabled when plugin unloads.
- **[Touch UI](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/Touch_UI.py)***
	Use touchscreen input to toggle settings.
- [Instattack](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/instattack.py)
	Pwn more aggressively. Launch immediate associate or deauth attack when bettercap spots a device.
- [EXP V2](https://github.com/Kaska89/pwnagotchi-EXPv2-plugin)
	Get exp every time a handshake get captured. You can add the Age plugin too, but I reflash my build so often that EXP is more than enough for my pwnys.
- **[Achievement](https://github.com/LegendEvent/pwnagotchi-custom-plugins/blob/main/achievements.py)***
	Collect achievements for daily challenges.
- [Shower Thoughts](https://github.com/NoxiousKarn/Showerthoughts)
	Displays random r/showerthoughts headlines on your pwnagotchi when the device is waiting. You need to modify core files, which are rewritten to default whith autoupdate. Thinking about changing to [RSS Voice](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/rss_voice.py) plugin in the future

### **Step 10) Back up all your hard work!**
Download the Backup script from [Github]( https://github.com/evilsocket/pwnagotchi/blob/master/scripts/backup.sh)
Append the "FILES_TO_BACKUP" section of the backup script to include the following additional files that have been added or modified as a result of this guide:
```
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
```
Note: The last entry in the list must include an end quotation mark. Be sure to relocate this to the end of the list before saving.
Make the script executable:
`sudo chmod +x backup.sh`
Run the script
`sudo ./backup.sh`

Enjoy your new Pwnagotchi, and please support the Pwnagotchi community on [Reddit](https://www.reddit.com/r/pwnagotchi/) and [Discord](https://discord.gg/jUhuehCK4c)!

# **My Hardware:**
- **Boards:**
	- [Raspberry Pi](https://www.raspberrypi.com/)
		- [0](https://www.raspberrypi.com/products/raspberry-pi-zero/)
		- [0W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
		- [0W2](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
		- [3B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)
		- [3A+](https://www.raspberrypi.com/products/raspberry-pi-3-model-a-plus/)
		- [400](https://www.raspberrypi.com/products/raspberry-pi-400-unit/)
- **Screens:**
	- [**Waveshare**](https://www.waveshare.com/ "Waveshare"):
		- [Eink 2,13"](https://www.waveshare.com/2.13inch-e-paper-hat.htm "Eink 2,13") (250x122)
		- [OLED/LCD](https://www.waveshare.com/oled-lcd-hat-a.htm "OLED/LCD") (OLEDs: 128x64; SSD1306; LCD: 320x240; 4 GPIO Buttons)
	- [**Adafruit**](https://www.adafruit.com/ "Adafruit"):
		- [Pitft 2,8"](https://www.adafruit.com/product/2298 "Pitft 2,8") (320x240; Resistive touch; 4 GPIO Buttons; GPIO Header)
		- [Pitft 2,4"](https://www.adafruit.com/product/2455 "Pitft 2,4") (320x240; Resistive touch; 5 GPIO Buttons; GPIO Header)
		- [Mini Pi tft 1,3"](https://www.adafruit.com/product/4484 "Mini Pi tft 1,3") (240x240; 2 GPIO Buttons; Stemma QT)
		- [TFT Bonnet](https://www.adafruit.com/product/4506) (240x240; 7 GPIO Buttons/Joystick; Stemma QT)
	- [**Pimoroni**](https://shop.pimoroni.com/ "Pimoroni"):
		- [Displayhatmini](https://shop.pimoroni.com/products/display-hat-mini?variant=39496084717651 "Displayhatmini") (320x240; RGB LED, 4 GPIO Buttons; Stemma QT; Breakout Garden / I2C header)
		- [Pirateaudio line-out](https://shop.pimoroni.com/products/pirate-audio-line-out?variant=31189750546515 "Pirateaudio line-out") (240x240; 4 GPIO Buttons; PCM5100A DAC chip with 3,5mm jack)
		- [GFX Hat 128x64](https://shop.pimoroni.com/products/gfx-hat?variant=12828343631955 "GFX Hat 128x64") (128x64; RGB Backlight; 6 capacitive touch buttons)
		- [Hyperpixel Touch](https://shop.pimoroni.com/products/hyperpixel-4?variant=12569485443155 "Hyperpixel Touch") (800x480; Breakout Garden / I2C header)
	- [**Sparkfun**](https://www.sparkfun.com/ "Sparkfun"):
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

# **My Setups:**

| Name  | Picture  | Board  | Screen  | Case  | Power  | Extra  |
| :------------ | :------------ | :------------ | :------------ |  :------------ | :------------ | :------------ |
| **Pwnamon**  |   | Pi zero w  | Waveshare E-ink V4  | [3D printed](https://cults3d.com/en/3d-model/gadget/coque-pwnagotchi-waveshare3-pisugar3-et-protection-d-ecran-plexiglass "3D printed")  | PiSugar 3  |   |
| **FAT32**  |   | Pi 3B  | Adafruit Pitft 2,8"  | [Adafruit Case and Faceplate](https://www.adafruit.com/product/3062 "Adafruit Case and Faceplate") | USB  |   |
| **FAT16**  |   | Pi 3A+  | Adafruit Pitft 2,4"  | [Adafruit Case](https://www.adafruit.com/product/2361 "Adafruit Case") and [Faceplate](https://www.adafruit.com/product/2808 "Faceplate") | USB  |   |
| **Pip-Boy** |   | Pi zero 2 w  | Pimoroni Displayhat mini  | [3D printed](https://makerworld.com/en/models/417258#profileId-319628 "3D printed")  | PiSugar 3  |   |
| **WarDriver**  |   | Pi zero 2 w  | Adafruit Mini TFT  | 3D printed (under development) | USB  | Pimoroni I2C GPS  |
| **RasTest OLEDLCD**  |   | Pi 3A+  | Waveshare OLED/LCD |[Geekworm Alu case](https://geekworm.com/products/raspberry-pi-3a-a-cnc-ultra-thin-aluminum-alloy-metal-case " Geekworm Alu case") (+ 3D printed faceplate under development)  | USB  |   |
| **RasTest GFX Hat**  |   | Pi 3A+  | Pimoroni GFX Hat  | 3D printed (under development)  | Pisugar 3 Plus  | Adafruit I2C GPS  |
|   |   |   |   |   |   |   |
