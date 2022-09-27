# OSMC Equalizer Setup

A Kodi addon simplifying the installation of pulseaudio equalizer on OSMC systems.

Tested on raspberry pi 3b, OSMC 9/22, Kodi 19.4.

It installs pulseaudio together with the required modules and the [*Linux Addon Repository*](https://github.com/wastis/LinuxAddonRepo). It further configures the system to run with pulseaudio. 

Version 1.0.0

<img src="resources/media/icon.png" alt="drawing" width="200"/> 

# Installation

- Download latest [zip](https://github.com/wastis/OSMCEqualizerSetup/archive/refs/tags/v1.0.0.zip) from releases.
- In OSMC, select install from zip and install this addon.
- Now it is possible to select different scripts in the OSMC Equalizer Setup settings.

#### Install from zip
	settings -> Add-on browser -> Install from zip file

#### Prepare System
	settings -> Add-on brower -> My add-ons -> Program add-ons -> Equalizer Setup -> Configure
	
	Install -> Prepare System with Pulseaudio

#### Reboot
Reboot is important to start OSMC with pulseaudio. 

#### Enable the Linux Addon Repository
	settings -> Add-on browser -> My add-ons -> Add-on repository -> Linux Addon Repository -> enable

#### Install Pulseaudio Interface
	settings -> Add-on browser -> Install from repository -> Linux Addon Repository -> Program add-ons -> Pulse Equalizer

#### Direct audio though pulseaudio
	settings -> System -> Audio -> Audio output device -> Pulseaudio Sound Server


# Bluetooth devices with Equalizer
Pulseaudio is in conflict with ALSA if it comes to bluetooth devices. Therefore alsa-bluetooth needs to be disabled, when bluetooth shall be used with pulseaudio equalizer.

	settings -> Add-on browser -> My add-ons -> Program add-ons -> Equalizer Setup -> Configure
	
	Install -> Disable Alsa Bluetooth

# Revert everything

#### Remove Pulseaudio from the System
	settings -> Add-on brower -> My add-ons -> Program add-ons -> Equalizer Setup -> Configure
	
	Remove -> Remove Pulseaudio from System

#### Enable ALSA Bluetooth
	settings -> Add-on brower -> My add-ons -> Program add-ons -> Equalizer Setup -> Configure
	
	Remove -> Enable Alsa Bluetooth

# Behind the Scenes

There are four shell scripts that also could be launched from command line. 
They are located in  

	./kodi/addons/script.equalizersetup.osmc/resources/lib/



**install_equalizer**: Install pulseaudio, pulseaudio-equalizer, swh-plugins,pulseaudio-module-bluetooth, alters the OSMC startup script, downloads and installs the *Linux Addon Repository*

**remove_equalizer**: removes pulseaudio, pulseaudio-equalizer, swh-plugins,pulseaudio-module-bluetooth from the system, recovers original OSMC startup script

**disable_alsa_blue**: stops and disables bluealsa.service

**enable_alsa_blue**: enables and starts bluealsa.service

Those script are launched with sudo -u osmc, obviously they need root access to make the changes to the system. Currently there is no password request by osmc for sudo, this might change in the future. In this case this addon needs to be altered. 


2022 wastis


