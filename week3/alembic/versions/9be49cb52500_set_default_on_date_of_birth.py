"""set default on date_of_birth 

Revision ID: 9be49cb52500
Revises: 537bcd96f37f
Create Date: 2022-05-12 12:56:55.483937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9be49cb52500'
down_revision = '537bcd96f37f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET DEFAULT now();
        """
    )
    pass


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP DEFAULT;
        """
    )
    pass
