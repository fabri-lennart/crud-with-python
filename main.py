import pymysql
import configparser
from loguru import logger

config = configparser.ConfigParser()
config.read('config.ini')

# Access values
db_host = config['data_base']['host']
db_user = config['data_base']['user']
db_password = config['data_base']['password']
db_port = int(config['data_base']['port'])
db_name = config['data_base']['database']

connection = None  

try:
    logger.debug("Trying the connection")
    connection = pymysql.connect(
                 host=db_host,
                 port=db_port,
                 user=db_user,
                 password=db_password,
                 database=db_name)
    logger.info("Connection successful")
    
    
except pymysql.MySQLError as e:
    logger.error(f"DB connection failed: {e}")  

finally:
    if connection:
        connection.close()
        logger.info("Connection closed")

if __name__ == "__main__":
    pass
