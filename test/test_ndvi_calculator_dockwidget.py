# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'vrnkvknn@gmail.com'
__date__ = '2026-10-14'
__copyright__ = 'Copyright 2026, vrnk'

import unittest

from qgis.PyQt.QtWidgets import QDockWidget

from ndvi_calculator_dockwidget import NdviCalculatorDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class NdviCalculatorDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = NdviCalculatorDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test the dockwidget is a QDockWidget and exposes its closing signal."""
        self.assertIsInstance(self.dockwidget, QDockWidget)
        self.assertTrue(hasattr(self.dockwidget, 'closingPlugin'))

if __name__ == "__main__":
    suite = unittest.makeSuite(NdviCalculatorDockWidgetTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

