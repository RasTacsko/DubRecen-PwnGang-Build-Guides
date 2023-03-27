# *** Pwnagotchi Build Guide ***
Description:
  * notes for building my pwnagotchi
  * Based on: the guide from CyberSnek (https://pastebin.com/bTkXiZ52)
  * Last Updated: 2023 April
 
# *** Hardware: ***
   * Raspberry Pi 3b
   * Pitft 2,8" resistive touch
   * PiSugar 3 Plus 5000 mAh UPS (pending)
   * Panda Wireless PAUN09 Wifi Adapter (pending)
   * DIYmall VK-172 USB GPS Dongle (U-blox 7)
   * Sandisk Ultra 32Gb micro SD
 
*** Kudos and Special Thanks: ***
  * Reddit User "u/panoptyk", for their "Guerrilla guide to Pwnagotchi [v1.5.5/2022]:
    Link: https://www.reddit.com/r/pwnagotchi/comments/sl2rv1/guerrilla_guide_to_pwnagotchi_v1552022/?utm_source=share&utm_medium=web2x&context=3
  * Junohea (Wark#8463) on the "Pwnagotchi Unofficial" Discord, for their guidance on configuring an external wifi adapter
  * Reddit User "u/Capt_Panic" on Reddit and Discord, for their contributions to this guide.
    Link: https://www.reddit.com/r/pwnagotchi/comments/ubnlde/comment/i6gg8sj/?utm_source=share&utm_medium=web2x&context=3
  * The Pwnagotchi Reddit Community:
    Link: https://www.reddit.com/r/pwnagotchi/
  * The "Pwnagotchi Unofficial" Discord Community:
    Link: https://discord.gg/8fV5Ka32
  * GaelicThunder on GitHub, for their Exp Plugin:
    Link: https://github.com/GaelicThunder/Experience-Plugin-Pwnagotchi
  * Hanna.Diamond on GitHub, for their Age Plugin and Waveshare 3.7" e-ink display Plugin:
    Link: https://github.com/hannadiamond/pwnagotchi-plugins
 
*** Build Instructions Below: ***
 
Step 1) Download Pwnagotchi image from pwnagotchi.ai
       Note: version 1.5.5 is the latest version as of April 2022
             Many have recommended instead to flash version 1.5.3
             in order to avoid reported bugs regarding AI mode not starting.
             once installed, version 1.5.3 will automatically update to 1.5.5
             with an established internet connection (host connection sharing or bt-tether)
 Download version 1.5.3 to avoid having to fix AI Mode. 
      Remediation guidance for v1.5.5 AI Mode bug is available from u/panoptyk on Reddit. See Link in Kudos section above.
 
Step 2) Flash pwnagotchi image to microSD.
       Note: Recommended to use "balenaEtcher" to flash the image.
             Several tutorials exist online (Google or YouTube) that
             provide instructions for flashing an image to a microSD.
 
Step 3) Build your initial config.toml
       Note: your initial config.toml will contain the baseline configuration
             for your pwnagotchi, such as the name of the device. It is recommended to avoid
             trying to configure all of your plugins at this stage, and only focus on the 
             essential plugins, such as 'bt-tether'.
 
######## start of config.toml ########
 
Main settings
main.name = "pwnagotchi"
main.lang = "en"
main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"
main.whitelist = [
  "Other...",
]
 
#Reporting results to PwnGRID
main.plugins.grid.enabled = true
main.plugins.grid.report = true
main.plugins.grid.exclude = [
  "Other..."
]
 
#Display configuration
ui.display.enabled = false #set to false for now
ui.display.type = "waveshare37inch" #"waveshare37inch" doesn't exist (yet). To be created later...
ui.display.color = "black"
 
#Reduce Writes to preserve SD Lifespan
fs.memory.enabled = true
fs.memory.mounts.log.enabled = true
fs.memory.mounts.data.enabled = true
 
#bt-tether settings
main.plugins.bt-tether.enabled = true
main.plugins.bt-tether.devices.ios-phone.enabled = true
main.plugins.bt-tether.devices.ios-phone.search_order = 1
main.plugins.bt-tether.devices.ios-phone.mac = "CH:AN:GE:XX:MM:EE" #mobile Bluetooth MAC
main.plugins.bt-tether.devices.ios-phone.ip = "172.20.10.6" #custom static IP for iPhone PAN
main.plugins.bt-tether.devices.ios-phone.netmask = 24
main.plugins.bt-tether.devices.ios-phone.interval = 1
main.plugins.bt-tether.devices.ios-phone.scantime = 10
main.plugins.bt-tether.devices.ios-phone.max_tries = 10
main.plugins.bt-tether.devices.ios-phone.share_internet = true
main.plugins.bt-tether.devices.ios-phone.priority = 1
 
