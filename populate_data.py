from app import db
from models import TypeHotel, TypeChambre, TypeClient, Hotel, Chambre, Client, Reservation
from datetime import datetime
from app import app  # Importer l'application Flask pour gérer le contexte

# Démarrer le contexte d'application
with app.app_context():
    # Ajout des types d'hôtel
    type_hotels = [
        TypeHotel(ID_type_hotel=1, type_hotel="2 Etoile"),
        TypeHotel(ID_type_hotel=2, type_hotel="3 Etoile"),
        TypeHotel(ID_type_hotel=3, type_hotel="4 Etoile")
    ]
    db.session.bulk_save_objects(type_hotels)

    # Ajout des types de chambre
    type_chambres = [
        TypeChambre(ID_type_chambre=1, type_chambre="Simple"),
        TypeChambre(ID_type_chambre=2, type_chambre="Double"),
        TypeChambre(ID_type_chambre=3, type_chambre="VIP")
    ]
    db.session.bulk_save_objects(type_chambres)

    # Ajout des types de client
    type_clients = [
        TypeClient(ID_type_client=1, type_client="Personne"),
        TypeClient(ID_type_client=2, type_client="Societe")
    ]
    db.session.bulk_save_objects(type_clients)

    # Ajout des hôtels
    hotels = [
        Hotel(ID_hotel=1, nom_hotel="DAR DIAF", ID_type_hotel=1),
        Hotel(ID_hotel=2, nom_hotel="Best Night", ID_type_hotel=2),
        Hotel(ID_hotel=3, nom_hotel="Sidi Yahia", ID_type_hotel=3)
    ]
    db.session.bulk_save_objects(hotels)

    # Ajout des chambres
    chambres = [
        Chambre(ID_chambre=1, nom_chambre="DAR_DIAF_1", ID_hotel=1, ID_type_chambre=1),
        Chambre(ID_chambre=2, nom_chambre="DAR_DIAF_2", ID_hotel=1, ID_type_chambre=1),
        Chambre(ID_chambre=3, nom_chambre="DAR_DIAF_3", ID_hotel=1, ID_type_chambre=2),
        Chambre(ID_chambre=4, nom_chambre="DAR_DIAF_4", ID_hotel=1, ID_type_chambre=3),
        Chambre(ID_chambre=5, nom_chambre="Best_Night_1", ID_hotel=2, ID_type_chambre=1),
        Chambre(ID_chambre=6, nom_chambre="Best_Night_2", ID_hotel=2, ID_type_chambre=1),
        Chambre(ID_chambre=7, nom_chambre="Best_Night_3", ID_hotel=2, ID_type_chambre=2),
        Chambre(ID_chambre=8, nom_chambre="Best_Night_4", ID_hotel=2, ID_type_chambre=3),
        Chambre(ID_chambre=9, nom_chambre="Sidi_Yahia_1", ID_hotel=3, ID_type_chambre=1),
        Chambre(ID_chambre=10, nom_chambre="Sidi_Yahia_2", ID_hotel=3, ID_type_chambre=1),
        Chambre(ID_chambre=11, nom_chambre="Sidi_Yahia_3", ID_hotel=3, ID_type_chambre=2),
        Chambre(ID_chambre=12, nom_chambre="Sidi_Yahia_4", ID_hotel=3, ID_type_chambre=3)
    ]
    db.session.bulk_save_objects(chambres)

    # Ajout des clients
    clients = [
    Client(ID_client=1, nom_client="Ouldaouali", prenom_client="Mehdi", ID_type_client=2, email="mehdi@exemple.com"),
    Client(ID_client=2, nom_client="Hedli", prenom_client="Ayoub", ID_type_client=1, email="ayoub@exemple.com"),
    Client(ID_client=3, nom_client="Zouggari", prenom_client="Wahab", ID_type_client=1, email="wahab@exemple.com"),
    Client(ID_client=4, nom_client="Berghiche", prenom_client="Yazid", ID_type_client=1, email="yazid@exemple.com"),
    Client(ID_client=5, nom_client="Smahi", prenom_client="Rayane", ID_type_client=2, email="rayane@exemple.com"),
    Client(ID_client=6, nom_client="Gaba", prenom_client="Borhane", ID_type_client=2, email="borhane@exemple.com")
    ]


    
    db.session.bulk_save_objects(clients)

    # Ajout des réservations
    reservations = [
        Reservation(ID_reservation=1, ID_client=1, ID_chambre=1, date_debut=datetime(2024, 3, 5), date_fin=datetime(2024, 3, 8)),
        Reservation(ID_reservation=2, ID_client=1, ID_chambre=2, date_debut=datetime(2024, 3, 10), date_fin=datetime(2024, 3, 12)),
        Reservation(ID_reservation=3, ID_client=2, ID_chambre=3, date_debut=datetime(2024, 3, 15), date_fin=datetime(2024, 3, 20)),
        # Ajoutez d'autres réservations ici...
    ]
    db.session.bulk_save_objects(reservations)

    # Commit des données
    db.session.commit()

    print("Données ajoutées avec succès!")
