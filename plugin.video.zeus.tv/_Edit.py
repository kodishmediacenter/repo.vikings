import xbmcaddon
import zlib
import binascii

MainBase = zlib.decompress(binascii.unhexlify('789ccb28292928b6d2d72f482c2e494dcaccd34bcecfd52f4a2cd7cf0bc90e72ca750d0300d10b0c00'))
addon = xbmcaddon.Addon('plugin.video.zeus.tv')