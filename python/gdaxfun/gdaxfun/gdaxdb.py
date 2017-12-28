from pony.orm import *
from decimal import Decimal
from datetime import time
from gdaxtables import define_tables
#=========================================================================
# This class manage the functions to store json results into a database.
# Default will be sqlite, but you can point it to a different database if
# necessary. We utilize Pony ORM (https://docs.ponyorm.com) an
# Object-Relational-Mappers to abstract the direct access to the database
# so we can migrate and appoint to any type of supported database
# afterward without changing our code.
#
# See: https://www.fullstackpython.com/object-relational-mappers-orms.html
# Supported database will be SQLite (default), PostgreSQL, and MySQL.
# You will need to install additional drivers for other database if you are
# not using SQLite.
#=========================================================================


class GdaxDBLabel(object):
    SQLITE = 1
    POSTGRES = 2
    MYSQL = 3


class GdaxDB():

    def __init__(self, db_label, **params):
        db = Database()
        define_tables(db)
        if db_label == GdaxDBLabel.SQLITE:
            db.bind(provider='sqlite',
                    filename=params['sqlite']['file_path'], create_db=True)
        elif db_label == GdaxDBLabel.MYSQL:
            # db.bind(provider='mysql', host='', user='', passwd='', db='')
            raise Exception("MySQL is not supported yet!")
        elif db_label == GdaxDBLabel.POSTGRES:
            # db.bind(provider='postgres', user='',
            #              password='', host='', database='')
            raise Exception("PostgreSQL is not supported yet!")
        else:
            raise Exception("Cannot find supported database ID " + db_label)
        self.db = db

    def initdb(self):
        self.db.generate_mapping(create_tables=True)

    @db_session
    def insert_record(self, dparams):
        t = self.db.TradeHistory(**dparams)
        commit()

    @db_session
    def query_record(self, tid):
        t = self.db.TradeHistory.get(trade_id=tid)
        return t.to_dict()

    @db_session
    def delete_record(self, tid):
        t = self.db.TradeHistory.get(trade_id=tid)
        t.delete()

    @db_session
    def count_records(self):
        return count(t for t in self.db.TradeHistory)
