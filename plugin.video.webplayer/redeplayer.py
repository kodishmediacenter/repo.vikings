import xbmc
import os
import webbrowser


def browser_player(os,link):

    if os =='android':
        links = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( ''+link+'' ) )
    else:
        links = webbrowser . open ( ''+link+'' )










    
    
