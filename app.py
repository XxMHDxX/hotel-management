from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import TypeHotel, TypeChambre, TypeClient, Hotel, Chambre, Client, Reservation
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    hotels = Hotel.query.all()
    return render_template('index.html', hotels=hotels)

@app.route('/rooms')
def rooms():
    rooms = Chambre.query.all()
    return render_template('rooms.html', rooms=rooms)

@app.route('/hotel_rooms/<int:hotel_id>')
def hotel_rooms(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)  # Récupère l'hôtel par son ID
    rooms = Chambre.query.filter_by(ID_hotel=hotel_id).all()  # Récupère les chambres de cet hôtel
    return render_template('hotel_rooms.html', hotel=hotel, rooms=rooms)

@app.route('/book/<int:room_id>', methods=['GET', 'POST'])
def book_room(room_id):
    room = Chambre.query.get_or_404(room_id)
    if request.method == 'POST':
        client_name = request.form['client_name']
        client_email = request.form['client_email']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')

        # Check room availability
        existing_reservations = Reservation.query.filter(
            Reservation.ID_chambre == room_id,
            Reservation.date_debut <= end_date,
            Reservation.date_fin >= start_date
        ).all()
        if existing_reservations:
            return render_template('book_room.html', room=room, error="Room is not available for the selected dates.")

        # Create or find client
        client = Client.query.filter_by(email=client_email).first()
        if not client:
            client = Client(nom_client=client_name, prenom_client="Unknown", email=client_email, ID_type_client=1)
            db.session.add(client)
            db.session.commit()

        # Create reservation
        reservation = Reservation(
            date_debut=start_date,
            date_fin=end_date,
            ID_client=client.ID_client,
            ID_chambre=room.ID_chambre
        )
        db.session.add(reservation)
        db.session.commit()

        return redirect(url_for('confirmation', reservation_id=reservation.ID_reservation))
    return render_template('book_room.html', room=room)

@app.route('/confirmation/<int:reservation_id>')
def confirmation(reservation_id):
    reservation = db.session.query(
        Reservation.date_debut,
        Reservation.date_fin,
        Client.nom_client,
        Client.email,
        Chambre.nom_chambre,
        Hotel.nom_hotel
    ).join(Client, Reservation.ID_client == Client.ID_client
    ).join(Chambre, Reservation.ID_chambre == Chambre.ID_chambre
    ).join(Hotel, Chambre.ID_hotel == Hotel.ID_hotel
    ).filter(Reservation.ID_reservation == reservation_id).first()

    if reservation:
        return render_template('confirmation.html', reservation=reservation)
    else:
        return "Reservation not found", 404


@app.route('/reservations')
def reservations():
    reservations = db.session.query(
        Reservation,
        Client.nom_client,
        Client.email,
        Chambre.nom_chambre,
        Hotel.nom_hotel
    ).join(Client, Reservation.ID_client == Client.ID_client
    ).join(Chambre, Reservation.ID_chambre == Chambre.ID_chambre
    ).join(Hotel, Chambre.ID_hotel == Hotel.ID_hotel
    ).all()

    return render_template('reservations.html', reservations=reservations)

if __name__ == "__main__":
    app.run(debug=True)
