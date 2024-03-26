*** Pwnagotchi Build Guide ***
Description:
  * notes for building my pwnagotchis
  * Last Updated: 2023 April
 
*** Hardware: ***
   * Boards: Raspberry Pi 0W; 0W2; 3B; 3A+
   * Screens:
     * Waveshare: Eink 2,13" V3; OLED/LCD
     * Adafruit: Pitft 2,8" & 2,4"; MiniPiTFT 240x240; TFT Bonnet
     * Pimoroni: Displayhatmini; Pirateaudio line-out; GFX Hat 128x64
     * Sparkfun: I2C OLED 128x32
   * Power: PiSugar 3; Pisugar 3 Plus
   * GPS: USB GPS Dongle (U-blox 7); I2C PA1010D (Adafruit & Pimoroni)
   * Sandisk Ultra 32Gb micro SD
   * Micro USB OTG cable; USB Ethernet adapter
 
*** Build Instructions Below: ***

[PLEASE REFER TO THE UNOFICCIAL PWNAGOTCHI WIKI!](https://pwnagotchi.org/index.html)

Step 1) Download Pwnagotchi image
  * Jayofelony repo: https://github.com/jayofelony/pwnagotchi/releases
 
Step 2) Flash pwnagotchi image to microSD.
Note: Recommended to use "Raspberry Imager" to flash the image. 
Several tutorials exist online (Google or YouTube) that provide instructions for flashing an image to a microSD.
 
Step 3) Build your initial config.toml
Note: your initial config.toml will contain the baseline configuration for your pwnagotchi, such as the name of the device. 
It is recommended to avoid trying to configure all of your plugins at this stage, and only focus on the essential plugins, such as 'bt-tether'.
 
######## start of config.toml ########
main.name = "pwnagotchi"
main.lang = "en"
main.whitelist = [
 "Your",
 "Network",
 "Here",
]
main.plugins.grid.enabled = true
main.plugins.grid.report = true
main.plugins.grid.exclude = [
 "Your",
 "Network",
 "Here",
]

main.plugins.bt-tether.enabled = true
main.plugins.bt-tether.devices.android-phone.enabled = true
main.plugins.bt-tether.devices.android-phone.search_order = 1
main.plugins.bt-tether.devices.android-phone.mac = "CH:AN:GE:XX:MM:EE"    # Change this to your phones BT MAC
main.plugins.bt-tether.devices.android-phone.ip = "192.168.44.44"         # If you have multiple pwnagotchi units, they will need different IPs 
main.plugins.bt-tether.devices.android-phone.netmask = 24
main.plugins.bt-tether.devices.android-phone.interval = 1
main.plugins.bt-tether.devices.android-phone.scantime = 10
main.plugins.bt-tether.devices.android-phone.max_tries = 0
main.plugins.bt-tether.devices.android-phone.share_internet = true
main.plugins.bt-tether.devices.android-phone.priority = 1

ui.display.enabled = false          # set it to false, just to be safe
ui.display.rotation = 0             # 0 and 180 degree are supported for most screens, square ones can rotate 90 and 270 too
ui.display.type = "displayhatmini"  # for screen support check the repo that you are using (pwnagotchi/pwnagotchi/ui/hw/)
ui.display.color = "black"

# The web ui will be available from phone on the previously set IP, or if you connect to a router check the Pi-s IP address for web the web ui
ui.web.username = "changeme"
ui.web.password = "changeme"

######## end of config.toml ########
 
Step 4) Copy config.toml to MicroSD (boot)
Note: Insert the microSD card flashed in Step 3. Open the new drive titled "boot", and copy over your config.toml
 
Step 5) Boot pwnagotchi for the first time
WARNING: BE PATIENT. The First boot will take longer than average due to key generation.

NOTE: If you specified settings for bt-tether plugin, ensure your mobile device is nearby and listening for new bluetooth devices to pair. 
Ensure Internet sharing via Personal Hotspot is enabled. Your mobile device will be prompted to pair with your pwnagotchi.

Step 6) Bluetooth connection manually
   * SSH in (default login: pi, pw: raspberry)

