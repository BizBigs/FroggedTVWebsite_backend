from .. import db

association_table = db.Table('link_ftv_user_ftv_roles', db.Model.metadata,
    db.Column('user_id', db.ForeignKey('ftv_user.id_user'), primary_key=True),
    db.Column('role_id', db.ForeignKey('ftv_roles.id_role'), primary_key=True)
)