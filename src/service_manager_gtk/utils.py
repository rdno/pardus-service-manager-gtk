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

import gtk
import gobject

def open_error_dialog(text):
    """opens a gtk error dialog"""
    dialog = gtk.MessageDialog(type=gtk.MESSAGE_ERROR,
                               buttons=gtk.BUTTONS_OK,
                               message_format=text)
    dialog.run()
    dialog.destroy()

def get_icon(name, size=32, flags=0):
    """gets icon from gtk.IconTheme return Pixbuf

    Arguments:
    - `name`: icon name
    - `size`: icon size
    - `flags`: the flags modifying the behavior of the icon lookup
    """
    it = gtk.icon_theme_get_for_screen(gtk.gdk.Screen())
    try:
        return it.load_icon(name, size, flags)
    except gobject.GError, e:
        print unicode(e)

def get_image(name, size=32, flags=0):
    """gets icon from gtk.IconTheme return as Image

    Arguments:
    - `name`: icon name
    - `size`: icon size
    - `flags`: the flags modifying the behavior of the icon lookup
    """
    return gtk.image_new_from_pixbuf(get_icon(name, size, flags))

