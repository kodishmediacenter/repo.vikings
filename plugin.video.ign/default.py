# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/ncs
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

addonID = 'plugin.video.ign'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"


YOUTUBE_CHANNEL_ID1 = "channel/UCfg4PAgKIurlvYJRhhukv_g/playlists"
icon1 = "https://yt3.ggpht.com/a-/AN66SAy2MKvILvtUHB-02erGCmsnsW1MWe3HbmVZ4Q=s288-mo-c-c0xffffffff-rj-k-no"

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
	plugintools.log("ign.main_list "+repr(params))
	
	plugintools.log("ign.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "IGN Brasil",
		url = "plugin://plugin.video.youtube/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail = icon1,
		folder = True )
		
	
run()
