# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PluginGpul
                                 A QGIS plugin
 plugin desarrollado en GRUP LAb
                             -------------------
        begin                : 2016-04-13
        copyright            : (C) 2016 by Bundless
        email                : lpirelli@boundlessgeo.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PluginGpul class from file PluginGpul.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .plugin_gpul import PluginGpul
    return PluginGpul(iface)