Step 9) Install custom plugins 
 #Consider this step OPTIONAL, unless you would like these custom plugins. Otherwise, proceed to Step 10.
 cd ~
 sudo mkdir /usr/local/share/pwnagotchi/installed-plugins/ 
      #make custom-plugins directory defined in config.toml, if not done so already.
 
 Step 9.1) aircrackonly plugin
  sudo pwnagotchi plugins install aircrackonly
  sudo nano /etc/pwnagotchi/config.toml
       # add the following lines to config.toml:
         main.plugins.aircrackonly.enabled = true
         main.plugins.aircrackonly.face = "( >.< )"
         
  # Aircrack-ng needed, to install:
  apt-get install aircrack-ng
        
 Step 9.2) Exp plugin #Generates an "experiance" level and progress bar for your pwnagotchi.
  #Copy exp.py from git: https://github.com/GaelicThunder/Experience-Plugin-Pwnagotchi
  sudo nano /usr/local/share/pwnagotchi/installed-plugins/exp.py #paste contents of exp.py from github to exp.py on your pwnagotchi.
  sudo nano /etc/pwnagotchi/config.toml
  #add the following to your config.toml. Please note that the positions have been adjusted to accomodate the waveshare 3.7 display.
    main.plugins.exp.enabled = true
    main.plugins.exp.lvl_x_coord = 0
    main.plugins.exp.lvl_y_coord = 210
    main.plugins.exp.exp_x_coord = 0
    main.plugins.exp.exp_y_coord = 228
 
 Step 9.3) Age plugin #Generates the pwnagotchi's "age" and "strength".
  #Copy exp.py from git: https://github.com/hannadiamond/pwnagotchi-plugins/blob/main/plugins/age.py
  sudo nano /usr/local/share/pwnagotchi/installed-plugins/age.py #paste contents of exp.py from github to exp.py on your pwnagotchi.
  sudo nano /etc/pwnagotchi/config.toml
  #add the following to your config.toml. Please note that the positions have been adjusted to accomodate the waveshare 3.7 display.
    main.plugins.age.enabled = true
    main.plugins.age.age_x_coord = 0
    main.plugins.age.age_y_coord = 56
    main.plugins.age.str_x_coord = 125
    main.plugins.age.str_y_coord = 56
    
 Step 9.4) GPS plugin #Uses the Ublox-7 USB GPS dongle to capture the GPS coordinates for a collected handshake. 
    #NOTE: Many people believe the GPS plugin should always communicate the current GPS coordinates. This is not true. the GPS coordinates will only update on the display when a handshake has been obtained. 
    #Troubleshooting: If the GPS dongle does not appear to be functioning, it is likely that the device is unable to capture a location (or has yet to capture a handshake. Try changing your physical location (i.e. go outside, walk around the house, down the street, etc). 
  lsusb #confirm the gps dongle is detected as plugged in.
  sudo pwnagotchi plugins install gps
  sudo nano /etc/pwnagotchi/config.toml
  #add the following to your config.toml. Please note that the positions have been adjusted to accomodate the waveshare 3.7 display.
    main.plugins.gps.enabled = true
    main.plugins.gps.speed = 19200
    main.plugins.gps.device = "/dev/ttyACM0" #gps dongle location
    main.plugins.gps.position = "225,194" #adjusted to support waveshare 3.7
    main.plugins.gps.linespacing = 18 #adjusted to support waveshare 3.7
    
 Step 9.5) PiSugar Plugin 
  #Ensure PiSugar Power Manager is installed:
  curl http://cdn.pisugar.com/release/pisugar-power-manager.sh | sudo bash
  cd /usr/local/share/pwnagotchi/installed-plugins/
  sudo nano pisugar2.py
  #locate and modify the following contents of 'def on_ui_setup':
        def on_ui_setup(self, ui):
        ui.add_element(
            "bat",
            LabeledValue(
                color=BLACK,
                label="BAT",
                value="0%",
                position=(ui.width() / 2 + 30, 0),
                label_font=fonts.Bold,
                text_font=fonts.Medium,
            ),
        )
  
 Step 9.6) memtemp Plugin
  sudo pwnagotchi plugins install memtemp
  sudo nano /etc/pwnagotchi/config.toml
  #add the following to your config.toml. Please note that the positions have been adjusted to accomodate the waveshare 3.7 display.
    main.plugins.memtemp.enabled = true
    main.plugins.memtemp.scale = "celsius"
    main.plugins.memtemp.orientation = "vertical" #adjusted for preference on waveshare 3.7
    main.plugins.memtemp.position = "382,194" #adjusted to support waveshare 3.7
    main.plugins.memtemp.linespacing = 18 #adjusted to support waveshare 3.7
    
 Step 9.7) customize bt-tether display position #to accomodate waveshare 3.7
  cd /usr/local/lib/python3.7/dist-packages/pwnagotchi/plugins/default 
  sudo nano bt-tether.py
  #locate and modify the following under 'def pn_ui_setup':
    def on_ui_setup(self, ui):
        with ui._lock:
            ui.add_element('bluetooth', LabeledValue(color=BLACK, label='BT', value='-', position=(ui.width() / 2 - 28$
                           label_font=fonts.Bold, text_font=fonts.Medium))
    
  sudo systemctl restart pwnagotchi.service #reload pwnagotchi with new plugins
 
Step 10) Update everything. #OPTIONAL. I'm just obsessive about updating everything...
 sudo pwnagotchi plugins update 
 sudo pwnagotchi plugins upgrade
 sudo apt-get update --allow-releaseinfo-change
      #Troubleshooting: Some repos for "re4son-kernel.com/re4son kali-pi" might present an error resembling the following: "The following signatures were invalid: EXPKEYSIG 11764EE8AC24832F Carsten Boeving <carsten.boeving@whitedome.com.au>"
      wget -O - https://re4son-kernel.com/keys/http/archive-key.asc | sudo apt-key add -
 
 sudo apt-get upgrade #This will take a while (~45 minutes). Be patient.
      #Troubleshooting: You might encounter an error that looks similar to:
      # Errors were encountered while processing:
      #  /var/cache/apt/archives/kalipi-kernel_5.4.83-20211204_armhf.deb
      # E: Sub-process /usr/bin/dpkg returned an error code (1)
         sudo mv /boot/overlays/ overlaysbackup #rename the existing overlays in /boot/. The renamed overlays can be safely deleted later
         sudo apt-get upgrade #attempt upgrade again.
 
 
