# -*- coding: utf-8 -*-
"""Service Manager widgets

ServiceItem - service item widget
ServiceBox - holds ServiceItems
"""

#
# Rıdvan Örsvuran (C) 2010
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import gtk
import gobject

from service_manager_gtk.translation import _
from service_manager_gtk.utils import get_image
from service_manager_gtk.utils import get_icon

class ServiceItem(gtk.Table):
    """service item widget"""
    def __init__(self, name, stype, desc, state):
        """init
        Arguments:
        - `name`: service name
        - `stype`: service type
        - `desc`: service description
        - `state`: (on|off|started|stopped)
        """
        gtk.Table.__init__(self, rows=2, columns=6)
        self._name = name
        self._type = stype
        self._desc = desc
        self._state = state
        self._set_style()
        self._create_ui()
    def _set_style(self):
        # set style of table
        self.set_col_spacings(5)
        self.set_row_spacings(5)
    def is_auto(self):
        """returns True if run at startup is true"""
        return (self._state == 'on') | (self._state == 'stopped')
    def is_running(self):
        """return True if service is running"""
        return (self._state == 'on') | (self._state == 'started')
    def _create_ui(self):
        #create ui
        self.icon = gtk.Image()

        self.name_lb = gtk.Label()
        self.name_lb.set_markup("<b>"+self._name+"</b>")
        self.name_lb.set_alignment(0.0, 0.5)

        self.desc_lb = gtk.Label(self._desc)
        self.desc_lb.set_alignment(0.0, 0.5)

        self.start_btn = gtk.Button()
        self.start_btn.set_image(get_image('media-playback-start', 16))
        self.start_btn.set_tooltip_text(_('Start Service'))

        self.restart_btn = gtk.Button()
        self.restart_btn.set_image(get_image('view-refresh', 16))
        self.restart_btn.set_tooltip_text(_('Restart Service'))

        self.stop_btn = gtk.Button()
        self.stop_btn.set_image(get_image('media-playback-stop', 16))
        self.stop_btn.set_tooltip_text(_('Stop Service'))

        self.auto_cb = gtk.CheckButton(_('Run at startup'))

        self.attach(self.icon, 0, 1, 0, 2,
                    gtk.SHRINK, gtk.SHRINK)
        self.attach(self.name_lb, 1, 2, 0, 1,
                    gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        self.attach(self.desc_lb, 1, 2, 1, 2,
                    gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        self.attach(self.start_btn, 2, 3, 0, 2,
                    gtk.SHRINK, gtk.SHRINK)
        self.attach(self.restart_btn, 3, 4, 0, 2,
                    gtk.SHRINK, gtk.SHRINK)
        self.attach(self.stop_btn, 4, 5, 0, 2,
                    gtk.SHRINK, gtk.SHRINK)
        self.attach(self.auto_cb, 5, 6, 0, 2,
                    gtk.SHRINK, gtk.SHRINK)

        self.show_all()
        self._update_ui()
    def update(self, values):
        """update values"""
        if values[0]:
            self._type = values[0]
        if values[1]:
            self._desc = values[1]
        if values[2]:
            self._state = values[2]
        self._update_ui()
    def _update_ui(self):
        self.auto_cb.set_active(self.is_auto())
        self.desc_lb.set_text(self._desc)
        if self.is_running():
            icon_name = 'flag-green'
            tip = _('Service is running')
        else:
            icon_name = 'flag-black'
            tip = _('Service is not running')
        self.icon.set_from_pixbuf(get_icon(icon_name, 32))
        self.icon.set_tooltip_text(tip)
    def listen_signals(self, func):
        """listen signals

        Arguments:
        - `func`: callback function
        """
        callback_data = lambda x: {'action':x,
                                   'name':self._name,
                                   'item':self}
        self.start_btn.connect('clicked', func,
                               callback_data('start'))
        self.restart_btn.connect('clicked', func,
                                 callback_data('restart'))
        self.stop_btn.connect('clicked', func,
                              callback_data('stop'))
        self.auto_cb.connect('pressed', func,
                             callback_data('auto'))
gobject.type_register(ServiceItem)

class ServiceBox(gtk.ScrolledWindow):
    """holds ServiceItems"""
    def __init__(self, callback_func):
        """init
        Arguments:
        - `callback_func`: callback function
        """
        gtk.ScrolledWindow.__init__(self)
        self._func = callback_func
        self.vbox = gtk.VBox(spacing=5)
        self.services = {}
        self._set_style()
        self._create_ui()
    def _set_style(self):
        self.set_shadow_type(gtk.SHADOW_IN)
        self.set_policy(gtk.POLICY_NEVER,
                        gtk.POLICY_AUTOMATIC)
    def _create_ui(self):
        self.add_with_viewport(self.vbox)
        self.vbox.show()
    def add_item(self, name, stype='', desc='', state=''):
        """adds a ServiceItem

        Arguments:
        - `name`: service name
        - `stype`: type (local, server, etc.)
        - `desc`: service description
        - `state`: service state
        """
        item = ServiceItem(name, stype, desc, state)
        item.listen_signals(self._func)
        self.vbox.pack_start(item, expand=False)
        self.services[name] = {'widget':item}
        self.set_item(name, (stype, desc, state))
    def set_item(self, name, info):
        """set item values

        Arguments:
        - `name`: service name
        - `info`: (type, desc, state)
        """
        self.services[name]['values'] = info
        self.services[name]['widget'].update(info)
