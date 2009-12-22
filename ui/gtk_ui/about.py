# -*- coding: utf-8 -*-

# Ventana para subir el ego de los desarrolladores de Turpial xD
#
# Author: Wil Alvarez (aka Satanas)
# Dic 21, 2009

import gtk

from ui import util as util

class About:
    def __init__(self):
        about=gtk.AboutDialog()
        about.set_logo(util.load_image('turpial_icon.png', True))
        about.set_name('Turpial')
        about.set_version('0.8')
        about.set_copyright('Copyleft (C) 2009 Wil Alvarez - Eleazar Meza')
        about.set_comments('Cliente de Twitter multi-interfaz escrito en Python')
        
        try:
            lic = file('COPYING', 'r')
            license=lic.read()
        except:
            license='This script is free software; you can redistribute it'
            'and\/or modify it under the\n\terms of the GNU General Public '
            'License as published by the Free Software\n\Foundation; either '
            'version 3 of the License, or (at your option) any later version.'
            '\n\n\You should have received a copy of the GNU General Public '
            'License along with\n\this script (see license); if not, write to '
            'the Free Software\n\Foundation, Inc., 59 Temple Place, Suite 330, '
            'Boston, MA  02111-1307  USA'
        about.set_license(license)
        about.set_authors([
            'Wil A. Alvarez aka Satanas (Concepto y programación)',
            'Eleazar Meza aka Shaka (Concepto y arte)',
        ])
        
        about.connect("response", self.__response)
        about.connect("close", self.__close)
        about.connect("delete_event", self.__close)
        
        about.run()
        
    def __response(self, dialog, response, *args):
        if response < 0:
            dialog.destroy()
            dialog.emit_stop_by_name('response')
        
    def __close(self, widget, event=None):
        widget.destroy()
        return True