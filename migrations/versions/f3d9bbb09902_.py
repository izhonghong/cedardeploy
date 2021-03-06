"""empty message

Revision ID: f3d9bbb09902
Revises: 
Create Date: 2018-11-07 18:07:31.725512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3d9bbb09902'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_config',
    sa.Column('project_name', sa.String(length=64), nullable=False),
    sa.Column('config1', sa.Text(), nullable=True),
    sa.Column('config2', sa.Text(), nullable=True),
    sa.Column('config3', sa.Text(), nullable=True),
    sa.Column('config4', sa.Text(), nullable=True),
    sa.Column('config5', sa.Text(), nullable=True),
    sa.Column('config6', sa.Text(), nullable=True),
    sa.Column('config7', sa.Text(), nullable=True),
    sa.Column('config8', sa.Text(), nullable=True),
    sa.Column('config9', sa.Text(), nullable=True),
    sa.Column('config10', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('project_name')
    )
    op.create_table('projectinfo',
    sa.Column('project_name', sa.String(length=64), nullable=False),
    sa.Column('project', sa.String(length=64), nullable=True),
    sa.Column('environment', sa.String(length=64), nullable=True),
    sa.Column('branch', sa.String(length=64), nullable=True),
    sa.Column('type', sa.String(length=10), nullable=True),
    sa.Column('git', sa.String(length=1024), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('make', sa.Text(), nullable=True),
    sa.Column('istag', sa.String(length=10), nullable=True),
    sa.Column('isnginx', sa.String(length=10), nullable=True),
    sa.Column('business', sa.String(length=40), nullable=True),
    sa.Column('ischeck', sa.String(length=10), nullable=True),
    sa.Column('checkurl', sa.String(length=300), nullable=True),
    sa.Column('statuscode', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('project_name')
    )
    op.create_table('serverinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=64), nullable=True),
    sa.Column('hostname', sa.String(length=64), nullable=True),
    sa.Column('ip', sa.String(length=64), nullable=True),
    sa.Column('variable1', sa.String(length=64), nullable=True),
    sa.Column('variable2', sa.String(length=64), nullable=True),
    sa.Column('variable3', sa.String(length=64), nullable=True),
    sa.Column('variable4', sa.String(length=64), nullable=True),
    sa.Column('variable5', sa.String(length=64), nullable=True),
    sa.Column('variable6', sa.String(length=64), nullable=True),
    sa.Column('variable7', sa.String(length=64), nullable=True),
    sa.Column('variable8', sa.String(length=64), nullable=True),
    sa.Column('variable9', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_serverinfo_project_name'), 'serverinfo', ['project_name'], unique=False)
    op.create_table('updatelog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('taskid', sa.String(length=64), nullable=True),
    sa.Column('project_name', sa.String(length=64), nullable=True),
    sa.Column('host', sa.String(length=2000), nullable=True),
    sa.Column('tag', sa.String(length=64), nullable=True),
    sa.Column('rtime', sa.String(length=32), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('loginfo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_updatelog_taskid'), 'updatelog', ['taskid'], unique=False)
    op.create_table('updateoperation',
    sa.Column('taskid', sa.String(length=64), nullable=False),
    sa.Column('project_name', sa.String(length=64), nullable=True),
    sa.Column('hostlist', sa.String(length=2000), nullable=True),
    sa.Column('tag', sa.String(length=64), nullable=True),
    sa.Column('rtime', sa.String(length=32), nullable=True),
    sa.Column('operation', sa.String(length=64), nullable=True),
    sa.Column('loginfo', sa.String(length=6400), nullable=True),
    sa.Column('user', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('taskid')
    )
    op.create_index(op.f('ix_updateoperation_taskid'), 'updateoperation', ['taskid'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('_password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('userservicegroup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('servicegroup', sa.String(length=64), nullable=True),
    sa.Column('permissions', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workorder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group', sa.String(length=64), nullable=True),
    sa.Column('project', sa.String(length=64), nullable=True),
    sa.Column('applicant', sa.String(length=64), nullable=True),
    sa.Column('applicationtime', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('executor', sa.String(length=64), nullable=True),
    sa.Column('completiontime', sa.String(length=64), nullable=True),
    sa.Column('remarks', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workorder')
    op.drop_table('userservicegroup')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_updateoperation_taskid'), table_name='updateoperation')
    op.drop_table('updateoperation')
    op.drop_index(op.f('ix_updatelog_taskid'), table_name='updatelog')
    op.drop_table('updatelog')
    op.drop_index(op.f('ix_serverinfo_project_name'), table_name='serverinfo')
    op.drop_table('serverinfo')
    op.drop_table('projectinfo')
    op.drop_table('project_config')
    # ### end Alembic commands ###