######## end of config.toml ########
 
Step 4) Copy config.toml to MicroSD (boot)
        Note: Insert the microSD card flashed in Step 3.
 Open the new drive titled "boot", and copy over your config.toml
 
Step 5) Boot pwnagotchi for the first time, connected via USB (will boot into MANU Mode).
        WARNING: BE PATIENT. The First boot will take longer than average due to key generation.
        NOTE: If you specified settings for bt-tether plugin, ensure your mobile device is
              nearby and listening for new bluetooth devices to pair. 
              Ensure Internet sharing via Personal Hotspot is enabled.
 Your mobile device will be prompted to pair with your pwnagotchi.
 
Step 6) Configure host Internet sharing (macOS) 
  This guide will cover host internet sharing for macOS only. Windows host internet sharing is available from u/panoptyk on Reddit. See Link in Kudos section above.
  ETH0 Instructions for Internet access via onboard ethernet port can be found via the following link, thanks to u/Capt_Panic on Reddit: https://reddit.com/r/pwnagotchi/comments/ucig3u/configuring_pi_3_b_for_pnwagotchi_for_nic/
 ** On pwnagotchi: **
  ssh pi@10.0.0.2
     # type "yes" if prompted to accept the ssh key for this not-yet known host.
     # default password: "raspberry" (to be changed later)
     # Note: If you receive "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!":
           # This is due to a previous ssh entry conflicting with your pwnagtochi's IP/hostname.
           sudo nano /Users/{user}/.ssh/known_hosts
           # comment-out or delete lines resembling your raspberry pi IP or hostname
 
  sudo nano /etc/resolv.conf
       # modify "nameserver 127.0.0.1" to be "nameserver 1.1.1.1"
 
  sudo nano /etc/network/interfaces.d/usb0-cfg
       # add "dns-nameservers 1.1.1.1" under the gateway line"
 
  sudo nano /etc/dnsmasq.conf
       # add "server=1.1.1.1@usb0"
 
  sudo systemctl disable dnsmasq
 
  sudo chattr +i /etc/resolv.conf
      # make file immutable 
 
 ** On host macOS system: **
      # Manually configure network device (RNDIS/Ethernet Gadget) IPv4 to support
      # default IP addressing.
        "IPv4 Address: 10.0.0.1"
        "Subnet Mask: 255.255.255.0"
        "Router: 10.0.0.1"
 
  sudo ./macos_connection_share.sh 
      # Note: Internet sharing scripts obtained from pwnagotchi.ai. 
      #       More scripts are available for Windows and Linux OS at pwnagotchi.ai
      #
      # The Raspberry Pi 4b comes equiped with a Ethernet Port, allowing most users the ability to directly connect 
      # their pwnagotchi to their home router, or to their computer via the CAT 5 port. This is a far simpler method
      # of obtaining internet access than the instructions I provide below. However, if you are like me, the method below 
      # provides you the ability to quickly connect your rpi to your comptuer on-the-go via a USB C cable.
      #
      # Troubleshooting:
        Unable to ping 1.1.1.1 from pwnagotchi with macOS host sharing:
        # "sudo pfctl -sn" may sometimes report the following:
          # nat on en0 inet from 10.0.0.0/24 to any -> (en0) round-robin
          # Fix via: "sudo echo "nat on en0 from en6:network to any -> en0" | sudo pfctl -f -"
          # The above cmd sets proper nat direction (rather than round-robin DNS).
 
