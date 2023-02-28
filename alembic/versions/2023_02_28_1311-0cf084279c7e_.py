"""empty message

Revision ID: 0cf084279c7e
Revises: 0d5d86e756fd
Create Date: 2023-02-28 13:11:48.814739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError

# revision identifiers, used by Alembic.
revision = '0cf084279c7e'
down_revision = '0d5d86e756fd'
branch_labels = None
depends_on = None

from models import Category

categories = ('Coffee', 'Tea', 'Hamburger')


def upgrade() -> None:
    for category in categories:
        category = Category(name=category)
        try:
            category.save()
        except IntegrityError:
            pass


def downgrade() -> None:
    with Category.session() as session:
        for category in categories:
            session.execute(delete(Category).where(Category.name == category))
            session.commit()
