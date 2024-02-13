import oracledb

def create_table(odb_con: oracledb.Connection):
    create_movie_table_query = """
    CREATE TABLE movie
    (
        id  NUMBER(5)  GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
        moviename   VARCHAR2(100)       NOT NULL,
        director    VARCHAR2(30),
        releasedate VARCHAR2(12),
        janre       VARCHAR2(30)
    )
    """
    with odb_con.cursor() as cursor:
        cursor.execute(create_movie_table_query)

    create_cinema_table_query = """
    CREATE TABLE cinema
    (
        id  NUMBER(5)  GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
        cinemaname  VARCHAR2(100)       NOT NULL,
        location    VARCHAR2(200),
        numberoftheater NUMBER(5)
    )
    """
    with odb_con.cursor() as cursor:
        cursor.execute(create_cinema_table_query)
    
    create_movie_schedule_table_query = """
    CREATE TABLE movieschedule
    (
        id  NUMBER(5)  GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
        cinemaname  VARCHAR2(100)       NOT NULL,
        cinemanumber    NUMBER(5)       NOT NULL,
        moviename   VARCHAR2(100)       NOT NULL,
        startdate   VARCHAR2(12)        NOT NULL,
        starttime   VARCHAR2(30)        NOT NULL,
        endtime     VARCHAR2(30)        NOT NULL       
    )
    """
    with odb_con.cursor() as cursor:
        cursor.execute(create_movie_schedule_table_query)

    create_userinfo_table_query = """
    CREATE TABLE userinfo
    (
        id  NUMBER(5)  GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
        userid      VARCHAR2(30)        NOT NULL,
        userpwd     VARCHAR2(30)        NOT NULL,
        isdelete    NUMBER(1)           NOT NULL
    )
    """
    with odb_con.cursor() as cursor:
        cursor.execute(create_userinfo_table_query)
    
    create_book_table_query = """
    CREATE TABLE book
    (
        id  NUMBER(5)  GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
        moviescheduleid NUMBER(5)       NOT NULL,
        userid      VARCHAR2(30)        NOT NULL,
        seat        VARCHAR2(10)        NOT NULL,
        isdelete    NUMBER(1)           NOT NULL 
    )
    """
    with odb_con.cursor() as cursor:
        cursor.execute(create_book_table_query)
    return

def drop_table(odb_con: oracledb.Connection):
    drop_movie_table_query = "DROP TABLE movie CASCADE CONSTRAINTS"
    drop_cinema_table_query = "DROP TABLE cinema CASCADE CONSTRAINTS"
    drop_movieschedule_table_query = "DROP TABLE movieschedule CASCADE CONSTRAINTS"
    drop_userinfo_table_query = "DROP TABLE userinfo CASCADE CONSTRAINTS"
    drop_book_table_query = "DROP TABLE book CASCADE CONSTRAINTS"

    with odb_con.cursor() as cursor:
        cursor.execute(drop_movie_table_query)
        cursor.execute(drop_cinema_table_query)
        cursor.execute(drop_movieschedule_table_query)
        cursor.execute(drop_userinfo_table_query)
        cursor.execute(drop_book_table_query)
    return 

