*** Pwnagotchi Build Guide *** Description:

notes for building my pwnagotchis
Last Updated: 2023 April

*** Hardware: ***

Boards: Raspberry Pi 0W; 0W2; 3B; 3A+
Screens:
Waveshare: Eink 2,13" V3 <D34d>; OLED/LCD
Adafruit: Pitft 2,8" & 2,4"; MiniPiTFT 240x240; TFT Bonnet
Pimoroni: Displayhatmini; Pirateaudio line-out; GFX Hat 128x64
Sparkfun: I2C OLED 128x32
Power: PiSugar 3; Pisugar 3 Plus
GPS: USB GPS Dongle (U-blox 7); I2C PA1010D (Adafruit & Pimoroni)
Sandisk Ultra 32Gb micro SD
Micro USB OTG cable; USB Ethernet adapter

*** Build Instructions Below: ***

PLEASE REFER TO THE UNOFICCIAL PWNAGOTCHI SITE!

Step 1) Download Pwnagotchi image
Jayofelony repo: https://github.com/jayofelony/pwnagotchi/releases

Step 2) Flash pwnagotchi image to microSD. Note: Recommended to use "Raspberry Imager" to flash the image. 
Several tutorials exist online (Google or YouTube) that provide instructions for flashing an image to a microSD.
Before flashing the image I use the Raspberry Imager, to set the timezone, and change the default user/password.

Step 3) Build your initial config.toml 
Note: your initial config.toml will contain the baseline configuration for your pwnagotchi, such as the name of the device. It is recommended to avoid trying to configure all of your plugins at this stage, and only focus on the essential plugins, such as 'bt-tether'.

######## start of config.toml ######## 

########  end of config.toml  ########

Step 4) Copy config.toml to MicroSD (boot) 
Note: If you removed, insert the microSD card flashed in Step 3. 
Open the new drive titled "boot", and copy over your config.toml

Step 5) If you are using an SPI LCD screen with Pi3 or Pi0, you may have to modifiy the config.txt.
For jays image since 2.8.7 until now, there is some issue with the SPI chip select stuff.
If your LCD screen isn't showing any image, but backlight works, you should modify the /boot/firmware/config.txt, and change dtoverlay=spi0-0cs to dtoverlay=spi0-1cs under the necessary pi settings.

Step 6) Boot pwnagotchi for the first time WARNING: BE PATIENT. 
The First boot will take longer than average due to key generation.

NOTE: If you specified settings for bt-tether plugin, ensure your mobile device is nearby and listening for new bluetooth devices to pair. Ensure Internet sharing via Personal Hotspot is enabled. Your mobile device will be prompted to pair with your pwnagotchi.

Step 6) Bluetooth connection manually

SSH in (default login: pi, pw: raspberry)
sudo bluetoothctl
scan on
Wait until your phones mac address shows up
Copy your phoes mac address
pair MA:CA:DD:RE:SS
trust MA:CA:DD:RE:SS
exit

Step 7) Change all the default passwords
If you haven't done it with the Raspberry Imager, change "pi" password. Default "raspberry"
passwd

Change "root" password:
sudo passwd root

If you haven't done it yet, change pwnagotchi Web UI password. Default "changeme"
sudo nano /etc/pwnagotchi/config.toml

Locate and update the values for:
ui.web.username = "changeme"
ui.web.password = "changeme"

Update bettercap password, if you want to. Default "pwnagotchi"
sudo nano /etc/pwnagotchi/config.toml

locate and update the values for:
bettercap.username = "pwnagotchi"
bettercap.password = "pwnagotchi"
sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-auto.cap #modify the bettercap username & password to match config.toml sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-manual.cap #modify the bettercap username & password to match config.toml

sudo systemctl restart pwnagotchi.service #reload pwnagotchi for config changes to apply.

Step 8) Install custom plugins 
Consider this step OPTIONAL, unless you would like these custom plugins. Otherwise, proceed to Step 10. 
Make custom-plugins directory defined in config.toml, if not done so already.
cd ~ sudo mkdir /usr/local/share/pwnagotchi/installed-plugins/ 

Step 8.1) Default plugins I use: 
auto-update
bt-tether
fix-services
gdrivesync*
gpio_buttons*
grid
logtail
memtemp
onlinehashcrack
session-stats
webcfg
webgpsmap
wpa-sec

Step 8.2) 3rd party plugins:
Clock
PiSugar3
Poweruitls
Pwnmenu
Custom Faces
Tweak View
Fancygotchi*
GPSD Easy
Wardriver
Aircrackonly
Enable deauth / Enable Assoc / Touch UI*
Instattack
EXP V2
Achievement*
Shower Thoughts*

Plugins marked with * are not tested by me yet, or needs some tweaking to work on my setup.
Details soon


Step 9) Back up all your hard work! Download the Backup script from Github.

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
