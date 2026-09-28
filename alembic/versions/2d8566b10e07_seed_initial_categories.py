"""seed_initial_categories

Revision ID: 2d8566b10e07
Revises: bdfb2d6b6e35
Create Date: 2026-09-28 14:01:25.007849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d8566b10e07'
down_revision: Union[str, Sequence[str], None] = 'bdfb2d6b6e35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

categories_table = sa.table(
    'categories',
    sa.Column('id', sa.Integer),
    sa.Column('name', sa.String)
)

def upgrade() -> None:
    op.bulk_insert(categories_table, [
        {'id': 1, 'name': 'Fitness'},
        {'id': 2, 'name': 'Work'},
        {'id': 3, 'name': None},
        {'id': 4, 'name': None},
        {'id': 5, 'name': 'Health'}
    ])


def downgrade() -> None:
    op.execute("DELETE FROM categories WHERE id IN (1, 2, 3, 4, 5)")
