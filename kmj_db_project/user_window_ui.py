# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 643)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_sign_in_menu = QPushButton(self.centralwidget)
        self.pushButton_sign_in_menu.setObjectName(u"pushButton_sign_in_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_sign_in_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_sign_in_menu.setSizePolicy(sizePolicy2)
        self.pushButton_sign_in_menu.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u"icon/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_sign_in_menu.setIcon(icon)
        self.pushButton_sign_in_menu.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_sign_in_menu)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pushButton_movie_select_menu = QPushButton(self.centralwidget)
        self.pushButton_movie_select_menu.setObjectName(u"pushButton_movie_select_menu")
        sizePolicy2.setHeightForWidth(self.pushButton_movie_select_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_movie_select_menu.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u"icon/movie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_movie_select_menu.setIcon(icon1)
        self.pushButton_movie_select_menu.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_movie_select_menu)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.pushButton_user_info_menu = QPushButton(self.centralwidget)
        self.pushButton_user_info_menu.setObjectName(u"pushButton_user_info_menu")
        sizePolicy2.setHeightForWidth(self.pushButton_user_info_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_user_info_menu.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u"icon/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_user_info_menu.setIcon(icon2)
        self.pushButton_user_info_menu.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_user_info_menu)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_user_id_info = QLabel(self.centralwidget)
        self.label_user_id_info.setObjectName(u"label_user_id_info")
        sizePolicy1.setHeightForWidth(self.label_user_id_info.sizePolicy().hasHeightForWidth())
        self.label_user_id_info.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_user_id_info)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_6)

        self.tableWidget_user_book = QTableWidget(self.centralwidget)
        self.tableWidget_user_book.setObjectName(u"tableWidget_user_book")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget_user_book.sizePolicy().hasHeightForWidth())
        self.tableWidget_user_book.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.tableWidget_user_book)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_cancel_book = QPushButton(self.centralwidget)
        self.pushButton_cancel_book.setObjectName(u"pushButton_cancel_book")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel_book)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc601\ud654 \uc608\ub9e4 \ud504\ub85c\uadf8\ub7a8 made by \uae40\ubbfc\uc7ac", None))
        self.pushButton_sign_in_menu.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign in / Sign up", None))
        self.pushButton_movie_select_menu.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Movie", None))
        self.pushButton_user_info_menu.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User Information", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User ID", None))
        self.label_user_id_info.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc608\ub9e4 \ud604\ud669", None))
        self.pushButton_cancel_book.setText(QCoreApplication.translate("MainWindow", u"\ucde8\uc18c", None))
    # retranslateUi

