import os

import oracledb

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QTableWidgetItem
from PySide6.QtCore import QTimer, Slot, QMutex
import PySide6.QtCore as QtCore

import manage_db

import start_window_ui
import movie_window_ui
import user_window_ui

user_id = None

class StartWindow(QMainWindow):
    def __init__(self, window_manager, odb_con: oracledb.Connection):
        super(StartWindow, self).__init__()

        self.window_manager = window_manager
        self.odb_con = odb_con

        self.ui = start_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_movie_select_menu.clicked.connect(self.convert_to_movie)
        self.ui.pushButton_user_info_menu.clicked.connect(self.convert_to_user)
        self.ui.pushButton_sign_up.clicked.connect(self.sign_up)
        self.ui.pushButton_sign_in.clicked.connect(self.sign_in)
    
    def show_window(self, geometry):
        if geometry is not None:
            self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        self.show()
        return

    def get_window_geometry(self):
        return [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
    
    def convert_to_movie(self):
        global user_id
        if user_id is not None:
            self.window_manager.convert_start_to_movie()
        return

    def convert_to_user(self):
        global user_id
        if user_id is not None:
            self.window_manager.convert_start_to_user()
        return

    def sign_up(self):
        id = self.ui.lineEdit_sign_up_user_id.text()
        pwd = self.ui.lineEdit_sign_up_user_pwd.text()

        if len(id) < 4 or len(pwd) < 4:
            self.ui.label_sign_up_result.setText("아이디와 비밀번호가 너무 짧거나 없습니다!")
            return
        
        manage_db.add_user_info(self.odb_con, id, pwd)
        self.ui.label_sign_up_result.setText(id + "님, 가입을 축하드립니다!")
        return

    def sign_in(self):
        global user_id
        id = self.ui.lineEdit_sign_in_user_id.text()
        pwd = self.ui.lineEdit_sign_in_user_pwd.text()

        if len(id) < 4 or len(pwd) < 4:
            self.ui.label_sign_in_result.setText("아이디와 비밀번호가 너무 짧거나 없습니다!")
            return
        
        if manage_db.check_user_info(self.odb_con, id, pwd) == False:
            self.ui.label_sign_in_result.setText("아이디 또는 비번이 잘못 입력되었습니다.")
            return
        
        user_id = id
        self.ui.label_sign_in_result.setText(id + "님, 반갑습니다.")
        

    
class MovieWindow(QMainWindow):
    def __init__(self, window_manager, odb_con: oracledb.Connection):
        super(MovieWindow, self).__init__()

        self.window_manager = window_manager
        self.odb_con = odb_con

        self.cinema_list = []
        self.cinema = None
        self.movie_list = []
        self.movie = None
        self.ms_id = None
        self.seat = None

        self.ui = movie_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_cinema_widget()

        self.ui.pushButton_sign_in_menu.clicked.connect(self.convert_to_start)
        self.ui.pushButton_user_info_menu.clicked.connect(self.convert_to_user)

        self.ui.pushButton_select_cinema.clicked.connect(self.select_cinema)
        self.ui.pushButton_select_movie.clicked.connect(self.select_movie)
        self.ui.pushButton_book.clicked.connect(self.select_seat)
        self.ui.pushButton_purchase.clicked.connect(self.do_purchase)

    def set_cinema_widget(self):
        cinema_list = manage_db.get_cinema_table(self.odb_con)
        for cinema in cinema_list:
            self.cinema_list.append([cinema[1], cinema[2]])
        
        self.ui.tableWidget_cinema.setColumnCount(2)
        self.ui.tableWidget_cinema.setRowCount(len(self.cinema_list))
        
        for row in range(len(self.cinema_list)):
            for col in range(2):
                self.ui.tableWidget_cinema.setItem(row, col, QTableWidgetItem(str(self.cinema_list[row][col])))

    def set_movie_by_cinema_widget(self):
        self.movie_list = []
        movie_list = manage_db.get_movieschdule_table_by_cinema(self.odb_con, self.cinema)
        for movie in movie_list:
            self.movie_list.append([movie[0], movie[1], movie[2], movie[3], movie[4], movie[5], movie[6]])
        
        self.ui.tableWidget_movie.clear()
        self.ui.tableWidget_movie.setColumnCount(6)
        self.ui.tableWidget_movie.setRowCount(len(self.movie_list))
        
        for row in range(len(self.movie_list)):
            for col in range(7):
                self.ui.tableWidget_movie.setItem(row, col, QTableWidgetItem(str(self.movie_list[row][col])))

    
    def show_window(self, geometry):
        if geometry is not None:
            self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        self.show()
        return

    def get_window_geometry(self):
        return [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
    
    def convert_to_start(self):
        self.window_manager.convert_movie_to_start()

    def convert_to_user(self):
        self.window_manager.convert_movie_to_user()

    def select_cinema(self):
        self.cinema = self.ui.tableWidget_cinema.item(self.ui.tableWidget_cinema.currentRow(), 0).text()
        self.ms_id = None
        self.movie = None
        self.ui.label_cinema_name.setText(self.cinema)
        self.ui.label_movie_name.setText("")
        self.set_movie_by_cinema_widget()

    def select_movie(self):
        self.ms_id = self.ui.tableWidget_movie.item(self.ui.tableWidget_movie.currentRow(), 0).text()
        self.movie = self.ui.tableWidget_movie.item(self.ui.tableWidget_movie.currentRow(), 3).text()
        self.ui.label_movie_name.setText(self.movie)

    def select_seat(self):
        print("okay")
        if self.cinema is None or self.ms_id is None:
            self.label_purchase_result.setText("아직 영화관과 영화가 설정되지 않았습니다.")
            return
        self.seat = self.ui.lineEdit_seat.text()
        if self.seat[0] >= 'A' and self.seat[0] < 'F':
            self.ui.label_ticket_price_2.setText("10000")
        else:
            self.ui.label_ticket_price_2.setText("12000")
    
    def do_purchase(self):
        global user_id
        if self.cinema is None or self.ms_id is None or self.seat is None:
            self.label_purchase_result.setText("아직 영화관, 영화, 좌석이 설정되지 않았습니다.")
            return
        manage_db.add_book(self.odb_con, user_id, self.ms_id, self.seat)
        self.ui.label_purchase_result.setText(self.cinema + ", " + self.movie + ", " + self.seat + " 결제 완료되었습니다!")
            

class UserWindow(QMainWindow):
    def __init__(self, window_manager, odb_con: oracledb.Connection):
        super(UserWindow, self).__init__()

        self.window_manager = window_manager
        self.odb_con = odb_con

        self.ui = user_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_sign_in_menu.clicked.connect(self.convert_to_start)
        self.ui.pushButton_movie_select_menu.clicked.connect(self.convert_to_movie)

    def show_window(self, geometry):
        if geometry is not None:
            self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        self.show()
        self.set_user_book_info()
        return

    def get_window_geometry(self):
        return [self.geometry().x(), self.geometry().y(), self.geometry().width(), self.geometry().height()]
    
    def convert_to_start(self):
        self.window_manager.convert_user_to_start()

    def convert_to_movie(self):
        self.window_manager.convert_user_to_movie()

    def set_user_book_info(self):
        global user_id

        self.ui.label_user_id_info.setText(user_id)
        user_book_info = manage_db.get_book_info_by_user(self.odb_con, user_id)
        self.ui.tableWidget_user_book.clear()
        self.ui.tableWidget_user_book.setColumnCount(7)
        self.ui.tableWidget_user_book.setRowCount(len(user_book_info))

        for row in range(len(user_book_info)):
            for col in range(7):
                self.ui.tableWidget_user_book.setItem(row, col, QTableWidgetItem(str(user_book_info[row][col])))
        return
        
        
    
class WindowManager:
    def __init__(self, odb_con: oracledb.Connection):
        self.odb_con = odb_con

        self.app = QApplication()
        self.start_window = StartWindow(self, odb_con)
        self.movie_window = MovieWindow(self, odb_con)
        self.user_window = UserWindow(self, odb_con)
        self.start_window.show()
        self.app.exec()

    def convert_start_to_movie(self):
        geometry = self.start_window.get_window_geometry()
        self.start_window.hide()
        self.movie_window.show_window(geometry)
    
    def convert_start_to_user(self):
        geometry = self.start_window.get_window_geometry()
        self.start_window.hide()
        self.user_window.show_window(geometry)
    
    def convert_movie_to_start(self):
        geometry = self.movie_window.get_window_geometry()
        self.movie_window.hide()
        self.start_window.show_window(geometry)

    def convert_movie_to_user(self):
        geometry = self.movie_window.get_window_geometry()
        self.movie_window.hide()
        self.user_window.show_window(geometry)

    def convert_user_to_start(self):
        geometry = self.user_window.get_window_geometry()
        self.user_window.hide()
        self.start_window.show_window(geometry)

    def convert_user_to_movie(self):
        geometry = self.user_window.get_window_geometry()
        self.user_window.hide()
        self.movie_window.show_window(geometry)

def init_db(odb_con: oracledb.Connection):
    manage_db.create_table(odb_con)
    manage_db.add_movie_info(odb_con)
    manage_db.add_cinema_info(odb_con)
    manage_db.add_movie_schedule_info(odb_con)

def close_db(odb_con: oracledb.Connection):
    manage_db.drop_table(odb_con)
    odb_con.close()
    os._exit(0)

if __name__ == "__main__":
    odb_con = oracledb.connect(user="system", password="1234", host="localhost", port=1521, service_name="orcl")
    init_db(odb_con)
    manage_db.add_user_info(odb_con, "abc", "1234")
    manage_db.add_user_info(odb_con, "dfc", "3456")
    manage_db.add_book_info(odb_con, "abc", "10b", '고려대학교 동대문점', '3', '그대들은 어떻게 살 것인가', '2023/12/06', '10:00')
    manage_db.get_book_info_by_user(odb_con, "abc")
    manage_db.view_table(odb_con)

    window_manager = WindowManager(odb_con)

    close_db(odb_con)
