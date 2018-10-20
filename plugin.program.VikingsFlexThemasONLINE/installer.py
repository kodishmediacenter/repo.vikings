##==============
## Installer
##===============
import xbmc,xbmcaddon,xbmcgui,os,time
import skindefault
import downloader
import extract
import common
import shutil

AddonID = 'plugin.program.VikingsThemasON'
ADDON=xbmcaddon.Addon(id='plugin.program.VikingsFlexThemasONLINE')
HOME =  xbmc.translatePath('special://home/')   
AddonTitle = "[COLOR aqua]Vikings Kodi Wizard[/COLOR]"
VERSION = xbmcaddon.Addon().getAddonInfo('version')
PATH = xbmcaddon.Addon().getAddonInfo('name')
directory = xbmc.translatePath('special://thumbnails')
packages = xbmc.translatePath(os.path.join('special://home/addons','packages/'))
limpei = xbmc.translatePath(os.path.join('special://home/media','backgrounds/'))

##============
##   WIZARD
##============
def WIZARD(name,url,description):
    if not os.path.exists(packages): os.makedirs(packages)
    skindefault.SetDefaultSkin()
    if os.path.exists(limpei): shutil.rmtree(limpei)
    KODIVERSION = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
    dialog = xbmcgui.Dialog()
    if KODIVERSION < 16.0:
        dialog.ok("[COLOR=red][B]Atencao !!! [/COLOR][/B]", "Seu dispositivo possui uma versao antiga do Kodi que deve ser atualizada.")
        return
    else:
        dp = xbmcgui.DialogProgress()
        dp.create(AddonTitle,"Carregando a ultima compilacao... ",'','Por favor aguarde...')
        path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
        lib=os.path.join(path, name+'.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib, dp)
        time.sleep(2)
        addonfolder = xbmc.translatePath(os.path.join('special://','home'))
        dp.update(0,"", "Extraindo arquivos do ZIP...")
        extract.all(lib,addonfolder,dp)
        common.killxbmc()