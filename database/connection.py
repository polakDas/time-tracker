import peewee

db = peewee.SqliteDatabase('db.sqlite3')

class BaseModel(peewee.Model):
    class Meta:
        database = db