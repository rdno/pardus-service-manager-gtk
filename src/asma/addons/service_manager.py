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
from asma.addon import AsmaAddon
from service_manager_gtk import ServiceManager
from service_manager_gtk.translation import _
class ServiceManagerAddon(AsmaAddon):
    """Service Manager Asma addon"""
    def __init__(self):
        """init the variables"""
        super(ServiceManagerAddon, self).__init__()
        self._uuid = "513d0f37-51aa-4124-959c-dfad32f63246"
        self._icon_name = "flag"
        self._label = _("Service Manager")
        self._widget = ServiceManager
