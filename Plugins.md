
# Plugins and mods
If you managed to boot your pwnagotchi, and have your basic setup ready, you can try to play with the plugins (or even create one yourself).
Because every plugin is slightly different there is no one-for-all tutorial...
The basic steps are the same though....
Copy the `plugin.py` to your custom plugin folder and add the necessary config lines to your `config.toml` file.
Some plugins require just one line like 
```toml
main.plugins.pluginname.enabled = true
```
But some needs further settings or even modifying the core files in the pwnagotchi  folder. You have to read the readmes on github or check the code itself. Most of the time all the info is there, but I try to collect the important info here as well.

Make custom-plugins directory defined in config.toml, if not done so already.
```sh
cd ~ sudo mkdir /usr/local/share/pwnagotchi/custom-plugins/
```
I usually use the default plugin directory, but it is better to separate the built-in and 3rd party plugins.

*Plugins marked with &#42; are not tested by me yet, or needs some tweaking to work on my setup.*

## Default plugins:
These plugins are provided in [**Jayofelonys repo**](https://github.com/jayofelony/pwnagotchi/releases/tag/v2.8.9 "Jayofelonys repo"), therefore if you have a working pwnagotchi, you should have a full `config.toml` file , the default settings should be there as well. 

### [auto-update](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/auto-update.py)
I usually leave it turned off, and update manually after the new release seems stable.

### [bt-tether](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/bt-tether.py)
Plugin for connecting the pwnagotchi to your phone and share your internet via bluetooth,
See the build guide [Step 3](#step-3-build-your-initial-configtoml) and [Step 7](#step-7-bluetooth-connection-manually).

### [fix-services](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/fix_services.py)
Updated watchdog plugin to avoid the blindbug issue.

### **[gdrivesync](https://github.com/jayofelony/pwnagotchi/blob/master/README-google.md)***
Not tested, but I would like to use something like this, to backup my pwnys automatically to a server (preferably to one of my NAS).

### **[gpio_buttons](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/gpio_buttons.py)***
   There are some issues with GPIO in the latest builds, I use it to control the pwnmenu.

### [grid](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/grid.py)
   Sending data to [the grid](https://opwngrid.xyz/)

### [logtail](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/logtail.py)
   Useful tool in the webUI, to check your logs without ssh.

### [memtemp](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/memtemp.py)
Shows system information on the screen (CPU temperature; load and memory load).

### [onlinehashcrack](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/onlinehashcrack.py)
Automatically uploads handshakes to [onlinehashcrack.com](https://onlinehashcrack.com).

### [session-stats](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/session-stats.py)
Displays stats of the current session in the webUI.

### [webcfg](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/webcfg.py)
Editor for your config.toml file in the webUI.

### [webgpsmap](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/webgpsmap.py)
Shows GPS location of your handshakes on a map.

### [wpa-sec](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/wpa-sec.py)
Automatically uploads handshakes to [wpa-sec](https://wpa-sec.stanev.org).

## 3rd party plugins and mods:

### [Clock](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/clock.py)
Clock/Calendar for pwnagotchi
**Config:**
```toml
main.plugins.clock.enabled = true
```

### [PiSugar3](https://github.com/nullm0ose/pwnagotchi-plugin-pisugar3)
The PiSugar 3 Plugin displays the battery percentage as well as the charging status on your Pwnagotchi's UI.
****Config:****
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

### [Powerutils](https://github.com/sn0wflakeAU/powerutils)
The Powerutils plugin lets you run the Pwnagotchi's internal shutdown, restart, or reboot functions, instead of the system "shutdown" command. By using the internal functions, you can access other features such as syncing the AI data before shutdown, or switching between AUTO and MANU mode.
**Config:**
```toml
main.plugins.powerutils.enabled = true
```

### [Pwnmenu](https://github.com/sn0wflakeAU/pwnmenu/)
Pwnmenu is a plugin that lets you run scripts on a Pwnagotchi using the 2.13 inch Waveshare e-paper display. You can use it to select and call scripts to extend the functionality of the host Raspberry Pi Zero W.
To do this, the Pwnmenu can be controlled with terminal commands bound to GPIO pins.
**Config:**
```toml
main.plugins.pwnmenu.enabled = true
```

### [Custom Faces](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD)
A mod that allows you to use custom images as pwnagotchi Faces with transparency feature (.png) and themed plugins.
**Config:**
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

### [Tweak View](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/tweak_view.py)
Editor for the UI layout.
**Config:**
```toml
main.plugins.tweak_view.enabled = true
```

### **[Fancygotchi](https://github.com/V0r-T3x/pwnagotchi-fancygotchi)***
Theme manager for the Pwnagotchi. 

**NOT WORKING WITH JAYS IMAGE AT THE MOMENT!!!**
Please be patient, the plugin will be released when ready.


### [GPSD Easy](https://github.com/jayofelony/pwnagotchi-torch-plugins/blob/main/gpsdeasy.py)
Uses gpsd to report lat/long on the screen and setup bettercap pcap gps logging. Better than the baked in GPS plugin. The plugin should install gpsd automatically, but it can take a long time, especially with BT internet sharing. Before enabling the plugin for the first time you can install GPSD manually from the terminal:
```sh
sudo apt-get install gpsd gpsd-clients
```
**Config:**
```toml
main.plugins.gpsdeasy.enabled = true
main.plugins.gpsdeasy.host = "127.0.0.1"
main.plugins.gpsdeasy.port = 2947
main.plugins.gpsdeasy.device = "/dev/ttyACM0"
main.plugins.gpsdeasy.baud = 9600
main.plugins.gpsdeasy.fields = ['fix']
```

### [Wardriver](https://github.com/cyberartemio/wardriver-pwnagotchi-plugin)
A simple plugin for wardriving on your pwnagotchi.
**Config:**
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

### [Enable deauth](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_deauth.py) / [Enable Assoc](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_assoc.py)
Enable and disable **DEAUTH** and **ASSOC** attacks on the fly. Enabled when plugin loads, disabled when plugin unloads.
**Config:**
```toml
main.plugins.enable_deauth.enabled = true
```
```toml
main.plugins.enable_assoc.enabled = true
```

### **[Touch UI](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/Touch_UI.py)***
Use touchscreen input to toggle settings.

### [Instattack](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/instattack.py)
Pwn more aggressively. Launch immediate associate or deauth attack when bettercap spots a device.
**Config:**
```toml
main.plugins.instattack.enabled = true
```

### [EXP V2](https://github.com/Kaska89/pwnagotchi-EXPv2-plugin)
Get exp every time a handshake get captured. You can add the Age plugin too, but I reflash my build so often that EXP is more than enough for my pwnys.
**Config:**
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

### **[Achievement](https://github.com/LegendEvent/pwnagotchi-custom-plugins/blob/main/achievements.py)***
Collect achievements for daily challenges.

### [Shower Thoughts](https://github.com/NoxiousKarn/Showerthoughts)
Displays random r/showerthoughts headlines on your pwnagotchi when the device is waiting. You need to modify core files, which are rewritten to default whith autoupdate. Thinking about changing to [RSS Voice](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/rss_voice.py) plugin in the future
