# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'user@ugatu.su'
__date__ = '2019-09-16'
__copyright__ = 'Copyright 2019, Niyaz Lutfullin'

import unittest

from qgis.PyQt.QtGui import QDockWidget

from vector_worker_dockwidget import VectorWorkerDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class VectorWorkerDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = VectorWorkerDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(VectorWorkerDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