Step 11) Change all the default passwords
 # Change "pi" password. Default "raspberry"
 psswd
 
 # Change "root" password:
 sudo su
 psswd
 
 # Change pwnagotchi Web UI password. Default "changeme"
 sudo nano /etc/pwnagotchi/config.toml
  # locate and update the values for:
    ui.web.username = "changeme"
    ui.web.password = "changeme"
 
 # Update bettercap password. Default "pwnagotchi"
 sudo nano /etc/pwnagotchi/config.toml
  # locate and update the values for:
    bettercap.username = "pwnagotchi"
    bettercap.password = "pwnagotchi"
  sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-auto.cap 
    #modify the bettercap username & password to match config.toml
  sudo nano /usr/local/share/bettercap/caplets/pwnagotchi-manual.cap
    #modify the bettercap username & password to match config.toml
 
 sudo systemctl restart pwnagotchi.service #reload pwnagotchi for config changes to apply.
    
Step 12) Back up all your hard work!
 Download the Backup script from Github.
 # Link: https://github.com/evilsocket/pwnagotchi/blob/master/scripts/backup.sh
 
 Append the "FILES_TO_BACKUP" section of the backup script to include the following additional files that have been added or modified as a result of this guide:
 
  /usr/bin/pwnlib \
  /etc/systemd/system/pwngrid-peer.service \
  /usr/local/share/pwnagotchi/custom-plugins/ \
  /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/libs/waveshare/v37inch/ \
  /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/waveshare37inch.py \
  /usr/local/lib/python3.7/dist-packages/pwnagotchi/utils.py \
  /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/display.py \
  /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/components.py \
  /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/__init__.py
 
     # Note: The last entry in the list must include an end quotation mark. Be sure to relocate this to the end of the list before saving.
  
  sudo chmod +x backup.sh # make backup.sh executable
  sudo ./backup.sh
 
#### Enjoy your new Pwnagotchi, and please support the Pwnagotchi community on Reddit and Discord! ####
 
Step 13) [OPTIONAL] Accessing your handshakes
#### Additional Optional step, curtosy of /u/Capt_Panic on Reddit and Discord #### 
    #Reference: https://www.reddit.com/r/pwnagotchi/comments/ubnlde/comment/i6gg8sj/?utm_source=share&utm_medium=web2x&context=3
    
#create file to access handshakes
 sudo nano cph.sh
 #insert these lines into the file
    \#/bin/bash
 
 cp -r /root/handshakes/\* /home/pi/handshakes/
 
 chown pi:pi /home/pi/handshakes
 
 chown pi:pi /home/pi/handshakes/\*
 sudo chmod +x cph.sh
    #To run file, execute 'sudo cph.sh'. This will copy your handshakes into the /home/pi/handshakes directory
 
Step 14) [OPTIONAL] May be required if you are having troubles with bluetooth
#### Additional Optional step, curtosy of /u/Capt_Panic on Reddit and Discord #### 
    #Reference: https://www.reddit.com/r/pwnagotchi/comments/ubnlde/comment/i6gg8sj/?utm_source=share&utm_medium=web2x&context=3
 
 # We need to add something into our profile which is in our root directory, hidden.
 sudo su
 cd /root
 sudo nano ~/.profile
 #add the following at the bottom of the file.
 \# attempt to restart bluetooth
 
 sudo systemctl restart bluetooth
 #save using crtl + x and then hit enter.
 #Comment out an if-else-statement.
 sudo nano /usr/bin/btuart
 #At the first if-else-statement you see, comment it out like you you see below.
 \#if grep -q "raspberrypi,4" /proc/device-tree/compatible; then
 
 BDADDR=
 
 \#else
 
 SERIAL='cat /proc/device-tree/serial-number | cut -c9-'
 
 B1='echo $SERIAL | cut -c3-4'
 
 B2='echo $SERIAL | cut -c5-6'
 
 B3='echo $SERIAL | cut -c7-8'
 
 BDADDR='printf b8:27:eb:%02x:%02x:%02x $((0x$B1 \^ 0xaa)) $((0x$B2 \^ 0xaa)) $((0x$B3 \^ 0xaa))'
 
 \#fi
 #save it using crtl + x and then hit enter.
 sudo reboot
