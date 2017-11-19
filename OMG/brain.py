from __future__ import print_function
from __future__ import absolute_import
from bs4 import BeautifulSoup
try:
    from urllib.request import (Request, urlopen)
    from urllib.error import URLError
except:
    from urllib2 import (Request, urlopen, URLError)
import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import (Gtk, Notify, AppIndicator3)
import signal
import webbrowser

url = 'http://www.omgubuntu.co.uk'
icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo.png')
IDENTITY = 'my indicator'
Notify.init("my app")


def desktop():
    environ = os.environ.get('DESKTOP_SESSION')
    if environ is not None:
        environ = environ.lower()
        if environ in ['gnome', 'gnome-classic', 'cinnamon', 'gnome-xorg', 'budgie', 'pantheon']:
            return environ
        elif environ == 'ubuntu':
            return 'unity'
        elif environ == 'unity':
            return 'unity'
        elif os.environ.get('XDG_CURRENT_DESKTOP'):
            if 'GNOME' in os.environ.get('XDG_CURRENT_DESKTOP'):
                return 'gnome'
            elif 'unity' in os.environ.get('XDG_CURRENT_DESKTOP'):
                return 'unity'
    else:
        pass


def access():
    global links
    try:
        req = Request(url)
        soup = BeautifulSoup(urlopen(req), 'html.parser')
        info = soup.find(id='primary')
        links = [i['href'] for i in info.select('.entry-title a')]
        pre = [i.get_text() for i in info.select('.entry-title a')]
        display = links[0] + '\n' + pre[0]
        session = desktop()
        if session in ['gnome', 'gnome-classic', 'cinnamon', 'gnome-xorg', 'budgie', 'pantheon']:
            Notify.Notification.new("UbuntuNews", display, icon).show()
            Notify.uninit()
        elif session == 'unity' or session == 'ubuntu':
            Notify.Notification.new("UbuntuNews", display, icon).show()
            indicator = AppIndicator3.Indicator.new(
                IDENTITY,
                icon,
                AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
            indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
            indicator.set_menu(menu_created())
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            Gtk.main()
    except URLError as e:
        print('[-] Cant\'t connect:', e.reason)
    return links[0]


def menu_created():
    menu = Gtk.Menu()
    item = Gtk.MenuItem('News')
    item.connect('activate', news)
    menu.append(item)
    item_quit = Gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu


def news(self):
    webbrowser.open(links[0])


def quit(self):
    Gtk.main_quit()


if __name__ == '__main__':
    access()
