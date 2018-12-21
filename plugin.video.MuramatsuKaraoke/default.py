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

addonID = 'plugin.video.MuramatsuKaraoke'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

addonfolder = local.getAddonInfo('path')
resfolder = addonfolder + '/resources/'
entryurl=resfolder+"entrada.mp4"

YOUTUBE_CHANNEL_ID1=  "PLgFrDSKYT2CMlgFuuuGT5f-gk_0JDDj0R"
YOUTUBE_CHANNEL_ID2=  "PLgFrDSKYT2CMJd9rJhUmUVKvMjxUK2lCk"
YOUTUBE_CHANNEL_ID3=  "PLgFrDSKYT2CNx-vXZyUf47sraP0t5XdmI"
YOUTUBE_CHANNEL_ID4=  "PLgFrDSKYT2CP7Y9xd8pcsU_edYFwiQC01"
YOUTUBE_CHANNEL_ID5=  "PLgFrDSKYT2COR8WNnRrYxNkKqx3GfLjux"
YOUTUBE_CHANNEL_ID6=  "PLgFrDSKYT2CORbuWeU34siSu2VDEV369D"
YOUTUBE_CHANNEL_ID7=  "PLgFrDSKYT2CMx-0_tGK2_DQAfnJK77omh"
YOUTUBE_CHANNEL_ID8=  "PLgFrDSKYT2CN4ZMJOLb6-cSKJ2jZSOdEA"
YOUTUBE_CHANNEL_ID9=  "PLgFrDSKYT2CMDrgkNMEVLXR-Ja9-wXkeF"
YOUTUBE_CHANNEL_ID10= "PLgFrDSKYT2CPIDYEph5rFJvxc_7sK5Tqt"
YOUTUBE_CHANNEL_ID11= "PLgFrDSKYT2CNRnJ9_UqKCWv89f_ChOJSF"
YOUTUBE_CHANNEL_ID12= "PLgFrDSKYT2CPf8TwTqmNu_LRta1y9Q9sJ"



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
	plugintools.log("Muramatsu.main_list "+repr(params))
	
	plugintools.log("Muramatsu.run")
	
	#plugintools.direct_play(str(entryurl))

	plugintools.add_item(
		title = "Arrocha",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID1+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Axe",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID2+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Brega/Classicos",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID3+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Eletronico/Party",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID4+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Forro",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID5+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Funk / Funk Melody e Funk Carioca",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID6+"/",
		thumbnail = icon,
		folder = True )
	
	plugintools.add_item(
		title = "Gospel/Sacra/Crista",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID7+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Hip-Hop",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID8+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "MPB",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID9+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Pagode",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID10+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Parodia",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID11+"/",
		thumbnail = icon,
		folder = True )

	plugintools.add_item(
		title = "Pop",
		url = "plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID12+"/",
		thumbnail = icon,
		folder = True )

run()
