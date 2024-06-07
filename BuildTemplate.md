# [Pwnamon](https://opwngrid.xyz/search/392c08ac4f0ef60f82bd9169f5b7e09b01b8f01a8155cd2e50756a9f4dd36711)

## Hardware list
| Picture  | Board  | Screen  | Case  | Power  | Extra  | Firmware|
| :-- | :-- | :-- | :-- | :-- |  :-- | :-- | 
|![Pwnamon UI](https://github.com/RasTacsko/Pwnagotchi-workinprogress/blob/main/Pictures/UI_pwnamon.jpg?raw=true)| [Raspberry Pi0W](https://www.raspberrypi.com/products/raspberry-pi-zero/)|[Waveshare Eink 2,13"](https://www.waveshare.com/2.13inch-e-paper-hat.htm "Eink 2,13")|[3D printed](https://cults3d.com/en/3d-model/gadget/coque-pwnagotchi-waveshare3-pisugar3-et-protection-d-ecran-plexiglass "3D printed")|[PiSugar 3](https://www.tindie.com/products/pisugar/pisugar-3-battery-for-raspberry-pi-zero/ "PiSugar 3")|[USB GPS Dongle](https://thepihut.com/products/usb-gps-receiver-compatible-with-raspberry-pi-lattepanda-jetson-nano "USB GPS Dongle")|2.8.9|

## Plugins
### [PiSugar3](https://github.com/nullm0ose/pwnagotchi-plugin-pisugar3)
Config:
```toml
main.plugins.pisugar3.enabled = true
main.plugins.pisugar3.shutdown = 1
```
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
Config:
```toml
main.plugins.pwnmenu.enabled = true
```
### [Powerutils](https://github.com/sn0wflakeAU/powerutils)
Config:
```toml
main.plugins.powerutils.enabled = true
```
### [GPSD Easy](https://github.com/jayofelony/pwnagotchi-torch-plugins/blob/main/gpsdeasy.py)
Config:
```toml
main.plugins.gpsdeasy.enabled = true
main.plugins.gpsdeasy.host = "127.0.0.1"
main.plugins.gpsdeasy.port = 2947
main.plugins.gpsdeasy.device = "/dev/ttyACM0"
main.plugins.gpsdeasy.baud = 9600
main.plugins.gpsdeasy.fields = ['fix']
```
```sh
sudo apt-get install gpsd gpsd-clients
```
### [Wardriver](https://github.com/cyberartemio/wardriver-pwnagotchi-plugin)
Config:
```toml
main.plugins.wardriver.enabled = true
main.plugins.wardriver.path = "/root/wardriver"
main.plugins.wardriver.ui.enabled = true
main.plugins.wardriver.ui.position.x = 5
main.plugins.wardriver.ui.position.y = 95

main.plugins.wardriver.wigle.enabled = true
main.plugins.wardriver.wigle.api_key = "YOURAPIKEYHERE"
main.plugins.wardriver.wigle.donate = false

main.plugins.wardriver.whitelist = []
```
### [Enable deauth](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_deauth.py)
Config:
```toml

```
### [Enable Assoc](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_assoc.py)
Config:
```toml
main.plugins.enable_assoc.enabled = true
```
### [Instattack](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/instattack.py)
Config:
```toml
main.plugins.enable_deauth.enabled = true
```
### [Clock](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/clock.py)
Config:
```toml
main.plugins.clock.enabled = true
```
### [EXP V2](https://github.com/Kaska89/pwnagotchi-EXPv2-plugin)
Config:
```toml
main.plugins.expv2.enabled = true
main.plugins.expv2.lvl_x_coord = 0
main.plugins.expv2.lvl_y_coord = 81
main.plugins.expv2.exp_x_coord = 38
main.plugins.expv2.exp_y_coord = 81
main.plugins.expv2.str_x_coord = 67
main.plugins.expv2.str_y_coord = 32
main.plugins.expv2.bar_symbols_count = 12
```
### [Tweak View](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/tweak_view.py)
Config:
```toml
main.plugins.tweak_view.enabled = true
```
### [Custom Faces](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD)
Config:
```toml
ui.faces.look_r = "/custom-faces/look_r.png"
ui.faces.look_l = "/custom-faces/look_l.png"
ui.faces.look_r_happy = "/custom-faces/look_r-happy.png"
ui.faces.look_l_happy = "/custom-faces/look_l-happy.png"
ui.faces.sleep = "/custom-faces/sleep.png"
ui.faces.sleep2 = "/custom-faces/sleep2.png"
ui.faces.awake = "/custom-faces/awake.png"
ui.faces.bored = "/custom-faces/bored.png"
ui.faces.intense = "/custom-faces/intense.png"
ui.faces.cool = "/custom-faces/cool.png"
ui.faces.happy = "/custom-faces/happy.png"
ui.faces.excited = "/custom-faces/excited.png"
ui.faces.grateful = "/custom-faces/grateful.png"
ui.faces.motivated = "/custom-faces/motivated.png"
ui.faces.demotivated = "/custom-faces/demotivated.png"
ui.faces.smart = "/custom-faces/smart.png"
ui.faces.lonely = "/custom-faces/lonely.png"
ui.faces.sad = "/custom-faces/sad.png"
ui.faces.angry = "/custom-faces/angry.png"
ui.faces.friend = "/custom-faces/friend.png"
ui.faces.broken = "/custom-faces/broken.png"
ui.faces.debug = "/custom-faces/debug.png"
ui.faces.upload = "/custom-faces/upload.png"
ui.faces.upload1 = "/custom-faces/upload1.png"
ui.faces.upload2 = "/custom-faces/upload2.png"
ui.faces.png = true
ui.faces.position_x = 0
ui.faces.position_y = 34
```
