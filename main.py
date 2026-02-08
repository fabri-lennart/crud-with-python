import pymysql
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

# Access values
db_host = config['data_base']['host']
db_user = config['data_base']['user']
db_password = config['data_base']['password']
db_port = int(config['data_base']['port'])
db_name = config['data_base']['database']

# do the conection

try:
    connection = pymysql.connect(
                 host=db_host,
                 port=db_port,
                 user=db_user,
                 password=db_password,
                 database=db_name)
    print("connection was success")
except pymysql.MySQLError as e:
    print("DB connection failed:", e)


if __name__ == "__main__":
    pass
