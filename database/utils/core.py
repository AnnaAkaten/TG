from python_basic_diploma.database.commands import CRUDInterface
from python_basic_diploma.database.common.models import History, db
# db.connect()
db.create_tables([History])
crud = CRUDInterface()

if __name__ == '__main__':
    crud()
