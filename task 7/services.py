import os
import csv
import re
import sqlite3

DATA_FOLDER = 'static/'
DB_FOLDER = './database/database.db'


class Service:
    def __init__(self):
        self._conn = sqlite3.connect(DB_FOLDER)
        self._db = self._conn.cursor()
        self._preparation()

    def __create_table_on_db__(self):
        self._db.execute("PRAGMA encoding = 'UTF-8';")
        self._db.execute("""CREATE TABLE IF NOT EXISTS data(
            code INT,
            after INT,
            before INT,
            container INT,
            operator varchar(100),
            region varchar(100)
            );""")

    def _preparation(self):

        self.__create_table_on_db__()
        self._db.execute('SELECT COUNT(*) FROM data')
        count = self._db.fetchall()
        if count[0][0] == 0:
            self.__read_all_data__()

    def find_info(self, phone):
        regex = re.compile('\\D+')
        number = regex.sub('', phone)[1:]

        code = number[0:3]
        body = number[3:]

        info = self.__select_from_db__(code, body)

        return info[0]

    def __select_from_db__(self, code, body):
        cursor = sqlite3.connect(DB_FOLDER).cursor()
        cursor.execute('''SELECT * FROM data
                          WHERE (after <= {} AND before >= {}) AND code = {};'''.format(body, body, code))
        return cursor.fetchall()

    def __read_all_data__(self):
        files = os.listdir(DATA_FOLDER)
        for f in files:
            file = open(DATA_FOLDER + f, 'r', encoding="utf-8")
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                self.__write_data_in_db__(row)
        self._conn.commit()

    def __write_data_in_db__(self, d):
        self._db.execute('''INSERT INTO data (code, after, before, container, operator, region)
                         VALUES ({}, {}, {}, {}, '{}', '{}')'''
                         .format(d['АВС/ DEF'], d['От'], d['До'], d['Емкость'], d['Оператор'], d['Регион']))

