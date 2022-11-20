"""ADD NOT NULL to date_of_birth

Revision ID: 537bcd96f37f
Revises: c9fe968e0e89
Create Date: 2022-05-12 09:02:29.739429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '537bcd96f37f'
down_revision = 'c9fe968e0e89'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET NOT NULL;
        """
    )
    pass


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP NOT NULL;
        """
    )
    pass
