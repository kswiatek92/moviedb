"""populate db

Revision ID: ece9bc183ea7
Revises: 40390c2f5080
Create Date: 2020-04-09 23:28:00.740151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece9bc183ea7'
down_revision = '40390c2f5080'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO public.user (email, password) VALUES ('admin@example.com', '44b3ca6a6ee540220c2cc7ca24a62d4737219781d7b0e38f0b1bb83b55ded784e0c4e168eb9bbe97162b3d3ff621f54e67555820961ee5880ab57cc23049a166e01ae1b36682c7cd714bf6ee3102b67d2adc57e147a9cf2b04b9099d3ae7c4ec');")

def downgrade():
    pass
