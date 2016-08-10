# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\StereoVision\block_tuner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from argparse import ArgumentParser

import cv2
import numpy as np

from stereovision.blockmatchers import StereoBM, StereoSGBM
from stereovision.calibration import StereoCalibration
from stereovision.ui_utils import find_files, BMTuner, STEREO_BM_FLAG

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_BlockTunerDlg(object):
    def setupUi(self, BlockTunerDlg):
        BlockTunerDlg.setObjectName(_fromUtf8("BlockTunerDlg"))
        BlockTunerDlg.resize(469, 671)
        self.buttonBox = QDialogButtonBox(BlockTunerDlg)
        self.buttonBox.setGeometry(QRect(360, 630, 91, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.textP1 = QLineEdit(BlockTunerDlg)
        self.textP1.setGeometry(QRect(10, 40, 70, 30))
        self.textP1.setObjectName(_fromUtf8("textP1"))
        self.labelP1 = QLabel(BlockTunerDlg)
        self.labelP1.setGeometry(QRect(100, 20, 360, 20))
        self.labelP1.setAlignment(Qt.AlignCenter)
        self.labelP1.setObjectName(_fromUtf8("labelP1"))
        self.sliderP1 = QSlider(BlockTunerDlg)
        self.sliderP1.setGeometry(QRect(100, 40, 359, 29))
        self.sliderP1.setMaximum(1536)
        self.sliderP1.setOrientation(Qt.Horizontal)
        self.sliderP1.setObjectName(_fromUtf8("sliderP1"))
        self.labelP2 = QLabel(BlockTunerDlg)
        self.labelP2.setGeometry(QRect(100, 80, 360, 20))
        self.labelP2.setAlignment(Qt.AlignCenter)
        self.labelP2.setObjectName(_fromUtf8("labelP2"))
        self.sliderP2 = QSlider(BlockTunerDlg)
        self.sliderP2.setGeometry(QRect(100, 100, 359, 29))
        self.sliderP2.setMaximum(1536)
        self.sliderP2.setOrientation(Qt.Horizontal)
        self.sliderP2.setObjectName(_fromUtf8("sliderP2"))
        self.labelNumDisp = QLabel(BlockTunerDlg)
        self.labelNumDisp.setGeometry(QRect(100, 140, 360, 20))
        self.labelNumDisp.setAlignment(Qt.AlignCenter)
        self.labelNumDisp.setObjectName(_fromUtf8("labelNumDisp"))
        self.sliderNumDisp = QSlider(BlockTunerDlg)
        self.sliderNumDisp.setGeometry(QRect(100, 160, 359, 29))
        self.sliderNumDisp.setMaximum(1536)
        self.sliderNumDisp.setSingleStep(16)
        self.sliderNumDisp.setPageStep(16)
        self.sliderNumDisp.setOrientation(Qt.Horizontal)
        self.sliderNumDisp.setObjectName(_fromUtf8("sliderNumDisp"))
        self.labelSpeckleRange = QLabel(BlockTunerDlg)
        self.labelSpeckleRange.setGeometry(QRect(100, 200, 360, 20))
        self.labelSpeckleRange.setAlignment(Qt.AlignCenter)
        self.labelSpeckleRange.setObjectName(_fromUtf8("labelSpeckleRange"))
        self.sliderSpeckleRange = QSlider(BlockTunerDlg)
        self.sliderSpeckleRange.setGeometry(QRect(100, 220, 359, 29))
        self.sliderSpeckleRange.setMaximum(2)
        self.sliderSpeckleRange.setSingleStep(1)
        self.sliderSpeckleRange.setOrientation(Qt.Horizontal)
        self.sliderSpeckleRange.setObjectName(_fromUtf8("sliderSpeckleRange"))
        self.labelFullDP = QLabel(BlockTunerDlg)
        self.labelFullDP.setGeometry(QRect(100, 320, 360, 20))
        self.labelFullDP.setAlignment(Qt.AlignCenter)
        self.labelFullDP.setObjectName(_fromUtf8("labelFullDP"))
        self.sliderFullDP = QSlider(BlockTunerDlg)
        self.sliderFullDP.setGeometry(QRect(100, 340, 359, 29))
        self.sliderFullDP.setMaximum(1)
        self.sliderFullDP.setOrientation(Qt.Horizontal)
        self.sliderFullDP.setObjectName(_fromUtf8("sliderFullDP"))
        self.labelDisp12MaxDiff = QLabel(BlockTunerDlg)
        self.labelDisp12MaxDiff.setGeometry(QRect(100, 380, 360, 20))
        self.labelDisp12MaxDiff.setAlignment(Qt.AlignCenter)
        self.labelDisp12MaxDiff.setObjectName(_fromUtf8("labelDisp12MaxDiff"))
        self.sliderDisp12MaxDiff = QSlider(BlockTunerDlg)
        self.sliderDisp12MaxDiff.setGeometry(QRect(100, 400, 359, 29))
        self.sliderDisp12MaxDiff.setMaximum(1536)
        self.sliderDisp12MaxDiff.setOrientation(Qt.Horizontal)
        self.sliderDisp12MaxDiff.setObjectName(_fromUtf8("sliderDisp12MaxDiff"))
        self.labelMinDisparity = QLabel(BlockTunerDlg)
        self.labelMinDisparity.setGeometry(QRect(100, 500, 360, 20))
        self.labelMinDisparity.setAlignment(Qt.AlignCenter)
        self.labelMinDisparity.setObjectName(_fromUtf8("labelMinDisparity"))
        self.sliderMinDisparity = QSlider(BlockTunerDlg)
        self.sliderMinDisparity.setGeometry(QRect(100, 520, 359, 29))
        self.sliderMinDisparity.setMaximum(1536)
        self.sliderMinDisparity.setOrientation(Qt.Horizontal)
        self.sliderMinDisparity.setObjectName(_fromUtf8("sliderMinDisparity"))
        self.labelSADWindowSize = QLabel(BlockTunerDlg)
        self.labelSADWindowSize.setGeometry(QRect(100, 440, 360, 20))
        self.labelSADWindowSize.setAlignment(Qt.AlignCenter)
        self.labelSADWindowSize.setObjectName(_fromUtf8("labelSADWindowSize"))
        self.sliderSADWindowSize = QSlider(BlockTunerDlg)
        self.sliderSADWindowSize.setGeometry(QRect(100, 460, 359, 29))
        self.sliderSADWindowSize.setMaximum(11)
        self.sliderSADWindowSize.setOrientation(Qt.Horizontal)
        self.sliderSADWindowSize.setObjectName(_fromUtf8("sliderSADWindowSize"))
        self.labelSpeckleWindowSize = QLabel(BlockTunerDlg)
        self.labelSpeckleWindowSize.setGeometry(QRect(100, 260, 360, 20))
        self.labelSpeckleWindowSize.setAlignment(Qt.AlignCenter)
        self.labelSpeckleWindowSize.setObjectName(_fromUtf8("labelSpeckleWindowSize"))
        self.sliderSpeckleWindowSize = QSlider(BlockTunerDlg)
        self.sliderSpeckleWindowSize.setGeometry(QRect(100, 280, 359, 29))
        self.sliderSpeckleWindowSize.setMaximum(200)
        self.sliderSpeckleWindowSize.setOrientation(Qt.Horizontal)
        self.sliderSpeckleWindowSize.setObjectName(_fromUtf8("sliderSpeckleWindowSize"))
        self.textP2 = QLineEdit(BlockTunerDlg)
        self.textP2.setGeometry(QRect(10, 100, 70, 30))
        self.textP2.setObjectName(_fromUtf8("textP2"))
        self.textNumDisp = QLineEdit(BlockTunerDlg)
        self.textNumDisp.setGeometry(QRect(10, 160, 70, 30))
        self.textNumDisp.setObjectName(_fromUtf8("textNumDisp"))
        self.textSpeckleRange = QLineEdit(BlockTunerDlg)
        self.textSpeckleRange.setGeometry(QRect(10, 220, 70, 30))
        self.textSpeckleRange.setObjectName(_fromUtf8("textSpeckleRange"))
        self.textSpeckleWindowSize = QLineEdit(BlockTunerDlg)
        self.textSpeckleWindowSize.setGeometry(QRect(10, 280, 70, 30))
        self.textSpeckleWindowSize.setObjectName(_fromUtf8("textSpeckleWindowSize"))
        self.textFullDP = QLineEdit(BlockTunerDlg)
        self.textFullDP.setGeometry(QRect(10, 340, 70, 30))
        self.textFullDP.setObjectName(_fromUtf8("textFullDP"))
        self.textDisp12MaxDiff = QLineEdit(BlockTunerDlg)
        self.textDisp12MaxDiff.setGeometry(QRect(10, 400, 70, 30))
        self.textDisp12MaxDiff.setObjectName(_fromUtf8("textDisp12MaxDiff"))
        self.textSADWindowSize = QLineEdit(BlockTunerDlg)
        self.textSADWindowSize.setGeometry(QRect(10, 460, 70, 30))
        self.textSADWindowSize.setObjectName(_fromUtf8("textSADWindowSize"))
        self.textMinDisp = QLineEdit(BlockTunerDlg)
        self.textMinDisp.setGeometry(QRect(10, 520, 70, 30))
        self.textMinDisp.setObjectName(_fromUtf8("textMinDisp"))
        self.textUniqueRatio = QLineEdit(BlockTunerDlg)
        self.textUniqueRatio.setGeometry(QRect(10, 580, 70, 30))
        self.textUniqueRatio.setObjectName(_fromUtf8("textUniqueRatio"))
        self.sliderUniqueRatio = QSlider(BlockTunerDlg)
        self.sliderUniqueRatio.setGeometry(QRect(100, 580, 359, 29))
        self.sliderUniqueRatio.setMaximum(15)
        self.sliderUniqueRatio.setOrientation(Qt.Horizontal)
        self.sliderUniqueRatio.setObjectName(_fromUtf8("sliderUniqueRatio"))
        self.labelUniqueRatio = QLabel(BlockTunerDlg)
        self.labelUniqueRatio.setGeometry(QRect(100, 560, 360, 20))
        self.labelUniqueRatio.setAlignment(Qt.AlignCenter)
        self.labelUniqueRatio.setObjectName(_fromUtf8("labelUniqueRatio"))
        self.pushNextImage = QPushButton(BlockTunerDlg)
        self.pushNextImage.setGeometry(QRect(10, 640, 75, 23))
        self.pushNextImage.setObjectName(_fromUtf8("pushNextImage"))
        self.labelFileInfo = QLabel(BlockTunerDlg)
        self.labelFileInfo.setGeometry(QRect(120, 640, 201, 21))
        self.labelFileInfo.setText(_fromUtf8(""))
        self.labelFileInfo.setObjectName(_fromUtf8("labelFileInfo"))

        self.retranslateUi(BlockTunerDlg)
        QObject.connect(self.buttonBox, SIGNAL(_fromUtf8("accepted()")), BlockTunerDlg.accept)
        QObject.connect(self.buttonBox, SIGNAL(_fromUtf8("rejected()")), BlockTunerDlg.reject)
        QMetaObject.connectSlotsByName(BlockTunerDlg)

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
        self.pushNextImage.setText(_translate("BlockTunerDlg", "Next", None))

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

      self.textP1.setValidator(QIntValidator(0, 1536))
      self.textP2.setValidator(QIntValidator(0, 1536))
      self.textNumDisp.setValidator(QIntValidator(16, 1536))
      self.textSpeckleRange.setValidator(QIntValidator(0, 2))
      self.textFullDP.setValidator(QIntValidator(0, 1))
      self.textDisp12MaxDiff.setValidator(QIntValidator(0, 1536))
      self.textMinDisp.setValidator(QIntValidator(0, 1536))
      self.textSADWindowSize.setValidator(QIntValidator(1, 11))
      self.textSpeckleWindowSize.setValidator(QIntValidator(1, 200))
      self.textUniqueRatio.setValidator(QIntValidator(0, 15))

      self.textP1.textChanged.connect(self.txtChangedP1)
      self.textP2.textChanged.connect(self.txtChangedP2)
      self.textNumDisp.textChanged.connect(self.txtChangedNumDisp)
      self.textSpeckleRange.textChanged.connect(self.txtChangedSpeckleRange)
      self.textFullDP.textChanged.connect(self.txtChangedFullDP)
      self.textDisp12MaxDiff.textChanged.connect(self.txtChangedDisp12MaxDiff)
      self.textMinDisp.textChanged.connect(self.txtChangedMinDisp)
      self.textSADWindowSize.textChanged.connect(self.txtChangedSADWindowSize)
      self.textSpeckleWindowSize.textChanged.connect(self.txtChangedSpeckleWindowSize)
      self.textUniqueRatio.textChanged.connect(self.txtChangedUniqueRatio)

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

    def updateTuner(self):
      p1 = self.sliderP1.value()
      p2 = self.sliderP2.value()
      num_disp = self.sliderNumDisp.value()
      speckle_range = self.sliderSpeckleRange.value()
      full_dp = self.sliderFullDP.value()
      disp12 = self.sliderDisp12MaxDiff.value()
      min_disp = self.sliderMinDisparity.value()
      sad = self.sliderSADWindowSize.value()
      speckle_win = self.sliderSpeckleWindowSize.value()
      unique = self.sliderUniqueRatio.value()
      
      self.tuner.setTunerValue('P1', p1)
      self.tuner.setTunerValue('P2', p2)
      self.tuner.setTunerValue('numDisparities', num_disp)
      self.tuner.setTunerValue('speckleRange', speckle_range)
      self.tuner.setTunerValue('fullDP', full_dp)
      self.tuner.setTunerValue('disp12MaxDiff', disp12)
      self.tuner.setTunerValue('minDisparity', min_disp)
      self.tuner.setTunerValue('SADWindowSize', sad)
      self.tuner.setTunerValue('speckleWindowSize', speckle_win)
      self.tuner.setTunerValue('uniquenessRatio', unique)

      self.tuner.update_disparity_map()
      
    def sliderReleased(self):
      self.updateTuner()
    
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

    def txtChangedNumDisp(self):
      new = int(self.textNumDisp.text())
      
      # the new value must be divisible by 16
      div_val = int(new / 16)
      new_val = 16 * div_val
      
      self.sliderNumDisp.setValue(new_val)
      self.textNumDisp.setText(str(new_val))

    def txtChangedSpeckleRange(self):
      new = int(self.textSpeckleRange.text())
      self.sliderSpeckleRange.setValue(new)

    def txtChangedFullDP(self):
      new = int(self.textFullDP.text())
      self.sliderFullDP.setValue(new)

    def txtChangedDisp12MaxDiff(self):
      new = int(self.textDisp12MaxDiff.text())
      self.sliderDisp12MaxDiff.setValue(new)

    def txtChangedMinDisp(self):
      new = int(self.textMinDisp.text())
      self.sliderMinDisparity.setValue(new)

    def txtChangedSADWindowSize(self):
      new = int(self.textSADWindowSize.text())
      self.sliderSADWindowSize.setValue(new)

    def txtChangedSpeckleWindowSize(self):
      new = int(self.textSpeckleWindowSize.text())
      self.sliderSpeckleWindowSize.setValue(new)

    def txtChangedUniqueRatio(self):
      new = int(self.textUniqueRatio.text())
      self.sliderUniqueRatio.setValue(new)

    def showError(self, txtError):
      QMessageBox.about(self.textP1, "Error", txtError)

    def setDefaults(self):
      self.sliderP1.setValue(279)
      self.sliderP2.setValue(1536)
      self.sliderNumDisp.setValue(48)
      self.sliderSpeckleRange.setValue(1)
      self.sliderFullDP.setValue(0)
      self.sliderUniqueRatio.setValue(9)
      self.sliderDisp12MaxDiff.setValue(1)
      self.sliderMinDisparity.setValue(12)
      self.sliderSADWindowSize.setValue(3)
      self.sliderSpeckleWindowSize.setValue(100)

    def incrementImage(self):
      if input_files:
        image_pair = [cv2.imread(image) for image in input_files[:2]]
        rectified_pair = calibration.rectify(image_pair)
        tuner.tune_pair(rectified_pair)
        input_files = input_files[2:]
      
      
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    BlockTunerDlg = QDialog()
    ui = Ui_BlockTunerDlg()
    ui.setupUi(BlockTunerDlg)
    ui.setDefaults()
    ui.connectSlots();

    parser = ArgumentParser(description="Read images taken from a calibrated "
                           "stereo pair, compute disparity maps from them and "
                           "show them interactively to the user, allowing the "
                           "user to tune the stereo block matcher settings in "
                           "the GUI.", parents=[STEREO_BM_FLAG])
    parser.add_argument("calibration_folder",
                        help="Directory where calibration files for the stereo "
                        "pair are stored.")
    parser.add_argument("image_folder",
                        help="Directory where input images are stored.")
    parser.add_argument("--bm_settings",
                        help="File to save last block matcher settings to.",
                        default="")
    args = parser.parse_args()

    ui.calibration = StereoCalibration(input_folder=args.calibration_folder)
    ui.input_files = find_files(args.image_folder)
    if args.use_stereobm:
        ui.block_matcher = StereoBM()
    else:
        ui.block_matcher = StereoSGBM()
    ui.image_pair = [cv2.imread(image) for image in ui.input_files[:2]]
    ui.input_files = ui.input_files[2:]
    ui.rectified_pair = ui.calibration.rectify(ui.image_pair)
    ui.tuner = BMTuner(ui.block_matcher, ui.calibration, ui.rectified_pair)

    BlockTunerDlg.show()
    
#    for param in block_matcher.parameter_maxima:
#        print("{}\n".format(ui.tuner.report_settings(param)))
#
#    if args.bm_settings:
#        ui.block_matcher.save_settings(args.bm_settings)

    sys.exit(app.exec_())

