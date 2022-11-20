"""create customers

Revision ID: 957cd7b8194c
Revises: 
Create Date: 2022-05-11 16:56:53.017226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '957cd7b8194c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
    pass
