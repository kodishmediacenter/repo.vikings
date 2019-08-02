import xbmcaddon
import base64


host = "=wUYDZlTahHZTR3L3Fmcv02bj5icoNXZ0NXYw9yL6MHc0RHa"
tam = len(host)
basedem = host[::-1]
MainBase = base64.b64decode(basedem)
addon = xbmcaddon.Addon('plugin.video.keysey')