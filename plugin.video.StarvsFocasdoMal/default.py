# -*- coding: utf-8 -*-
#------------------------------------------------------------
# 
#------------------------------------------------------------
# Licença: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Baseado no código do addon youtube
#------------------------------------------------------------

import os
import sys
import time
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.StarvsFocasdoMal'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_CHANNEL_ID1= "PLfp1JBJztVEExHclODttQJVO80k22Zsyr"
YOUTUBE_CHANNEL_ID2= "PLfp1JBJztVEFlc6Heu_gQk1JjIBZWByzo"
YOUTUBE_CHANNEL_ID3= "PLfp1JBJztVEEAaWz5oEKWr7O5nvocqzO9"


# Ponto de Entrada
def run():
	# Pega Parâmetros
	params = plugintools.get_params()
	
	if params.get("action") is None:
		xbmc.Player().play(entryurl)
		
		while xbmc.Player().isPlaying():
			time.sleep(1)

		main_list(params)
	else:
		action = params.get("action")
		exec action+"(params)"

	plugintools.close_item_list()

# Menu Principal
def main_list(params):
	plugintools.log("StarvsFocasdoMal.main_list "+repr(params))
	
	plugintools.log("StarvsFocasdoMal.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "1º Temporada",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "2º Temporada",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "3º Temporada",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon,
		folder = True )

run()
