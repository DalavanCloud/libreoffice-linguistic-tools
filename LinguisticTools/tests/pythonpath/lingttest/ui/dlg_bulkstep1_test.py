# -*- coding: Latin-1 -*-
#
# This file created 11-Feb-2016 by Jim Kornelsen
#
# 21-May-16 JDK  Updated because step 1 ctrls have their own classes now.

"""
Tests the bulk conversion step 1 dialog.
Does not test the "Scan Files" button, because that goes beyond the UI.
"""
import logging
import os
import unittest

from lingt.ui.comp.bulkconv import DlgBulkConversion
from lingt.utils import util

from lingttest.utils import testutil

logger = logging.getLogger("lingttest.dlg_bulkstep1_test")


def getSuite():
    suite = unittest.TestSuite()
    for method_name in (
            'test1_',
            'test2_',
        ):
        suite.addTest(DlgBulkStep1TestCase(method_name))
    return suite


class DlgBulkStep1TestCase(unittest.TestCase):
    def __init__(self, testCaseName):
        unittest.TestCase.__init__(self, testCaseName)
        testutil.modifyClass_showDlg(DlgBulkConversion)

    def setUp(self):
        self.unoObjs = testutil.unoObjsForCurrentDoc()
        self.dlg = None

    def runDlg(self, dispose):
        self.dlg = DlgBulkConversion(self.unoObjs)
        self.dlg.showDlg()
        if dispose:
            testutil.do_dispose(self.dlg)
            self.dlg = None

    def test1(self):
        def useDialog(innerSelf):
            stepForm = innerSelf.step1Form
            filesList = stepForm.filesList
            outputTo = stepForm.outputTo

            self.assertEqual(outputTo.txtOutputTo.getText(), "")
            self.assertEqual(len(filesList.fileItems), 0)
            filepath = os.path.join(
                util.TESTDATA_FOLDER, "TbxIntJPDN60.xml")
            filesList.addFile(filepath)
            dirname = os.path.dirname(filepath)
            #innerSelf.evtHandler.actionPerformed(
            #    MyActionEvent("FileUpdate"))
            self.assertEqual(outputTo.txtOutputTo.getText(), dirname)
            self.assertEqual(len(filesList.fileItems), 1)
        DlgBulkConversion.useDialog = useDialog
        #self.dlg.showDlg()
        self.runDlg(True)


if __name__ == '__main__':
    testutil.run_suite(getSuite())
