import peewee as pw
from pathlib import Path

ROOT = Path().resolve() / "data" / "wordcloud"
ROOT.mkdir(parents=True, exist_ok=True)
db = pw.SqliteDatabase(ROOT / "db.sqlite3")


class Record(pw.Model):
    user_id = pw.IntegerField()
    group_id = pw.IntegerField()
    message = pw.CharField()
    timestamp = pw.IntegerField()

    class Meta:
        database = db


if not Path.exists(ROOT / "db.sqlite3"):
    db.connect()
    db.create_tables([Record])
    db.close()
