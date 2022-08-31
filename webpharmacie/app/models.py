
from datetime import datetime
from app import db, lm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(64), nullable=False, unique=False)
    firstname = db.Column(db.String(646), nullable=False, unique=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(500))
    is_admin = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, index=False,
                           unique=False, nullable=False)

    def __init__(self, lastname, firstname, email, password):
        self.lastname = lastname
        self.firstname = firstname
        self.password = password
        self.email = email
        self.is_admin = False
        self.created_on = datetime.now()

    def set_password(self, password):
        """create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r - %s>' % (self.id) % (self.email)

    def save(self):

        # inject self into db session
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self


class Medicament(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    prixu = db.Column(db.Integer)
    designation = db.Column(db.String(80))
    quantite = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)

    def __init__(self, name, prixu, designation, quantite, category_id):
        self.name = name
        self.prixu = prixu
        self.designation = designation
        self.quantite = quantite
        self.category_id = category_id

    def save(self):

        # inject self into db session
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Medicament %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def save(self):

        # inject self into db session
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Category %r>' % self.name


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(64), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    telephone = db.Column(db.String(64), nullable=False)
    adresse = db.Column(db.String(64), nullable=False)
    numsecurite = db.Column(db.String(64), nullable=False)

    def __init__(self, lastname, firstname, telephone, adresse, numsecurite) -> None:
        self.lastname = lastname
        self.firstname = firstname
        self.telephone = telephone
        self.adresse = adresse
        self.numsecurite = numsecurite

    def save(self):

        # inject self into db session
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Client %r>' % self.name


class Vente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_vente = db.Column(db.DateTime)
    medicament_id = db.Column(db.Integer, db.ForeignKey(
        'medicament.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=True)
    quantite = db.Column(db.Integer, nullable=False)
    montantTo = db.Column(db.Numeric, nullable=False)

    def __init__(self, transaction_vente, medicament_id, client_id, quantite, montantTo):
        """sumary_line
    
        Keyword arguments:
        argument -- all args on property class
        Return: none 
    """

        if transaction_vente is None:
            self.transaction_vente = datetime.utcnow()
        self.transaction_vente = transaction_vente
        self.medicament_id = medicament_id
        self.client_id = client_id
        self.quantite = quantite
        self.montantTo = montantTo

    def save(self):

        # inject self into db session
        db.session.add(self)
        # commit change and save the object
        db.session.commit()

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Vente %r>' % self.id


class Stats(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True)
    val = db.Column(db.Integer)
    val_s = db.Column(db.String(256))

    def __init__(self, key):
        self.key = key

        db_obj = Stats.query.filter_by(key=key).first()
        if db_obj:
            self.id = db_obj.id
            self.key = db_obj.key
            self.val = db_obj.val
            self.val_s = db_obj.val_s

        else:

            db.session.add(self)

            self.val = 0
            self.val_s = ''

    def __repr__(self):
        return '<Stats %s / %r / %s >' % (self.key, self.val, self.val_s)

    def save(self):

        db_obj = Stats.query.filter_by(key=self.key).first()

        # update the existing db object
        if db_obj:

            db_obj.val = self.val
            db_obj.val_s = self.val_s

        # commit change and save the object
        db.session.commit()

        return self


# user connected
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
