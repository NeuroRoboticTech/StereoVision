# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'block_tuner.ui'
#
# Created: Thu Aug  4 08:09:05 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BlockTunerDlg(object):
    def setupUi(self, BlockTunerDlg):
        BlockTunerDlg.setObjectName(_fromUtf8("BlockTunerDlg"))
        BlockTunerDlg.resize(469, 671)
        self.buttonBox = QtGui.QDialogButtonBox(BlockTunerDlg)
        self.buttonBox.setGeometry(QtCore.QRect(110, 630, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.textP1 = QtGui.QLineEdit(BlockTunerDlg)
        self.textP1.setGeometry(QtCore.QRect(10, 40, 70, 30))
        self.textP1.setObjectName(_fromUtf8("textP1"))
        self.labelP1 = QtGui.QLabel(BlockTunerDlg)
        self.labelP1.setGeometry(QtCore.QRect(100, 20, 360, 20))
        self.labelP1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelP1.setObjectName(_fromUtf8("labelP1"))
        self.sliderP1 = QtGui.QSlider(BlockTunerDlg)
        self.sliderP1.setGeometry(QtCore.QRect(100, 40, 359, 29))
        self.sliderP1.setMaximum(1536)
        self.sliderP1.setOrientation(QtCore.Qt.Horizontal)
        self.sliderP1.setObjectName(_fromUtf8("sliderP1"))
        self.labelP2 = QtGui.QLabel(BlockTunerDlg)
        self.labelP2.setGeometry(QtCore.QRect(100, 80, 360, 20))
        self.labelP2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelP2.setObjectName(_fromUtf8("labelP2"))
        self.sliderP2 = QtGui.QSlider(BlockTunerDlg)
        self.sliderP2.setGeometry(QtCore.QRect(100, 100, 359, 29))
        self.sliderP2.setMaximum(1536)
        self.sliderP2.setOrientation(QtCore.Qt.Horizontal)
        self.sliderP2.setObjectName(_fromUtf8("sliderP2"))
        self.labelNumDisp = QtGui.QLabel(BlockTunerDlg)
        self.labelNumDisp.setGeometry(QtCore.QRect(100, 140, 360, 20))
        self.labelNumDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumDisp.setObjectName(_fromUtf8("labelNumDisp"))
        self.sliderNumDisp = QtGui.QSlider(BlockTunerDlg)
        self.sliderNumDisp.setGeometry(QtCore.QRect(100, 160, 359, 29))
        self.sliderNumDisp.setMaximum(1536)
        self.sliderNumDisp.setSingleStep(16)
        self.sliderNumDisp.setPageStep(32)
        self.sliderNumDisp.setOrientation(QtCore.Qt.Horizontal)
        self.sliderNumDisp.setObjectName(_fromUtf8("sliderNumDisp"))
        self.labelSpeckleRange = QtGui.QLabel(BlockTunerDlg)
        self.labelSpeckleRange.setGeometry(QtCore.QRect(100, 200, 360, 20))
        self.labelSpeckleRange.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeckleRange.setObjectName(_fromUtf8("labelSpeckleRange"))
        self.sliderSpeckleRange = QtGui.QSlider(BlockTunerDlg)
        self.sliderSpeckleRange.setGeometry(QtCore.QRect(100, 220, 359, 29))
        self.sliderSpeckleRange.setMaximum(2)
        self.sliderSpeckleRange.setSingleStep(1)
        self.sliderSpeckleRange.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSpeckleRange.setObjectName(_fromUtf8("sliderSpeckleRange"))
        self.labelFullDP = QtGui.QLabel(BlockTunerDlg)
        self.labelFullDP.setGeometry(QtCore.QRect(100, 320, 360, 20))
        self.labelFullDP.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFullDP.setObjectName(_fromUtf8("labelFullDP"))
        self.sliderFullDP = QtGui.QSlider(BlockTunerDlg)
        self.sliderFullDP.setGeometry(QtCore.QRect(100, 340, 359, 29))
        self.sliderFullDP.setMaximum(1)
        self.sliderFullDP.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFullDP.setObjectName(_fromUtf8("sliderFullDP"))
        self.labelDisp12MaxDiff = QtGui.QLabel(BlockTunerDlg)
        self.labelDisp12MaxDiff.setGeometry(QtCore.QRect(100, 380, 360, 20))
        self.labelDisp12MaxDiff.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDisp12MaxDiff.setObjectName(_fromUtf8("labelDisp12MaxDiff"))
        self.sliderDisp12MaxDiff = QtGui.QSlider(BlockTunerDlg)
        self.sliderDisp12MaxDiff.setGeometry(QtCore.QRect(100, 400, 359, 29))
        self.sliderDisp12MaxDiff.setMaximum(1536)
        self.sliderDisp12MaxDiff.setOrientation(QtCore.Qt.Horizontal)
        self.sliderDisp12MaxDiff.setObjectName(_fromUtf8("sliderDisp12MaxDiff"))
        self.labelMinDisparity = QtGui.QLabel(BlockTunerDlg)
        self.labelMinDisparity.setGeometry(QtCore.QRect(100, 500, 360, 20))
        self.labelMinDisparity.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMinDisparity.setObjectName(_fromUtf8("labelMinDisparity"))
        self.sliderMinDisparity = QtGui.QSlider(BlockTunerDlg)
        self.sliderMinDisparity.setGeometry(QtCore.QRect(100, 520, 359, 29))
        self.sliderMinDisparity.setMaximum(1536)
        self.sliderMinDisparity.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMinDisparity.setObjectName(_fromUtf8("sliderMinDisparity"))
        self.labelSADWindowSize = QtGui.QLabel(BlockTunerDlg)
        self.labelSADWindowSize.setGeometry(QtCore.QRect(100, 440, 360, 20))
        self.labelSADWindowSize.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSADWindowSize.setObjectName(_fromUtf8("labelSADWindowSize"))
        self.sliderSADWindowSize = QtGui.QSlider(BlockTunerDlg)
        self.sliderSADWindowSize.setGeometry(QtCore.QRect(100, 460, 359, 29))
        self.sliderSADWindowSize.setMaximum(11)
        self.sliderSADWindowSize.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSADWindowSize.setObjectName(_fromUtf8("sliderSADWindowSize"))
        self.labelSpeckleWindowSize = QtGui.QLabel(BlockTunerDlg)
        self.labelSpeckleWindowSize.setGeometry(QtCore.QRect(100, 260, 360, 20))
        self.labelSpeckleWindowSize.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeckleWindowSize.setObjectName(_fromUtf8("labelSpeckleWindowSize"))
        self.sliderSpeckleWindowSize = QtGui.QSlider(BlockTunerDlg)
        self.sliderSpeckleWindowSize.setGeometry(QtCore.QRect(100, 280, 359, 29))
        self.sliderSpeckleWindowSize.setMaximum(200)
        self.sliderSpeckleWindowSize.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSpeckleWindowSize.setObjectName(_fromUtf8("sliderSpeckleWindowSize"))
        self.textP2 = QtGui.QLineEdit(BlockTunerDlg)
        self.textP2.setGeometry(QtCore.QRect(10, 100, 70, 30))
        self.textP2.setObjectName(_fromUtf8("textP2"))
        self.textNumDisp = QtGui.QLineEdit(BlockTunerDlg)
        self.textNumDisp.setGeometry(QtCore.QRect(10, 160, 70, 30))
        self.textNumDisp.setObjectName(_fromUtf8("textNumDisp"))
        self.textSpeckleRange = QtGui.QLineEdit(BlockTunerDlg)
        self.textSpeckleRange.setGeometry(QtCore.QRect(10, 220, 70, 30))
        self.textSpeckleRange.setObjectName(_fromUtf8("textSpeckleRange"))
        self.textSpeckleWindowSize = QtGui.QLineEdit(BlockTunerDlg)
        self.textSpeckleWindowSize.setGeometry(QtCore.QRect(10, 280, 70, 30))
        self.textSpeckleWindowSize.setObjectName(_fromUtf8("textSpeckleWindowSize"))
        self.textFullDP = QtGui.QLineEdit(BlockTunerDlg)
        self.textFullDP.setGeometry(QtCore.QRect(10, 340, 70, 30))
        self.textFullDP.setObjectName(_fromUtf8("textFullDP"))
        self.textDisp12MaxDiff = QtGui.QLineEdit(BlockTunerDlg)
        self.textDisp12MaxDiff.setGeometry(QtCore.QRect(10, 400, 70, 30))
        self.textDisp12MaxDiff.setObjectName(_fromUtf8("textDisp12MaxDiff"))
        self.textSADWindowSize = QtGui.QLineEdit(BlockTunerDlg)
        self.textSADWindowSize.setGeometry(QtCore.QRect(10, 460, 70, 30))
        self.textSADWindowSize.setObjectName(_fromUtf8("textSADWindowSize"))
        self.textMinDisp = QtGui.QLineEdit(BlockTunerDlg)
        self.textMinDisp.setGeometry(QtCore.QRect(10, 520, 70, 30))
        self.textMinDisp.setObjectName(_fromUtf8("textMinDisp"))
        self.textUniqueRatio = QtGui.QLineEdit(BlockTunerDlg)
        self.textUniqueRatio.setGeometry(QtCore.QRect(10, 580, 70, 30))
        self.textUniqueRatio.setObjectName(_fromUtf8("textUniqueRatio"))
        self.sliderUniqueRatio = QtGui.QSlider(BlockTunerDlg)
        self.sliderUniqueRatio.setGeometry(QtCore.QRect(100, 580, 359, 29))
        self.sliderUniqueRatio.setMaximum(15)
        self.sliderUniqueRatio.setOrientation(QtCore.Qt.Horizontal)
        self.sliderUniqueRatio.setObjectName(_fromUtf8("sliderUniqueRatio"))
        self.labelUniqueRatio = QtGui.QLabel(BlockTunerDlg)
        self.labelUniqueRatio.setGeometry(QtCore.QRect(100, 560, 360, 20))
        self.labelUniqueRatio.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUniqueRatio.setObjectName(_fromUtf8("labelUniqueRatio"))

        self.retranslateUi(BlockTunerDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BlockTunerDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BlockTunerDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(BlockTunerDlg)

    def retranslateUi(self, BlockTunerDlg):
        BlockTunerDlg.setWindowTitle(_translate("BlockTunerDlg", "Block Tuner Dialog", None))
        self.labelP1.setText(_translate("BlockTunerDlg", "P1", None))
        self.sliderP1.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelP2.setText(_translate("BlockTunerDlg", "P2", None))
        self.sliderP2.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelNumDisp.setText(_translate("BlockTunerDlg", "num Disparities", None))
        self.sliderNumDisp.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelSpeckleRange.setText(_translate("BlockTunerDlg", "Speckle Range", None))
        self.sliderSpeckleRange.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelFullDP.setText(_translate("BlockTunerDlg", "Full DP", None))
        self.sliderFullDP.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelDisp12MaxDiff.setText(_translate("BlockTunerDlg", "Disp12 Max Diff", None))
        self.sliderDisp12MaxDiff.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelMinDisparity.setText(_translate("BlockTunerDlg", "Min Disparity", None))
        self.sliderMinDisparity.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelSADWindowSize.setText(_translate("BlockTunerDlg", "SAD Window Size", None))
        self.sliderSADWindowSize.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelSpeckleWindowSize.setText(_translate("BlockTunerDlg", "Speckle Window Size", None))
        self.sliderSpeckleWindowSize.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.sliderUniqueRatio.setToolTip(_translate("BlockTunerDlg", "P1", None))
        self.labelUniqueRatio.setText(_translate("BlockTunerDlg", "Uniqueness Ratio", None))

    def connectSlots(self):
      self.updateTextValues()

      self.sliderP1.sliderReleased.connect(self.sliderReleased)
      self.sliderP2.sliderReleased.connect(self.sliderReleased)
      self.sliderNumDisp.sliderReleased.connect(self.sliderReleased)
      self.sliderSpeckleRange.sliderReleased.connect(self.sliderReleased)
      self.sliderFullDP.sliderReleased.connect(self.sliderReleased)
      self.sliderDisp12MaxDiff.sliderReleased.connect(self.sliderReleased)
      self.sliderMinDisparity.sliderReleased.connect(self.sliderReleased)
      self.sliderSADWindowSize.sliderReleased.connect(self.sliderReleased)
      self.sliderSpeckleWindowSize.sliderReleased.connect(self.sliderReleased)
      self.sliderUniqueRatio.sliderReleased.connect(self.sliderReleased)

      self.sliderP1.valueChanged.connect(self.changedP1)
      self.sliderP2.valueChanged.connect(self.changedP2)
      self.sliderNumDisp.valueChanged.connect(self.changedNumDisp)
      self.sliderSpeckleRange.valueChanged.connect(self.changedSpeckleRange)
      self.sliderFullDP.valueChanged.connect(self.changedFullDP)
      self.sliderDisp12MaxDiff.valueChanged.connect(self.changedDisp12MaxDiff)
      self.sliderMinDisparity.valueChanged.connect(self.changedMinDisp)
      self.sliderSADWindowSize.valueChanged.connect(self.changedSADWindowSize)
      self.sliderSpeckleWindowSize.valueChanged.connect(self.changedSpeckleWindowSize)
      self.sliderUniqueRatio.valueChanged.connect(self.changedUniqueRatio)

      self.textP1.setValidator(QtGui.QIntValidator(0, 1536))
      self.textP2.setValidator(QtGui.QIntValidator(0, 1536))
      self.textNumDisp.setValidator(QtGui.QIntValidator(16, 1536))
      self.textSpeckleRange.setValidator(QtGui.QIntValidator(0, 2))
      self.textFullDP.setValidator(QtGui.QIntValidator(0, 1))
      self.textDisp12MaxDiff.setValidator(QtGui.QIntValidator(0, 1536))
      self.textMinDisp.setValidator(QtGui.QIntValidator(0, 1536))
      self.textSADWindowSize.setValidator(QtGui.QIntValidator(1, 11))
      self.textSpeckleWindowSize.setValidator(QtGui.QIntValidator(1, 200))
      self.textUniqueRatio.setValidator(QtGui.QIntValidator(0, 15))

      self.textP1.textChanged.connect(self.txtChangedP1)
      self.textP2.textChanged.connect(self.txtChangedP2)
      #self.textNumDisp.valueChanged.connect(self.changedNumDisp)
      #self.textSpeckleRange.valueChanged.connect(self.changedSpeckleRange)
      #self.textFullDP.valueChanged.connect(self.changedFullDP)
      #self.textDisp12MaxDiff.valueChanged.connect(self.changedDisp12MaxDiff)
      #self.textMinDisp.valueChanged.connect(self.changedMinDisp)
      #self.textSADWindowSize.valueChanged.connect(self.changedSADWindowSize)
      #self.textSpeckleWindowSize.valueChanged.connect(self.changedSpeckleWindowSize)

    def updateTextValues(self):
      self.textP1.setText(str(self.sliderP1.value()))
      self.textP2.setText(str(self.sliderP2.value()))
      self.textNumDisp.setText(str(self.sliderNumDisp.value()))
      self.textSpeckleRange.setText(str(self.sliderSpeckleRange.value()))
      self.textFullDP.setText(str(self.sliderFullDP.value()))
      self.textDisp12MaxDiff.setText(str(self.sliderDisp12MaxDiff.value()))
      self.textMinDisp.setText(str(self.sliderMinDisparity.value()))
      self.textSADWindowSize.setText(str(self.sliderSADWindowSize.value()))
      self.textSpeckleWindowSize.setText(str(self.sliderSpeckleWindowSize.value()))
      self.textUniqueRatio.setText(str(self.sliderUniqueRatio.value()))

    def changedP1(self):
      p1 = self.sliderP1.value()
      p2 = self.sliderP2.value()
      if p1 >= p2:
        self.showError("P1 cannot be greater than P2.")
        self.sliderP1.setValue(self.sliderP2.value() - 1)        

      self.textP1.setText(str(self.sliderP1.value()))

    def changedP2(self):
      p1 = self.sliderP1.value()
      p2 = self.sliderP2.value()
      if p1 >= p2:
        self.showError("P1 cannot be greater than P2.")
        self.sliderP2.setValue(self.sliderP1.value() + 1)        

      self.textP2.setText(str(self.sliderP2.value()))

    def changedNumDisp(self):
      self.textNumDisp.setText(str(self.sliderNumDisp.value()))

    def changedSpeckleRange(self):
      self.textSpeckleRange.setText(str(self.sliderSpeckleRange.value()))

    def changedFullDP(self):
      self.textFullDP.setText(str(self.sliderFullDP.value()))

    def changedDisp12MaxDiff(self):
      self.textDisp12MaxDiff.setText(str(self.sliderDisp12MaxDiff.value()))

    def changedMinDisp(self):
      self.textMinDisp.setText(str(self.sliderMinDisparity.value()))

    def changedSADWindowSize(self):
      self.textSADWindowSize.setText(str(self.sliderSADWindowSize.value()))

    def changedSpeckleWindowSize(self):
      self.textSpeckleWindowSize.setText(str(self.sliderSpeckleWindowSize.value()))

    def changedUniqueRatio(self):
      self.textUniqueRatio.setText(str(self.sliderUniqueRatio.value()))

    def sliderReleased(self):
      print "slider released"

    def txtChangedP1(self):
      new_p1 = int(self.textP1.text())
      p2 = int(self.textP2.text())
      if new_p1 >= p2:
        self.showError("P1 cannot be greater than or equal P2.")
        self.textP1.setText(str(self.sliderP1.value()))        
      else:
        self.sliderP1.setValue(new_p1)

    def txtChangedP2(self):
      p1 = int(self.textP1.text())
      new_p2 = int(self.textP2.text())
      if p1 >= new_p2:
        self.showError("P1 cannot be greater than or equal P2.")
        self.textP2.setText(str(self.sliderP2.value()))
      else:
        self.sliderP2.setValue(new_p2)

    def showError(self, txtError):
      QtGui.QMessageBox.about(self.textP1, "Error", txtError)

    def setDefaults(self):
      self.sliderP1.setValue(216)
      self.sliderP2.setValue(864)
      self.sliderNumDisp.setValue(96)
      self.sliderSpeckleRange.setValue(2)
      self.sliderFullDP.setValue(0)
      self.sliderUniqueRatio.setValue(10)
      self.sliderDisp12MaxDiff.setValue(1)
      self.sliderMinDisparity.setValue(16)
      self.sliderSADWindowSize.setValue(3)
      self.sliderSpeckleWindowSize.setValue(100)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BlockTunerDlg = QtGui.QDialog()
    ui = Ui_BlockTunerDlg()
    ui.setupUi(BlockTunerDlg)
    ui.setDefaults()
    ui.connectSlots();
    BlockTunerDlg.show()
    sys.exit(app.exec_())

