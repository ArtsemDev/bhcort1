from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://dev:password@localhost:5432/bhcorp')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls) -> str:
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with Base.session() as session:
                return func(*args, **kwargs, session=session)
        return wrapper

    @create_session
    def save(self, session: Session = None):
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, id_, session: Session = None):
        return session.get(cls, id_)

    @create_session
    def delete(self, session: Session = None):
        session.delete(self)
        session.commit()

    @classmethod
    @create_session
    def all(
            cls,
            order_by: str = 'id',
            limit: int = None,
            offset: int = None,
            session: Session = None,
            **kwargs
    ):
        objs = session.scalars(
            select(cls)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
            .filter_by(**kwargs)
        )
        return objs.all()

    def dict(self) -> dict:
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class Category(Base):
    # __tablename__ = 'category'

    name = Column(VARCHAR(64), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Product(Base):
    # __tablename__ = 'product'

    name = Column(VARCHAR(128), nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False)
    category_id = Column(ForeignKey('category.id', ondelete='CASCADE'), nullable=False)


class ProductImage(Base):
    url = Column(VARCHAR(256), nullable=False)
    product_id = Column(ForeignKey('product.id', ondelete='CASCADE'), nullable=False)