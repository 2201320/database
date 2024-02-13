# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movie_window.ui'
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
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
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
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_5)

        self.tableWidget_cinema = QTableWidget(self.centralwidget)
        self.tableWidget_cinema.setObjectName(u"tableWidget_cinema")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget_cinema.sizePolicy().hasHeightForWidth())
        self.tableWidget_cinema.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.tableWidget_cinema)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_cinema_name = QLabel(self.centralwidget)
        self.label_cinema_name.setObjectName(u"label_cinema_name")
        sizePolicy1.setHeightForWidth(self.label_cinema_name.sizePolicy().hasHeightForWidth())
        self.label_cinema_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_cinema_name)

        self.pushButton_select_cinema = QPushButton(self.centralwidget)
        self.pushButton_select_cinema.setObjectName(u"pushButton_select_cinema")
        sizePolicy4.setHeightForWidth(self.pushButton_select_cinema.sizePolicy().hasHeightForWidth())
        self.pushButton_select_cinema.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.pushButton_select_cinema)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy5)

        self.verticalLayout_3.addWidget(self.label_7)

        self.tableWidget_movie = QTableWidget(self.centralwidget)
        self.tableWidget_movie.setObjectName(u"tableWidget_movie")
        sizePolicy3.setHeightForWidth(self.tableWidget_movie.sizePolicy().hasHeightForWidth())
        self.tableWidget_movie.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.tableWidget_movie)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.label_movie_name = QLabel(self.centralwidget)
        self.label_movie_name.setObjectName(u"label_movie_name")

        self.horizontalLayout_3.addWidget(self.label_movie_name)

        self.pushButton_select_movie = QPushButton(self.centralwidget)
        self.pushButton_select_movie.setObjectName(u"pushButton_select_movie")
        sizePolicy4.setHeightForWidth(self.pushButton_select_movie.sizePolicy().hasHeightForWidth())
        self.pushButton_select_movie.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.pushButton_select_movie)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_seat = QLineEdit(self.centralwidget)
        self.lineEdit_seat.setObjectName(u"lineEdit_seat")

        self.horizontalLayout_4.addWidget(self.lineEdit_seat)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton_book = QPushButton(self.centralwidget)
        self.pushButton_book.setObjectName(u"pushButton_book")
        sizePolicy4.setHeightForWidth(self.pushButton_book.sizePolicy().hasHeightForWidth())
        self.pushButton_book.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.pushButton_book)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_ticket_price = QLabel(self.centralwidget)
        self.label_ticket_price.setObjectName(u"label_ticket_price")
        sizePolicy4.setHeightForWidth(self.label_ticket_price.sizePolicy().hasHeightForWidth())
        self.label_ticket_price.setSizePolicy(sizePolicy4)

        self.horizontalLayout_6.addWidget(self.label_ticket_price)

        self.label_ticket_price_2 = QLabel(self.centralwidget)
        self.label_ticket_price_2.setObjectName(u"label_ticket_price_2")
        sizePolicy1.setHeightForWidth(self.label_ticket_price_2.sizePolicy().hasHeightForWidth())
        self.label_ticket_price_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_ticket_price_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.pushButton_purchase = QPushButton(self.centralwidget)
        self.pushButton_purchase.setObjectName(u"pushButton_purchase")
        sizePolicy4.setHeightForWidth(self.pushButton_purchase.sizePolicy().hasHeightForWidth())
        self.pushButton_purchase.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.pushButton_purchase)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.label_purchase_result = QLabel(self.centralwidget)
        self.label_purchase_result.setObjectName(u"label_purchase_result")
        sizePolicy1.setHeightForWidth(self.label_purchase_result.sizePolicy().hasHeightForWidth())
        self.label_purchase_result.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_purchase_result)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 22))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"1. \uc601\ud654\uad00 \uc120\ud0dd", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ub41c \uc601\ud654\uad00:  ", None))
        self.label_cinema_name.setText("")
        self.pushButton_select_cinema.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2. \uc601\ud654 \uc120\ud0dd", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ub41c \uc601\ud654:  ", None))
        self.label_movie_name.setText("")
        self.pushButton_select_movie.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"3. \uc88c\uc11d \uc120\ud0dd", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc88c\uc11d \uc785\ub825 (\uc601\uc5b4 + \uc22b\uc790, ex) F10):  ", None))
        self.pushButton_book.setText(QCoreApplication.translate("MainWindow", u"\uc608\ub9e4", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"4. \uacb0\uc81c", None))
        self.label_ticket_price.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uc81c \uae08\uc561:  ", None))
        self.label_ticket_price_2.setText("")
        self.pushButton_purchase.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uc81c", None))
        self.label_purchase_result.setText("")
    # retranslateUi

