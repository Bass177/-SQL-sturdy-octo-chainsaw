"""create orders

Revision ID: c437a3ad382c
Revises: 96d234c35eac
Create Date: 2022-05-12 13:15:27.215679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c437a3ad382c'
down_revision = '96d234c35eac'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE orders(
            id SERIAL PRIMARY KEY,
            dollar_amount_spent NUMERIC,
            customer_id INT NOT NULL,
            CONSTRAINT fk_orders_customers
                FOREIGN KEY (customer_id)
                REFERENCES customers(id)
                ON DELETE CASCADE
        );
        """
    )
    pass


def downgrade():
    op.execute(
        """
        DROP TABLE orders;
        """
    )
    pass
