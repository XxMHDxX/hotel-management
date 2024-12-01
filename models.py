# models.py
from extensions import db

# Modèle pour la table 'type_hotel'
class TypeHotel(db.Model):
    __tablename__ = 'type_hotel'
    ID_type_hotel = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_hotel = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<TypeHotel {self.type_hotel}>"

# Modèle pour la table 'type_chambre'
class TypeChambre(db.Model):
    __tablename__ = 'type_chambre'
    ID_type_chambre = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_chambre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<TypeChambre {self.type_chambre}>"

# Modèle pour la table 'type_client'
class TypeClient(db.Model):
    __tablename__ = 'type_client'
    ID_type_client = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_client = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<TypeClient {self.type_client}>"

# Modèle pour la table 'hotel'
class Hotel(db.Model):
    __tablename__ = 'hotel'
    ID_hotel = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_hotel = db.Column(db.String(100), nullable=False)
    ID_type_hotel = db.Column(db.Integer, db.ForeignKey('type_hotel.ID_type_hotel'), nullable=False)
    
    # Relation avec la table 'type_hotel'
    type_hotel = db.relationship('TypeHotel', backref='hotels')

    def __repr__(self):
        return f"<Hotel {self.nom_hotel}>"

# Modèle pour la table 'chambre'
class Chambre(db.Model):
    __tablename__ = 'chambre'
    ID_chambre = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_chambre = db.Column(db.String(100), nullable=False)
    ID_type_chambre = db.Column(db.Integer, db.ForeignKey('type_chambre.ID_type_chambre'), nullable=False)
    ID_hotel = db.Column(db.Integer, db.ForeignKey('hotel.ID_hotel'), nullable=False)

    # Relations
    type_chambre = db.relationship('TypeChambre', backref='chambres')
    hotel = db.relationship('Hotel', backref='chambres')

    def __repr__(self):
        return f"<Chambre {self.nom_chambre}>"

# Modèle pour la table 'client'
class Client(db.Model):
    __tablename__ = 'client'
    
    ID_client = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.String(100), nullable=False)
    prenom_client = db.Column(db.String(100), nullable=False)
    ID_type_client = db.Column(db.Integer, db.ForeignKey('type_client.ID_type_client'), nullable=False)
    email = db.Column(db.String(100), nullable=True)  # Autoriser NULL ici

    # Relation avec 'type_client'
    type_client = db.relationship('TypeClient', backref='clients')

    def __repr__(self):
        return f"<Client {self.nom_client} {self.prenom_client}>"

# Modèle pour la table 'reservation'
class Reservation(db.Model):
    __tablename__ = 'reservation'
    ID_reservation = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_debut = db.Column(db.DateTime, nullable=False)
    date_fin = db.Column(db.DateTime, nullable=False)
    ID_client = db.Column(db.Integer, db.ForeignKey('client.ID_client'), nullable=False)
    ID_chambre = db.Column(db.Integer, db.ForeignKey('chambre.ID_chambre'), nullable=False)

    # Relations
    client = db.relationship('Client', backref='reservations')
    chambre = db.relationship('Chambre', backref='reservations')

    def __repr__(self):
        return f"<Reservation {self.ID_reservation}>"
