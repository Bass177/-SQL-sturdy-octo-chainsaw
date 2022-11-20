"""create students

Revision ID: 8a421e07f782
Revises: a835c7dfbb05
Create Date: 2022-05-26 13:48:08.564099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a421e07f782'
down_revision = 'a835c7dfbb05'
branch_labels = None
depends_on = None


def upgrade():
    """
    CREATE TABLE students;

    """
    pass


def downgrade():
    pass
