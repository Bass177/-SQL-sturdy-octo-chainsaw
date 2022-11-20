"""add customers date_of_birth

Revision ID: c9fe968e0e89
Revises: 957cd7b8194c
Create Date: 2022-05-11 17:15:53.040472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9fe968e0e89'
down_revision = '957cd7b8194c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """

    )
    


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP column date_of_birth;
        """
    )
    
