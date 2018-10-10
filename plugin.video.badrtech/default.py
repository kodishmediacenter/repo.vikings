import xbmc
import xbmcgui
import webbrowser

def browser_player(os,link):

    if os =='android':
        links = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+link+'' ) )
    else:
        links = webbrowser . open ( ''+link+'' )


def redessociais(os):
    dialog = xbmcgui.Dialog()
    ret3 = dialog.select('[COLOR yellow]Badr For Tech[/COLOR]', ['Subscribe My Channel', 'Youtube Channel','Twitter'])
    if ret3 == 0:
        sub = "https://www.youtube.com/channel/UCVe-YrD8NfSXckQEP0BnHMg?sub_confirmation=1"
        browser_player(os,sub)
    if ret3 == 1:
        xbmc.executebuiltin("ActivateWindow(10025,plugin://plugin.video.youtube/channel/UCVe-YrD8NfSXckQEP0BnHMg/)")
    if ret3 == 2:
        face = "https://twitter.com/BadrForTech"
        browser_player(os,face)





if xbmc . getCondVisibility ('system.platform.android'):
    os = 'android'
    redessociais(os)
else:
    os = 'null'
    redessociais(os)
    
