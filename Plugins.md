# Plugins and mods

Consider this step OPTIONAL, unless you would like these custom plugins. Otherwise, proceed to Step 10.

Make custom-plugins directory defined in config.toml, if not done so already.

```sh
cd ~ sudo mkdir /usr/local/share/pwnagotchi/custom-plugins/
```

I usually use the default plugin directory.

*Plugins marked with &#42; are not tested by me yet, or needs some tweaking to work on my setup.*
Installation instruction and details soon

#### Step 9.1) Default plugins:
These plugins are provided in [**Jayofelonys repo**](https://github.com/jayofelony/pwnagotchi/releases/tag/v2.8.9 "Jayofelonys repo"), therefore if you have a full config.toml, the settings should be in your config.toml as well. 
[auto-update](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/auto-update.py)
	I usually leave it turned off, and update after the new release seems stable.

[bt-tether](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/bt-tether.py)
	See [Step 3](#step-3-build-your-initial-configtoml) and [Step 7](#step-7-bluetooth-connection-manually).

[fix-services](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/fix_services.py)
	Updated watchdog plugin to avoid the blindbug issue.

**[gdrivesync](https://github.com/jayofelony/pwnagotchi/blob/master/README-google.md)***
	Not tested, but I would like to use something like this, to backup my pwnys automatically to a server (preferably to one of my NAS).

**[gpio_buttons](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/gpio_buttons.py)***
    There are some issues with GPIO in the latest builds, I use it to control the pwnmenu.

[grid](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/grid.py)
    Sending data to [the grid](https://opwngrid.xyz/)

[logtail](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/logtail.py)
    Useful tool in the webUI, to check your logs without ssh.

[memtemp](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/memtemp.py)
    Shows system information on the screen (CPU temperature; load and memory load).

[onlinehashcrack](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/onlinehashcrack.py)
    Automatically uploads handshakes to [onlinehashcrack.com](https://onlinehashcrack.com).

[session-stats](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/session-stats.py)
    Displays stats of the current session in the webUI.

[webcfg](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/webcfg.py)
    Editor for your config.toml file in the webUI.

[webgpsmap](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/webgpsmap.py)
    Shows GPS location of your handshakes on a map.

[wpa-sec](https://github.com/jayofelony/pwnagotchi/blob/master/pwnagotchi/plugins/default/wpa-sec.py)
    Automatically uploads handshakes to [wpa-sec](https://wpa-sec.stanev.org).

#### Step 9.2) 3rd party plugins and mods:

[Clock](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/clock.py)
	Clock/Calendar for pwnagotchi

[PiSugar3](https://github.com/nullm0ose/pwnagotchi-plugin-pisugar3)
	The PiSugar 3 Plugin displays the battery percentage as well as the charging status on your Pwnagotchi's UI.

[Powerutils](https://github.com/sn0wflakeAU/powerutils)
	The Powerutils plugin lets you run the Pwnagotchi's internal shutdown, restart, or reboot functions, instead of the system "shutdown" command. By using the internal functions, you can access other features such as syncing the AI data before shutdown, or switching between AUTO and MANU mode.

[Pwnmenu](https://github.com/sn0wflakeAU/pwnmenu/)
	Pwnmenu is a plugin that lets you run scripts on a Pwnagotchi using the 2.13 inch Waveshare e-paper display. You can use it to select and call scripts to extend the functionality of the host Raspberry Pi Zero W.
To do this, the Pwnmenu can be controlled with terminal commands bound to GPIO pins.

[Custom Faces](https://github.com/roodriiigooo/PWNAGOTCHI-CUSTOM-FACES-MOD)
	A mod that allows you to use custom images as pwnagotchi Faces with transparency feature (.png) and themed plugins.

[Tweak View](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/tweak_view.py)
	Editor for the UI layout.

**[Fancygotchi](https://github.com/V0r-T3x/pwnagotchi-fancygotchi)***
	Theme manager for the Pwnagotchi. **NOT WORKING WITH JAYS IMAGE AT THE MOMENT!!!**

[GPSD Easy](https://github.com/jayofelony/pwnagotchi-torch-plugins/blob/main/gpsdeasy.py)
Uses gpsd to report lat/long on the screen and setup bettercap pcap gps logging. Better than the baked in GPS plugin. The plugin should install gpsd automatically, but it can take a long time, especially with BT internet sharing. Before enabling the plugin for the first time you can install GPSD manually from the terminal:
```sh
sudo apt-get install gpsd gpsd-clients
```

[Wardriver](https://github.com/cyberartemio/wardriver-pwnagotchi-plugin)
	A simple plugin for wardriving on your pwnagotchi.

[Enable deauth](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_deauth.py) / [Enable Assoc](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/enable_assoc.py)
	Enable and disable **DEAUTH** and **ASSOC** attacks on the fly. Enabled when plugin loads, disabled when plugin unloads.

**[Touch UI](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/Touch_UI.py)***
	Use touchscreen input to toggle settings.

[Instattack](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/instattack.py)
	Pwn more aggressively. Launch immediate associate or deauth attack when bettercap spots a device.

[EXP V2](https://github.com/Kaska89/pwnagotchi-EXPv2-plugin)
	Get exp every time a handshake get captured. You can add the Age plugin too, but I reflash my build so often that EXP is more than enough for my pwnys.

**[Achievement](https://github.com/LegendEvent/pwnagotchi-custom-plugins/blob/main/achievements.py)***
	Collect achievements for daily challenges.

[Shower Thoughts](https://github.com/NoxiousKarn/Showerthoughts)
	Displays random r/showerthoughts headlines on your pwnagotchi when the device is waiting. You need to modify core files, which are rewritten to default whith autoupdate. Thinking about changing to [RSS Voice](https://github.com/Sniffleupagus/pwnagotchi_plugins/blob/main/rss_voice.py) plugin in the future