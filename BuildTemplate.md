# [Pwnamon](https://opwngrid.xyz/search/392c08ac4f0ef60f82bd9169f5b7e09b01b8f01a8155cd2e50756a9f4dd36711)
![Pwnamon UI](https://github.com/RasTacsko/Pwnagotchi-workinprogress/blob/main/Pictures/UI_pwnamon.jpg?raw=true)
## Details
| Picture  | Board  | Screen  | Case  | Power  | Extra  | Firmware| Plugins  |
| :-- | :-- | :-- | :-- | :-- |  :-- | :-- | :-- |
| IMG | [Raspberry Pi0W](https://www.raspberrypi.com/products/raspberry-pi-zero/)|[Waveshare Eink 2,13"](https://www.waveshare.com/2.13inch-e-paper-hat.htm "Eink 2,13")|[3D printed](https://cults3d.com/en/3d-model/gadget/coque-pwnagotchi-waveshare3-pisugar3-et-protection-d-ecran-plexiglass "3D printed")|[PiSugar 3](https://www.tindie.com/products/pisugar/pisugar-3-battery-for-raspberry-pi-zero/ "PiSugar 3")|[USB GPS Dongle](https://thepihut.com/products/usb-gps-receiver-compatible-with-raspberry-pi-lattepanda-jetson-nano "USB GPS Dongle")|2.8.9| |

## Setup
### [Clock](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/clock.py)
### [PiSugar3](https://github.com/nullm0ose/pwnagotchi-plugin-pisugar3)
You have to install the PiSugar Powermanager.
Run this command and follow the instructions.
```sh
curl http://cdn.pisugar.com/release/pisugar-power-manager.sh | sudo bash
```
If you want to use the RTC too, add the following to your `/boot/firmware/config.txt` file:
`dtoverlay=i2c-rtc,ds3231`
After these steps finished you can reach the PiSugar power manager on `http://<your raspberry ip>:8421`
On this build I use the Custom Button functions to control the Pwnmenu plugin, and in the settings for soft shutdown, I use a python command to shutdown the pi .with the Powerutils plugin
### [Pwnmenu](https://github.com/sn0wflakeAU/pwnmenu/)
### [Powerutils](https://github.com/sn0wflakeAU/powerutils)
### [GPSD Easy](https://github.com/jayofelony/pwnagotchi-torch-plugins/blob/main/gpsdeasy.py)
```sh
sudo apt-get install gpsd gpsd-clients
```
### [Wardriver](https://github.com/cyberartemio/wardriver-pwnagotchi-plugin)
### [Enable deauth](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_deauth.py)
### [Enable Assoc](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_assoc.py)
### [Instattack](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/instattack.py)
### [Custom Faces](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD)
### [EXP V2](https://github.com/Kaska89/pwnagotchi-EXPv2-plugin)
### [Tweak View](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/tweak_view.py)
