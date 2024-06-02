# Blender Add-on Template
# Contributor(s): Aaron Powell (aaron@lunadigital.tv)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy
from . import ui, properties, bake
if 'bpy' in locals():
    import importlib
    importlib.reload(properties)
    importlib.reload(bake)
    importlib.reload(ui)

bl_info = {
        "name": "Animated Texture Baker",
        "description": "Addon for baking animated Materials and Textures to image sequence.",
        "author": "Soroush Azari",
        "version": (1, 0),
        "blender": (3, 40, 0),
        "location": "View3d > Sidebar > Animated Texture Baker",
        "warning": "", # used for warning icon and text in add-ons panel
        "wiki_url": "http://my.wiki.url",
        "tracker_url": "http://my.bugtracker.url",
        "support": "COMMUNITY",
        "category": "Render"
        }


#
# Add additional functions here
#

def register():
    properties.register()
    bake.register()
    ui.register()

def unregister():
    properties.unregister()
    bake.unregister()
    ui.unregister()

if __name__ == '__main__':
    register()
