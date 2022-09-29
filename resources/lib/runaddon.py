#	This file is part of Shell Script Launcher for Kodi.
#
#	Copyright (C) 2021 wastis    https://github.com/wastis/PulseEqualizerGui
#
#	PulseEqualizerGui is free software; you can redistribute it and/or modify
#	it under the terms of the GNU Lesser General Public License as published
#	by the Free Software Foundation; either version 3 of the License,
#	or (at your option) any later version.
#
#

import os
import sys
import subprocess

import xbmcaddon
import xbmc
import xbmcgui

from log import log
from handle import handle

from menu import MenuGui

addon = xbmcaddon.Addon()
def tr(lid):
	return addon.getLocalizedString(lid)

def run_addon():
	try:
		cwd = xbmcaddon.Addon().getAddonInfo('path')

		#
		#  check if the os is OSMC
		#

		if False:
			try:
				with open("/etc/os-release", "r") as f:
					content = f.read()
					if not "Open Source Media Center" in content:
						xbmcgui.Dialog().ok(tr(32000),tr(32001))
						return
			except FileNotFoundError:
				xbmcgui.Dialog().ok(tr(32000),tr(32001))
				return

		#
		#	get script name
		#

		try:
			script = sys.argv[1]
		except IndexError:
			xbmcgui.Dialog().ok(tr(32002),tr(32003))
			return

		if script == "install_equalizer":
			msg = 32005
		elif script == "disable_alsa_blue":
			msg = 32007
		elif script == "remove_equalizer":
			msg = 32006
		elif script == "enable_alsa_blue":
			msg = 32008
		elif script == "restore_pa_setting":
			msg = 32010
		else: return

		#
		#   warning mssages
		#

		if not xbmcgui.Dialog().yesno(tr(32002),tr(32009)):
			return

		#
		# show menu dialog
		#

		current_skin = xbmc.getSkinDir()

		if os.path.exists(os.path.join(cwd,"resources","skins",current_skin)):
			skin = current_skin
		else:
			skin = "Default"

		ui = MenuGui("menu.xml", cwd, skin, "1080i", script = script, message = msg)
		ui.doModal()

	except Exception as e:
		handle(e)
