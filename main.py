from sqlalchemy import create_engine, select, update, delete, and_, or_, any_
from sqlalchemy.orm import Session, sessionmaker

from models import Category, Product


cat = Category()
cat.execute()
# cats = Category.all()
# print(cats)

# cat = Category(name='Tea')
# cat.save()
# print(cat.id, cat.name)

# with Category.session() as session:
#     cat = session.get(Category, 4)
# cat = Category.get(4)
# cat.name = 'Tea'
# cat.save()

# with session() as session:
#     coffee = Category(name='Coffee')
#     session.add(coffee)
#     session.commit()
#     session.refresh(coffee)
#     print(coffee.name)

# with session() as session:
#     obj = session.get(Category, 1)
#     obj.name = 'Sandwich'
#     session.add(obj)
#     session.commit()
    # print(obj.name, obj.id)
    # response = session.execute(
    #     select(Category)
    #     .order_by('name')
    # )
    # print(response.all())


# with Category.session() as session:
#     session.execute(
#         delete(Category)
#         .where(Category.id == 1)
#     )
#     session.commit()
    # obj = session.get(Category, 1)
    # session.delete(obj)
    # session.commit()
