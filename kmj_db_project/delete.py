import oracledb
import manage_db

if __name__ == "__main__":
    odb_con = oracledb.connect(user="system", password="1234", host="localhost", port=1521, service_name="orcl")
    manage_db.drop_table(odb_con)
    odb_con.close()