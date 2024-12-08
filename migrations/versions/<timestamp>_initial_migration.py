"""Initial migration

Revision ID: abc123xyz456
Revises: None
Create Date: 2024-12-06 10:00:00

"""
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'abc123xyz456'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create power_outages table
    op.create_table(
        'power_outages',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('location', sa.String(length=255), nullable=False),
        sa.Column('account_id', sa.String(length=100), nullable=False),
        sa.Column('ticket_id', sa.String(length=100), unique=True, nullable=False),
        sa.Column('status', sa.String(length=50), nullable=False, default='Pending'),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )

    # Create water_issues table
    op.create_table(
        'water_issues',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('location', sa.String(length=255), nullable=False),
        sa.Column('issue_type', sa.String(length=100), nullable=False),
        sa.Column('ticket_id', sa.String(length=100), unique=True, nullable=False),
        sa.Column('status', sa.String(length=50), nullable=False, default='Pending'),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )

    # Create ferry_missed_trips table
    op.create_table(
        'ferry_missed_trips',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('ticket_id', sa.String(length=100), unique=True, nullable=False),
        sa.Column('status', sa.String(length=50), nullable=False, default='Pending'),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )


def downgrade():
    # Drop the created tables
    op.drop_table('power_outages')
    op.drop_table('water_issues')
    op.drop_table('ferry_missed_trips')
