# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sound.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(674, 589)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(570, 550, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBoxAgain = QtWidgets.QCheckBox(Dialog)
        self.checkBoxAgain.setGeometry(QtCore.QRect(30, 40, 71, 21))
        self.checkBoxAgain.setObjectName("checkBoxAgain")
        self.checkBoxHard = QtWidgets.QCheckBox(Dialog)
        self.checkBoxHard.setGeometry(QtCore.QRect(180, 40, 71, 21))
        self.checkBoxHard.setObjectName("checkBoxHard")
        self.checkBoxGood = QtWidgets.QCheckBox(Dialog)
        self.checkBoxGood.setGeometry(QtCore.QRect(350, 41, 61, 20))
        self.checkBoxGood.setObjectName("checkBoxGood")
        self.checkBoxEasy = QtWidgets.QCheckBox(Dialog)
        self.checkBoxEasy.setGeometry(QtCore.QRect(510, 40, 61, 21))
        self.checkBoxEasy.setObjectName("checkBoxEasy")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 651, 111))
        self.groupBox.setObjectName("groupBox")
        self.checkBoxFinish = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxFinish.setGeometry(QtCore.QRect(460, 70, 111, 21))
        self.checkBoxFinish.setObjectName("checkBoxFinish")
        self.spinGradWaitEasy = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spinGradWaitEasy.setGeometry(QtCore.QRect(170, 70, 51, 22))
        self.spinGradWaitEasy.setDecimals(1)
        self.spinGradWaitEasy.setMaximum(10.0)
        self.spinGradWaitEasy.setSingleStep(0.1)
        self.spinGradWaitEasy.setProperty("value", 0.3)
        self.spinGradWaitEasy.setObjectName("spinGradWaitEasy")
        self.checkBoxGrad = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxGrad.setGeometry(QtCore.QRect(20, 70, 141, 20))
        self.checkBoxGrad.setObjectName("checkBoxGrad")
        self.spinBoxVolFinish = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxVolFinish.setGeometry(QtCore.QRect(571, 70, 61, 22))
        self.spinBoxVolFinish.setMaximum(100)
        self.spinBoxVolFinish.setSingleStep(5)
        self.spinBoxVolFinish.setProperty("value", 100)
        self.spinBoxVolFinish.setObjectName("spinBoxVolFinish")
        self.spinBoxVolGraduate = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxVolGraduate.setGeometry(QtCore.QRect(240, 70, 61, 22))
        self.spinBoxVolGraduate.setMaximum(100)
        self.spinBoxVolGraduate.setSingleStep(5)
        self.spinBoxVolGraduate.setProperty("value", 100)
        self.spinBoxVolGraduate.setObjectName("spinBoxVolGraduate")
        self.spinBoxVolEasy = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxVolEasy.setGeometry(QtCore.QRect(571, 30, 61, 22))
        self.spinBoxVolEasy.setMaximum(100)
        self.spinBoxVolEasy.setSingleStep(5)
        self.spinBoxVolEasy.setProperty("value", 100)
        self.spinBoxVolEasy.setObjectName("spinBoxVolEasy")
        self.spinBoxVolGood = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxVolGood.setGeometry(QtCore.QRect(410, 30, 61, 22))
        self.spinBoxVolGood.setMaximum(100)
        self.spinBoxVolGood.setSingleStep(5)
        self.spinBoxVolGood.setProperty("value", 100)
        self.spinBoxVolGood.setObjectName("spinBoxVolGood")
        self.spinBoxVolHard = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxVolHard.setGeometry(QtCore.QRect(240, 30, 61, 22))
        self.spinBoxVolHard.setMaximum(100)
        self.spinBoxVolHard.setSingleStep(5)
        self.spinBoxVolHard.setProperty("value", 100)
        self.spinBoxVolHard.setObjectName("spinBoxVolHard")
        self.spinBoxVolAgain = QtWidgets.QSpinBox(self.groupBox)
        self.spinBoxVolAgain.setGeometry(QtCore.QRect(90, 30, 61, 22))
        self.spinBoxVolAgain.setMaximum(100)
        self.spinBoxVolAgain.setSingleStep(5)
        self.spinBoxVolAgain.setProperty("value", 100)
        self.spinBoxVolAgain.setObjectName("spinBoxVolAgain")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 651, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBoxCorrect = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxCorrect.setGeometry(QtCore.QRect(20, 31, 91, 20))
        self.checkBoxCorrect.setObjectName("checkBoxCorrect")
        self.checkBoxError = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxError.setGeometry(QtCore.QRect(210, 30, 71, 21))
        self.checkBoxError.setObjectName("checkBoxError")
        self.spinBoxVolCorret = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxVolCorret.setGeometry(QtCore.QRect(120, 30, 61, 22))
        self.spinBoxVolCorret.setMaximum(100)
        self.spinBoxVolCorret.setSingleStep(5)
        self.spinBoxVolCorret.setProperty("value", 100)
        self.spinBoxVolCorret.setObjectName("spinBoxVolCorret")
        self.spinBoxVolError = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxVolError.setGeometry(QtCore.QRect(290, 30, 61, 22))
        self.spinBoxVolError.setMaximum(100)
        self.spinBoxVolError.setSingleStep(5)
        self.spinBoxVolError.setProperty("value", 100)
        self.spinBoxVolError.setObjectName("spinBoxVolError")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 210, 651, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBoxSuspended = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxSuspended.setGeometry(QtCore.QRect(20, 30, 101, 21))
        self.checkBoxSuspended.setObjectName("checkBoxSuspended")
        self.checkBoxBuriedUsr = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxBuriedUsr.setGeometry(QtCore.QRect(230, 30, 111, 21))
        self.checkBoxBuriedUsr.setObjectName("checkBoxBuriedUsr")
        self.checkBoxBuriedSch = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxBuriedSch.setGeometry(QtCore.QRect(460, 30, 111, 21))
        self.checkBoxBuriedSch.setObjectName("checkBoxBuriedSch")
        self.spinBoxVolBuriedSch = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBoxVolBuriedSch.setGeometry(QtCore.QRect(571, 30, 61, 22))
        self.spinBoxVolBuriedSch.setMaximum(100)
        self.spinBoxVolBuriedSch.setSingleStep(5)
        self.spinBoxVolBuriedSch.setProperty("value", 100)
        self.spinBoxVolBuriedSch.setObjectName("spinBoxVolBuriedSch")
        self.spinBoxVolBuriedUsr = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBoxVolBuriedUsr.setGeometry(QtCore.QRect(350, 30, 61, 22))
        self.spinBoxVolBuriedUsr.setMaximum(100)
        self.spinBoxVolBuriedUsr.setSingleStep(5)
        self.spinBoxVolBuriedUsr.setProperty("value", 100)
        self.spinBoxVolBuriedUsr.setObjectName("spinBoxVolBuriedUsr")
        self.spinBoxVolSuspended = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBoxVolSuspended.setGeometry(QtCore.QRect(120, 30, 61, 22))
        self.spinBoxVolSuspended.setMaximum(100)
        self.spinBoxVolSuspended.setSingleStep(5)
        self.spinBoxVolSuspended.setProperty("value", 100)
        self.spinBoxVolSuspended.setObjectName("spinBoxVolSuspended")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 290, 651, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBoxDelayQ = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBoxDelayQ.setGeometry(QtCore.QRect(20, 32, 81, 20))
        self.checkBoxDelayQ.setObjectName("checkBoxDelayQ")
        self.checkBoxDelayA = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBoxDelayA.setGeometry(QtCore.QRect(340, 32, 71, 21))
        self.checkBoxDelayA.setObjectName("checkBoxDelayA")
        self.spinDelayQ = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.spinDelayQ.setGeometry(QtCore.QRect(120, 30, 51, 22))
        self.spinDelayQ.setDecimals(1)
        self.spinDelayQ.setMaximum(10.0)
        self.spinDelayQ.setSingleStep(0.1)
        self.spinDelayQ.setProperty("value", 0.3)
        self.spinDelayQ.setObjectName("spinDelayQ")
        self.spinDelayA = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.spinDelayA.setGeometry(QtCore.QRect(420, 30, 51, 22))
        self.spinDelayA.setDecimals(1)
        self.spinDelayA.setMaximum(10.0)
        self.spinDelayA.setSingleStep(0.1)
        self.spinDelayA.setProperty("value", 0.3)
        self.spinDelayA.setObjectName("spinDelayA")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 370, 651, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.checkBoxFadeInQ = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBoxFadeInQ.setGeometry(QtCore.QRect(20, 32, 81, 20))
        self.checkBoxFadeInQ.setObjectName("checkBoxFadeInQ")
        self.checkBoxFadeInA = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBoxFadeInA.setGeometry(QtCore.QRect(340, 32, 61, 20))
        self.checkBoxFadeInA.setObjectName("checkBoxFadeInA")
        self.spinFadeInQ = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinFadeInQ.setGeometry(QtCore.QRect(120, 30, 51, 22))
        self.spinFadeInQ.setMinimum(1)
        self.spinFadeInQ.setMaximum(10)
        self.spinFadeInQ.setObjectName("spinFadeInQ")
        self.spinFadeInA = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinFadeInA.setGeometry(QtCore.QRect(420, 30, 51, 22))
        self.spinFadeInA.setPrefix("")
        self.spinFadeInA.setMinimum(1)
        self.spinFadeInA.setMaximum(10)
        self.spinFadeInA.setProperty("value", 1)
        self.spinFadeInA.setObjectName("spinFadeInA")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 450, 651, 91))
        self.groupBox_6.setObjectName("groupBox_6")
        self.checkBoxAmbientM = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBoxAmbientM.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.checkBoxAmbientM.setObjectName("checkBoxAmbientM")
        self.checkBoxAmbientR = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBoxAmbientR.setGeometry(QtCore.QRect(340, 30, 71, 21))
        self.checkBoxAmbientR.setObjectName("checkBoxAmbientR")
        self.sliderAmbientRVol = QtWidgets.QSlider(self.groupBox_6)
        self.sliderAmbientRVol.setGeometry(QtCore.QRect(340, 60, 211, 22))
        self.sliderAmbientRVol.setMaximum(100)
        self.sliderAmbientRVol.setPageStep(1)
        self.sliderAmbientRVol.setProperty("value", 60)
        self.sliderAmbientRVol.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAmbientRVol.setObjectName("sliderAmbientRVol")
        self.sliderAmbientMVol = QtWidgets.QSlider(self.groupBox_6)
        self.sliderAmbientMVol.setGeometry(QtCore.QRect(20, 60, 211, 22))
        self.sliderAmbientMVol.setMaximum(100)
        self.sliderAmbientMVol.setPageStep(1)
        self.sliderAmbientMVol.setProperty("value", 60)
        self.sliderAmbientMVol.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAmbientMVol.setObjectName("sliderAmbientMVol")
        self.comboBoxAmbientMMode = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBoxAmbientMMode.setGeometry(QtCore.QRect(88, 30, 101, 21))
        self.comboBoxAmbientMMode.setObjectName("comboBoxAmbientMMode")
        self.comboBoxAmbientRMode = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBoxAmbientRMode.setGeometry(QtCore.QRect(410, 30, 101, 21))
        self.comboBoxAmbientRMode.setObjectName("comboBoxAmbientRMode")
        self.labelAmbientMVol = QtWidgets.QLabel(self.groupBox_6)
        self.labelAmbientMVol.setGeometry(QtCore.QRect(240, 59, 31, 21))
        self.labelAmbientMVol.setObjectName("labelAmbientMVol")
        self.labelAmbientRVol = QtWidgets.QLabel(self.groupBox_6)
        self.labelAmbientRVol.setGeometry(QtCore.QRect(560, 60, 31, 20))
        self.labelAmbientRVol.setObjectName("labelAmbientRVol")
        self.checkBoxAmbientRContinue = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBoxAmbientRContinue.setGeometry(QtCore.QRect(560, 30, 81, 21))
        self.checkBoxAmbientRContinue.setObjectName("checkBoxAmbientRContinue")
        self.pushButtonPathMenu = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonPathMenu.setGeometry(QtCore.QRect(200, 30, 31, 21))
        self.pushButtonPathMenu.setObjectName("pushButtonPathMenu")
        self.pushButtonPathReview = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonPathReview.setGeometry(QtCore.QRect(520, 30, 31, 21))
        self.pushButtonPathReview.setObjectName("pushButtonPathReview")
        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.checkBoxAgain.raise_()
        self.checkBoxHard.raise_()
        self.checkBoxGood.raise_()
        self.checkBoxEasy.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Advanced Answer Sounds Setting (Fixed by Shigeඞ)"))
        self.checkBoxAgain.setText(_translate("Dialog", "again"))
        self.checkBoxHard.setText(_translate("Dialog", "hard"))
        self.checkBoxGood.setText(_translate("Dialog", "good"))
        self.checkBoxEasy.setText(_translate("Dialog", "easy"))
        self.groupBox.setTitle(_translate("Dialog", "Answer Effect"))
        self.checkBoxFinish.setText(_translate("Dialog", "finish deck"))
        self.spinGradWaitEasy.setToolTip(_translate("Dialog", "wait easy time"))
        self.spinGradWaitEasy.setSuffix(_translate("Dialog", "s"))
        self.checkBoxGrad.setText(_translate("Dialog", "graduate(wait ease)"))
        self.groupBox_2.setTitle(_translate("Dialog", "Type Effect"))
        self.checkBoxCorrect.setText(_translate("Dialog", "correct"))
        self.checkBoxError.setText(_translate("Dialog", "error"))
        self.groupBox_3.setTitle(_translate("Dialog", "Note State"))
        self.checkBoxSuspended.setText(_translate("Dialog", "suspended"))
        self.checkBoxBuriedUsr.setText(_translate("Dialog", "user buried"))
        self.checkBoxBuriedSch.setText(_translate("Dialog", "sched buried"))
        self.groupBox_4.setTitle(_translate("Dialog", "Delay Play"))
        self.checkBoxDelayQ.setText(_translate("Dialog", "Question"))
        self.checkBoxDelayA.setText(_translate("Dialog", "Answer"))
        self.spinDelayQ.setToolTip(_translate("Dialog", "delay time"))
        self.spinDelayQ.setSuffix(_translate("Dialog", "s"))
        self.spinDelayA.setToolTip(_translate("Dialog", "delay time"))
        self.spinDelayA.setSuffix(_translate("Dialog", "s"))
        self.groupBox_5.setTitle(_translate("Dialog", "Fadein Show"))
        self.checkBoxFadeInQ.setText(_translate("Dialog", "Question"))
        self.checkBoxFadeInA.setText(_translate("Dialog", "Answer"))
        self.spinFadeInQ.setToolTip(_translate("Dialog", "fadein time"))
        self.spinFadeInQ.setSuffix(_translate("Dialog", "s"))
        self.spinFadeInA.setToolTip(_translate("Dialog", "fadein time"))
        self.spinFadeInA.setSuffix(_translate("Dialog", "s"))
        self.groupBox_6.setTitle(_translate("Dialog", "Ambient Music"))
        self.checkBoxAmbientM.setText(_translate("Dialog", "Menu"))
        self.checkBoxAmbientR.setText(_translate("Dialog", "Review"))
        self.sliderAmbientRVol.setToolTip(_translate("Dialog", " Volume"))
        self.sliderAmbientMVol.setToolTip(_translate("Dialog", "Volume"))
        self.comboBoxAmbientMMode.setToolTip(_translate("Dialog", "repeat mode"))
        self.comboBoxAmbientRMode.setToolTip(_translate("Dialog", "repeat mode"))
        self.labelAmbientMVol.setText(_translate("Dialog", "30%"))
        self.labelAmbientRVol.setText(_translate("Dialog", "30%"))
        self.checkBoxAmbientRContinue.setToolTip(_translate("Dialog", "Continued/Breaked with Cards"))
        self.checkBoxAmbientRContinue.setText(_translate("Dialog", "Continue"))
        self.pushButtonPathMenu.setText(_translate("Dialog", "..."))
        self.pushButtonPathReview.setText(_translate("Dialog", "..."))
