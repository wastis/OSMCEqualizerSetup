#	This file is part of OSM Equalizer Setup for Kodi.
#
#	Copyright (C) 2022 wastis    https://github.com/wastis/BluetoothManager
#
#	Bluetooth Manager is free software; you can redistribute it and/or modify
#	it under the terms of the GNU Lesser General Public License as published
#	by the Free Software Foundation; either version 3 of the License,
#	or (at your option) any later version.
#
#

import xbmcgui
import xbmcaddon
from subprocess import Popen, PIPE
import os
from xbmcgui import ListItem
from log import log
from handle import handle

addon = xbmcaddon.Addon()
def tr(lid):
	return addon.getLocalizedString(lid)

class MenuGui(  xbmcgui.WindowXMLDialog  ):
	def __init__( self, *_args, **kwargs ):
		self.cwd = _args[1]
		self.icon_path = self.cwd + "resources/skins/Default/media/"
		self.allow_input = False
		self.script = kwargs["script"]
		self.message = kwargs["message"]

	def onInit( self ):
		self.textbox = self.getControl(2000)
		self.execute()

	def execute(self):
		try:
			p = Popen(["/usr/bin/sudo","/usr/bin/sh",os.path.join(self.cwd,"resources","lib",self.script)], stdout=PIPE, stdin=PIPE, stderr=PIPE)
			txt = []
			errors = []
			cnt = 0
			template = "%d"

			# stout
			for line in iter(p.stdout):
				t = line.decode()[:-1]
				if t.startswith("next:"):
					template = t[5:] + " %d"
					cnt = 0
					txt.append(template % cnt)
				elif t.startswith("error:"):
					errors.append(t)
				else:
					cnt += 1
					txt[-1] = template % cnt

				self.textbox.setText("[CR]".join(txt))

			# sterr
			for line in iter(p.stderr):
				t = line.decode()[:-1].replace("\\n","[CR]")
				if t.startswith("WARNING"):
					continue
				if t in ["","dpkg-preconfigure: unable to re-open stdin: No such file or directory"]:
					continue
				errors.append(t)
				log("'%s'" % errors[-1])

			txt.append("")
			txt.append("System update script is finished")
			self.allow_input = True

			# show message
			if len(errors)>0:
				xbmcgui.Dialog().ok(tr(32000),tr(32004))
				self.close()
			else:
				xbmcgui.Dialog().ok(tr(32002),tr(self.message))
				self.close()
		except Exception as e:
			handle(e)

	#
	# dialog action handling
	#

	def end_gui(self):
		if self.allow_input:
			self.close()

	def ok_pressed(self):
		if self.allow_input:
			self.close()

	def onAction( self, action ):
		log("action id %s" % action.getId())

		#OK pressed
		if action.getId() in [7, 100]:
			self.ok_pressed()

		#Cancel / Fullscreen
		if action.getId() in [92,10,18]:
			self.end_gui()
