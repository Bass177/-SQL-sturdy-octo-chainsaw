"""rename date_of_birth

Revision ID: 96d234c35eac
Revises: 9be49cb52500
Create Date: 2022-05-12 13:10:39.083126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96d234c35eac'
down_revision = '9be49cb52500'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN date_of_birth to dob;
        """
    )
    pass


def downgrade():
    op.execute(
        """
        ALTER TABLE customers 
        RENAME COLUMN dob to date_of_birth;

        """
    )
    pass
