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

def get_services(iface):
    """get services as a dict

    Arguments:
    - `iface`: backend.ServiceIface
    """
    services = iface.services()
    for service in services:
        i = iface.info(service)
        yield {"name": service,
               "type": i[0],
               "desc": i[1],
               "state":i[2]}
    #return service_dict
