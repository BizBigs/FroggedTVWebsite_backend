from . import db, ma
from marshmallow import fields, validate
from .LinkTables.UserToRole import association_table

class RoleModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'ftv_roles'

    id_role = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True)
    users = db.relationship("UserModel", secondary=association_table, back_populates="roles")

    def addRole(newRole):
        db.session.add(newRole)
        db.session.commit()

    def deleteRole(roleToDelete):
        db.session.delete(roleToDelete)
        db.session.commit()

    def updateRole(roleToUpdate, updateValues):
        roleToUpdate.update(updateValues, synchronize_session="fetch")
        db.session.commit()

    def __repr__(self):
        return '<User Id: %s>' % self.id_role

class RoleSchema(ma.Schema):
  role_name = fields.String(required=True)
  class Meta:
    fields = ("role_name",)

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)