def view_table(odb_con: oracledb.Connection):
    view_movie_table_query = "SELECT * FROM movie"
    view_cinema_table_query = "SELECT * FROM cinema"
    view_movie_schedule_table_query = "SELECT * FROM movieschedule"
    view_userinfo_table_query = "SELECT * FROM userinfo"
    view_book_table_query = "SELECT * FROM book"
    with odb_con.cursor() as cursor:
        cursor.execute(view_movie_table_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.execute(view_cinema_table_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.execute(view_movie_schedule_table_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.execute(view_userinfo_table_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.execute(view_book_table_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)  
    return

def get_cinema_table(odb_con: oracledb.Connection):
    view_cinema_table_query = "SELECT * FROM cinema"
    with odb_con.cursor() as cursor:
        cursor.execute(view_cinema_table_query)
        rows = cursor.fetchall()
        return rows
    
def get_movieschdule_table_by_cinema(odb_con: oracledb.Connection, cinema: str):
    view_ms_table_query = "SELECT * FROM movieschedule WHERE cinemaname = " + "\'" + str(cinema) + "\'"
    with odb_con.cursor() as cursor:
        cursor.execute(view_ms_table_query)
        rows = cursor.fetchall()
        return rows

def add_movie_info(odb_con: oracledb.Connection):
    movie_list =[
        ['오펜하이머', '크리스토퍼 놀런', '2023/08/15', 'SF'],
        ['가디언즈 오브 갤럭시: Volume 3', '제임스 건', '2023/05/05', '액션'],
        ['그대들은 어떻게 살 것인가', '미야자키 하야오', '2023/10/25', '애니메이션'],
        ['범죄도시3', '이상용', '2023/05/31', '액션']
    ]
    add_movie_queries = []
    for movie in movie_list:
        add_movie_queries.append(
        """
        INSERT INTO movie
        (
            moviename,
            director,
            releasedate,
            janre
        )
        VALUES
        (
        """ + "\'" + movie[0] + "\'" + ", "
        + "\'" + movie[1] + "\'" + ", "
        + "\'" + movie[2] + "\'" + ", "
        + "\'" + movie[3] + "\'" + ")" )
    for add_movie_query in add_movie_queries:
        with odb_con.cursor() as cursor:
            cursor.execute(add_movie_query)
        odb_con.commit()
    return

def add_cinema_info(odb_con: oracledb.Connection):
    cinema_list = [
        ['고려시네마 동대문점', '서울시 동대문구 동대문앞길 321', '3'],
        ['백제시네마 군산점', '전라북도 군산시 미룡동 대학로 558', '2'],
        ['신라시네마 청주점', '충청북도 청주시 상동구 남일면 단재로 635', '2']
    ]
    add_cinema_queries = []
    for cinema in cinema_list:
        add_cinema_queries.append(
        """
        INSERT INTO cinema
        (
            cinemaname,
            location,
            numberoftheater
        )
        VALUES
        (
        """ 
        + "\'" + cinema[0] + "\'" + ", "
        + "\'" + cinema[1] + "\'" + ", "
        + cinema[2] + ") "
        )
    for add_cinema_query in add_cinema_queries:
        with odb_con.cursor() as cursor:
            cursor.execute(add_cinema_query)
        odb_con.commit()
    return

def add_movie_schedule_info(odb_con: oracledb.Connection):
    movie_schedule_list = [
        ['고려시네마 동대문점', '1', '오펜하이머', '2023/12/05', '10:00', '12:00'],
        ['고려시네마 동대문점', '2', '가디언즈 오브 갤럭시: Volume 3', '2023/12/05', '13:00', '15:00'],
        ['고려시네마 동대문점', '3', '그대들은 어떻게 살 것인가', '2023/12/06', '10:00', '12:00'],
        ['백제시네마 군산점', '1', '범죄도시3', '2023/12/05', '09:00', '12:00'],
        ['백제시네마 군산점', '2', '오펜하이머', '2023/12/06', '10:00', '12:00'],
        ['신라시네마 청주점', '1', '가디언즈 오브 갤럭시: Volume 3', '2023/12/05', '11:00', '13:00'],
        ['신라시네마 청주점', '2', '범죄도시3', '2023/12/06', '15:00', '18:00']
    ]
    add_movie_schedule_queries = []
    for movie_schedule in movie_schedule_list:
        add_movie_schedule_queries.append(
        """
        INSERT INTO movieschedule
        (
            cinemaname,
            cinemanumber,
            moviename,
            startdate,
            starttime,
            endtime
        )
        VALUES
        (
        """ + "\'" + movie_schedule[0] + "\'" + ", "
        + movie_schedule[1] + ", "
        + "\'" + movie_schedule[2] + "\'" + ", "
        + "\'" + movie_schedule[3] + "\'" + ", "
        + "\'" + movie_schedule[4] + "\'" + ", "
        + "\'" + movie_schedule[5] + "\'" + ")"
        )
    for add_movie_schedule_query in add_movie_schedule_queries:
        with odb_con.cursor() as cursor:
            cursor.execute(add_movie_schedule_query)
        odb_con.commit()
    return

def add_user_info(odb_con: oracledb.Connection, id: str, pwd: str):
    add_user_query = str("""
    INSERT INTO userinfo
    (
        userid,
        userpwd,
        isdelete
    )
    VALUES
    (
    """ + "\'" + id + "\'" + ", "
    + "\'" + pwd + "\'" + ", "
    + "0" + ")")

    with odb_con.cursor() as cursor:
        cursor.execute(add_user_query)
    odb_con.commit()
    return

def check_user_info(odb_con: oracledb.Connection, id: str, pwd: str):
    check_user_query = str("""
    SELECT COUNT(*)
    FROM userinfo
    WHERE userid  = """ + "\'" + str(id) + "\'"
    + " AND userpwd = " + "\'" + str(pwd) + "\'")

    is_user = False
    with odb_con.cursor() as cursor:
        cursor.execute(check_user_query)
        row = cursor.fetchone()
        if int(row[0]) > 0:
            is_user = True
    
    return is_user
    
    


def get_len_db(odb_con: oracledb.Connection, table_name):
    len_count_query = "SELECT COUNT(*) FROM " + str(table_name)
    number_db = 0
    with odb_con.cursor() as cursor:
        cursor.execute(len_count_query)
        row = cursor.fetchone()
        number_db = int(row[0])
    return row[0]

def add_book(odb_con: oracledb.Connection, user_id, movie_schedule_id, seat):
    add_book_query = str("""
    INSERT INTO book
    (
        moviescheduleid,
        userid,
        seat,
        isdelete
    )
    VALUES
    (
    """ + str(movie_schedule_id) + ", "
    + "\'" + str(user_id) + "\'" + ", "
    + "\'" + str(seat) + "\'" + ", "
    + "\'0\' )" )
    with odb_con.cursor() as cursor:
        cursor.execute(add_book_query)
    odb_con.commit()
    
    return

def add_book_info(odb_con: oracledb.Connection, user_id, seat, cinema_name, cinema_number, movie_name, start_date, start_time):
    movie_schedule_id = 0

    movie_schedule_search_query = str("""
    SELECT id 
    FROM movieschedule 
    WHERE cinemaname = """ + "\'" + cinema_name + "\'"
    + " AND cinemanumber = " + cinema_number
    + " AND moviename = " + "\'" + movie_name + "\'"
    + " AND startdate = " + "\'" + start_date + "\'"
    + " AND starttime = " + "\'" + start_time + "\'")

    with odb_con.cursor() as cursor:
        cursor.execute(movie_schedule_search_query)
        rows = cursor.fetchall()
        if len(rows) != 1:
            return -1
        for row in rows:
            movie_schedule_id = int(row[0])
    
    add_book_query = str("""
    INSERT INTO book
    (
        moviescheduleid,
        userid,
        seat,
        isdelete
    )
    VALUES
    (
    """ + str(movie_schedule_id) + ", "
    + "\'" + str(user_id) + "\'" + ", "
    + "\'" + str(seat) + "\'" + ", "
    + "\'0\' )" )
    with odb_con.cursor() as cursor:
        cursor.execute(add_book_query)
    odb_con.commit()
    
    return

def get_book_info_by_user(odb_con: oracledb.Connection, user_id):
    book_info_user_search_query = str("""
    SELECT *
    FROM book
    WHERE userid = """ 
    + "\'" + str(user_id) + "\'")

    books = []
    with odb_con.cursor() as cursor:
        cursor.execute(book_info_user_search_query)
        rows = cursor.fetchall()
        for row in rows:
            books.append(list(row))

    for idx1 in range(len(books)):
        schedule_search_query = str("""
        SELECT *
        FROM movieschedule
        WHERE id = """
        + str(books[idx1][1]))

        with odb_con.cursor() as cursor:
            cursor.execute(schedule_search_query)
            rows = cursor.fetchall()
            for row in rows:
                for ele1 in row:
                    books[idx1].append(ele1)
    
    book_infos = []
    for book in books:
        book_infos.append([book[3], book[6], book[8], book[9], book[10], book[11], book[4], book[2]])
    
    return book_infos