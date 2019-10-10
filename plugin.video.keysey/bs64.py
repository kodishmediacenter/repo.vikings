import xbmcaddon
import base64


host = "=YjdJ5UUkhlUSZ3L3FmcvMWasJWdw9SZulGbu9mLhJnY29mL5V2alR3chB3LvoDc0RHa"
tam = len(host)
basedem = host[::-1]
MainBase = base64.b64decode(basedem)
addon = xbmcaddon.Addon('plugin.video.keysey')