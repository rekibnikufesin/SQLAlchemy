from entity import Session, engine, Base
from inventory import Inventory, History

Base.metadata.create_all(engine)
session = Session()

def get_inventory():
    inventory_items = session.query(Inventory).all()
    return inventory_items

def add_inventory(make, model, year, color):
    new_inv = Inventory(make, model, year, True, color)
    new_inv.history = [
        History(history_type='New car added'),
        History(history_type='Car crashed')
    ]
    session.add(new_inv)
    session.commit()

def rent_inventory(inventory_id):
    inv_item = session.query(Inventory).filter_by(id=inventory_id).first()
    inv_item.available = False
    session.commit()

def return_inventory(inventory_id):
    inv_item = session.query(Inventory).filter_by(id=inventory_id).first()
    inv_item.available = True
    session.commit()
