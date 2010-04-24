# -*- coding: utf-8 -*-
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

__all__ = ["translation", "widgets", "backend",
           "ServiceManager"]

import gtk
import gobject

from dbus.mainloop.glib import DBusGMainLoop

from service_manager_gtk.backend import ServiceIface
from service_manager_gtk.translation import _
from service_manager_gtk.utils import get_services
from service_manager_gtk.widgets import ServiceBox

class ServiceManager(gtk.VBox):
    """Main widget of service_manager_gtk"""
    def __init__(self):
        """init"""
        gtk.VBox.__init__(self, spacing=5)
        self._dbus_loop()
        self.iface = ServiceIface()
        self.items = []
        self.container = ServiceBox(self.on_item)
        self.iface.listen(self.listen_comar)
        self._create_ui()
        self.services = sorted(self.iface.services())
        self.add_items()
        self.iface.services(self.get_infos)
    def _dbus_loop(self):
        #runs dbus main loop
        DBusGMainLoop(set_as_default = True)
    def _create_ui(self):
        self.pack_start(self.container,
                        fill=True, expand=True)
        self.container.show()
        print "showed"
        #self.add_items()
    def add_items(self):
        """adds services to ServiceBox"""
        for service in self.services:
            self.container.add_item(service)
    def get_infos(self, name, exception, args):
        """get service info

        Arguments:
        - `name`: service name
        - `exception`: exception
        - `args`: args
        """
        if not exception:
            self.container.set_item(name, args)
    def on_item(self):
        print "TODO:on_item"
    def listen_comar(self, package, signal, args):
        print "TODO:listen_comar", package, signal, args