Step 7) Install waveshare 3.7 e-ink display
 cd ~
 sudo mkdir /usr/local/share/pwnagotchi/custom-plugins/ 
      #make custom-plugins directory defined in config.toml, if not done so already.
      
 sudo mkdir /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/libs/waveshare/v37inch
 
 sudo git clone https://github.com/hannadiamond/pwnagotchi-plugins.git
 
 cd ./pwnagotchi-plugins/waveshare_37inch/
 
 sudo cp -r /home/pi/pwnagotchi-plugins/waveshare_37inch/v37inch/. /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/libs/waveshare/v37inch
 
 sudo cp waveshare37inch.py /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw
 
 sudo nano /etc/pwnagotchi/config.toml
      #set: ui.display.enabled = true
      #set: ui.display.type = "waveshare37inch"
 
 sudo nano /usr/local/lib/python3.7/dist-packages/pwnagotchi/utils.py
 #Locate "def load_config" and add the following:
 elif config['ui']['display']['type'] in ('ws_37inch', 'ws37inch', 'waveshare_37inch', 'waveshare37inch'):
    config['ui']['display']['type'] = 'waveshare37inch'
 
 sudo nano /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/display.py
 #Add the following:
 def is_waveshare37inch(self):
   return self.implementation.name == 'waveshare37inch'
 
 sudo nano /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/components.py
 #Locate "class LabeledValue" and REPLACE "def draw" with:
     def draw(self, canvas, drawer):
        if self.label is None:
            drawer.text(self.xy, self.value, font=self.label_font, fill=self.color)
        else:
            pos = self.xy
            drawer.text(pos, self.label, font=self.label_font, fill=self.color)
            drawer.text((pos[0] + self.label_spacing + self.label_font.getsize(self.label)[0], pos[1]), self.value, font=self.text_font, fill=self.color)
 
 sudo nano /usr/local/lib/python3.7/dist-packages/pwnagotchi/ui/hw/__init__.py
 #Add the following:
 from pwnagotchi.ui.hw.waveshare37inch import Waveshare37inch
 #Also, add the following into the elif block of the code:
 elif config['ui']['display']['type'] == 'waveshare37inch':
    return Waveshare37inch(config)
    
 sudo systemctl restart pwnagotchi.service #to initialize new waveshare 3.7 display. 
    # Troubleshooting: If the screen does not come on: 
    # Just SSH into your pwnagotchi via USB and check your work from the beginning of step 7.
    # I typically add the waveshare37 code snippets right between the sections for "waveshare27" and 
    # "waveshare29" in their respective sections within each script being modified.
 
Step 8) Install & Configure Wireless adapter
 lsusb #ensure wifi adapter is plugged in and detected
 iw dev #ensure wlan1 is observed with mon0 under phy#1
 sudo nano /boot/config.txt
   # Find the following line:
     # Additional overlays and parameters are documented /boot/overlays/README
   # Add the following line under it:
     dtoverlay=disable-wifi #disables the onboard wifi, allowing our adapter to operate as wlan0
 
 sudo nano /usr/bin/pwnlib
 #locate and replace the contents of "start_monitor_interface with the following:
   #rename adapter and bring up as mon0 in monitor mode
   ip link set wlan0 down
   ip link set wlan0 name mon0
   iw dev mon0 set type monitor
   ip link set mon0 up
   #add a mon1 interface from the same adapter
   iw phy "$(iw phy | head -1 | cut -d" " -f2)" interface add mon1 type monitor
   
 sudo nano /etc/systemd/system/pwngrid-peer.service
  # update the service launch param. Replace "mon0" with "mon1"
  # Everything else continues to use mon0, bettercap accepts it and works fine. Pwngrid works fine on the mon1 interface.
 
 sudo reboot #allow all changes to take affect.
 
Step 9) Install custom plugins 
 #Consider this step OPTIONAL, unless you would like these custom plugins. Otherwise, proceed to Step 10.
 cd ~
 sudo mkdir /usr/local/share/pwnagotchi/custom-plugins/ 
      #make custom-plugins directory defined in config.toml, if not done so already.
 
 Step 9.1) aircrackonly plugin
  sudo pwnagotchi plugins install aircrackonly
  sudo nano /etc/pwnagotchi/config.toml
       # add the following lines to config.toml:
         main.plugins.aircrackonly.enabled = true
         main.plugins.aircrackonly.face = "(>.<)"
        
 Step 9.2) Exp plugin #Generates an "experiance" level and progress bar for your pwnagotchi.
  #Copy exp.py from git: https://github.com/GaelicThunder/Experience-Plugin-Pwnagotchi
  sudo nano /usr/local/share/pwnagotchi/custom-plugins/exp.py #paste contents of exp.py from github to exp.py on your pwnagotchi.
  sudo nano /etc/pwnagotchi/config.toml
  #add the following to your config.toml. Please note that the positions have been adjusted to accomodate the waveshare 3.7 display.
    main.plugins.exp.enabled = true
    main.plugins.exp.lvl_x_coord = 0
    main.plugins.exp.lvl_y_coord = 210
    main.plugins.exp.exp_x_coord = 0
    main.plugins.exp.exp_y_coord = 228
 
 Step 9.3) Age plugin #Generates the pwnagotchi's "age" and "strength".
  #Copy exp.py from git: https://github.com/hannadiamond/pwnagotchi-plugins/blob/main/plugins/age.py
  sudo nano /usr/local/share/pwnagotchi/custom-plugins/age.py #paste contents of exp.py from github to exp.py on your pwnagotchi.
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
  curl http://cdn.pisugar.com/release/Pisugar-power-manager.sh | sudo bash
  cd /usr/local/share/pwnagotchi/custom-plugins/
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
