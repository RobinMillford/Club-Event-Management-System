from flask import Flask, jsonify, request
from datetime import datetime, date, time
from werkzeug.utils import secure_filename
import os
import pyodbc
import json
import socket

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, time)):
            return obj.isoformat()
        return super().default(obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# Set up the database connection
server = ''
database = 'Clubdb1'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                       SERVER=' + server +'; \
                       DATABASE=' + database +';\
                       Trusted_Connection=yes;')


#Student Interface
# Define a route for getting all events
@app.route('/events')
def get_events():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Club_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Mail, Event_Phone_No, Event_Budget, Event_Ticket, Event_url, Event_Picture,Event_Details FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Club_Id': row[1],
            'Event_Name': row[2],
            'Event_Type': row[3],
            'Event_Day': row[4],
            'Event_Date': row[5],  # No need for strftime here
            'Event_Start_Time': row[6],
            'Event_End_Time': row[7],
            'Event_Venue': row[8],
            'Event_Mail': row[9],
            'Event_Phone_No': row[10],
            'Event_Budget': row[11],
            'Event_Ticket': row[12],
            'Event_url': row[13],
            'Event_Picture': row[14],
            'Event_Details': row[15]
        }
        events.append(event)
    return jsonify(events)

#Student Interface
#Home page and it's components
@app.route('/1.1')
def one_1():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Picture FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Type': row[2],
            'Event_Day': row[3],
            'Event_Date': row[4],
            'Event_Start_Time': row[5],
            'Event_End_Time': row[6],
            'Event_Venue': row[7],
            'Event_Picture': row[8]
        }
        events.append(event)
    return jsonify(events)

@app.route('/1.1/1.11')
def one_11():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Type, Event_Day, Event_Date FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Type': row[0],
            'Event_Day': row[1],
            'Event_Date': row[2]
        }
        events.append(event)
    return jsonify(events)

@app.route('/1.1/1.11/1.12')
def one_12():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Name': row[0],
            'Event_Type': row[1],
            'Event_Day': row[2],
            'Event_Date': row[3],
            'Event_Start_Time': row[4],
            'Event_End_Time': row[5],
            'Event_Venue': row[6]
        }
        events.append(event)
    return jsonify(events)

@app.route('/1.1/1.11/1.12/1.13')
def one_13():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Mail, Event_Phone_No, Event_Budget, Event_Ticket, Event_url, Event_Picture FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Type': row[2],
            'Event_Day': row[3],
            'Event_Date': row[4],
            'Event_Start_Time': row[5],
            'Event_End_Time': row[6],
            'Event_Venue': row[7],
            'Event_Mail': row[8],
            'Event_Phone_No': row[9],
            'Event_Budget': row[10],
            'Event_Ticket': row[11],
            'Event_url': row[12],
            'Event_Picture': row[13]
        }
        events.append(event)
    return jsonify(events)

@app.route('/1.1/1.11/1.12/1.13/1.14')
def one_14():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Picture FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Type': row[2],
            'Event_Day': row[3],
            'Event_Date': row[4],
            'Event_Start_Time': row[5],
            'Event_End_Time': row[6],
            'Event_Venue': row[7],
            'Event_Picture': row[8]
        }
        events.append(event)
    return jsonify(events)

#clubs page and its redirects
@app.route('/1.2')
def one_2():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Club_name, Club_Picture, Club_Id, Club_Type FROM Clubs")
    rows = cursor.fetchall()
    clubs = []
    for row in rows:
        club = {
            'Club_Picture': row[0],
            'Club_Id': row[1],
            'Club_Type': row[2],
            'Club_Name': row[1]
        }
        clubs.append(club)
    return jsonify(clubs)

@app.route('/1.2/1.21')
def one_21():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Club_name, Club_Picture, Club_Id, Club_Type FROM Clubs")
    rows = cursor.fetchall()
    clubs = []
    for row in rows:
        club = {
            'Club_Name': row[0],
            'Club_Picture': row[1],
            'Club_Id': row[2],
            'Club_Type': row[3]
        }
        clubs.append(club)
    return jsonify(clubs)

@app.route('/1.2/1.22')
def one_22():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Club_Id, Club_Name, Club_Type, Club_Faculty_Cordinator_Name, Club_Mail, Club_Activity, Club_Total_Events, Club_Details, Club_Photos_Viwer, Club_Picture FROM Clubs")
    rows = cursor.fetchall()
    clubs = []
    for row in rows:
        club = {
            'Club_Id': row[0],
            'Club_Name': row[1],
            'Club_Type': row[2],
            'Club_Faculty_Cordinator_Name': row[3],
            'Club_Mail': row[4],
            'Club_Activity': row[5],
            'Club_Total_Events': row[6],
            'Club_Details': row[7],
            'Club_Photos_Viwer': row[8],
            'Club_Picture': row[9]
        }
        clubs.append(club)
    return jsonify(clubs)

from flask import jsonify

@app.route('/1.2/1.23')
def one_23():
    cursor = cnxn.cursor()
    cursor.execute("SELECT e.Event_Id, e.Event_Name, e.Event_Type, e.Event_Day, e.Event_Date, e.Event_Start_Time, e.Event_End_Time, e.Event_Venue, e.Event_Picture, e.Club_Id, c.Club_Name FROM Events e INNER JOIN Clubs c ON e.Club_Id = c.Club_Id")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Type': row[2],
            'Event_Day': row[3],
            'Event_Date': row[4],
            'Event_Start_Time': row[5],
            'Event_End_Time': row[6],
            'Event_Venue': row[7],
            'Event_Picture': row[8],
            'Club_Id': row[9],
            'Club_Name': row[10]
        }
        events.append(event)
    return jsonify(events)

from flask import jsonify

@app.route('/1.3')
def one_3():
    cursor = cnxn.cursor()
    cursor.execute("SELECT e.Event_Name, e.Club_Id, c.Club_Picture, e.Event_Date, e.Event_Day, e.Event_Start_Time FROM Events e INNER JOIN Clubs c ON e.Club_Id = c.Club_Id")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        event = {
            'Event_Name': row[0],
            'Club_Id': row[1],
            'Club_Picture': row[2],
            'Event_Date': row[3],
            'Event_Day': row[4],
            'Event_Start_Time': row[5]
        }
        data.append(event)
    
    return jsonify(data)

@app.route('/1.3/1.31')
def one_31():
    cursor = cnxn.cursor()
    cursor.execute("SELECT e.Event_Name, e.Club_Id, c.Club_Picture, e.Event_Date, e.Event_Day, e.Event_Start_Time FROM Events e INNER JOIN Clubs c ON e.Club_Id = c.Club_Id")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        event = {
            'Event_Name': row[0],
            'Club_Id': row[1],
            'Club_Picture': row[2],
            'Event_Date': row[3],
            'Event_Day': row[4],
            'Event_Start_Time': row[5]
        }
        data.append(event)
    
    return jsonify(data)

@app.route('/1.4')
def one_4():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Event_Name, Event_Picture FROM Events")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Picture': row[2]
        }
        data.append(event)
    
    return jsonify(data)


@app.route('/101')
def one_01():
    cursor = cnxn.cursor()
    cursor.execute("SELECT User_Student_Name, User_Student_Id, User_Student_Type, User_Student_Club_Id FROM User_Student")
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = {
            'User_Student_Name': row[0],
            'User_Student_Id': row[1],
            'User_Student_Type': row[2],
            'User_Student_Club_Id': row[3]
        }
        users.append(user)
    return jsonify(users)

#Student WELFARE INTERFACE
cursor = cnxn.cursor()

# Event approval: Get approved events, pending events, and past events
@app.route('/2.1/event-approval', methods=['GET'])
def event_approval():
    try:
        current_date = datetime.now().date()

        # Retrieve approved events
        cursor.execute("SELECT * FROM Events WHERE Event_Status = 'APPROVED'")
        approved_events = cursor.fetchall()

        # Retrieve pending events
        cursor.execute("SELECT * FROM Events WHERE Event_Status = 'Pending'")
        pending_events = cursor.fetchall()

        # Retrieve past events
        cursor.execute(f"SELECT * FROM Events WHERE Event_Date < '{current_date}'")
        past_events = cursor.fetchall()

        # Retrieve column names from cursor description
        column_names = [column[0] for column in cursor.description]

        # Convert rows to dictionaries
        approved_events = [dict(zip(column_names, row)) for row in approved_events]
        pending_events = [dict(zip(column_names, row)) for row in pending_events]
        past_events = [dict(zip(column_names, row)) for row in past_events]

        result = {
            'approved_events': approved_events,
            'pending_events': pending_events,
            'past_events': past_events
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Event report: Get approved and done events after the event date
@app.route('/2.1/event-report', methods=['GET'])
def event_report():
    try:
        current_date = datetime.now().date()

        # Retrieve approved and done events after the event date
        cursor.execute(f"SELECT * FROM Events WHERE Event_Status = 'Pending' AND Event_Date < '{current_date}'")
        events = cursor.fetchall()

        return jsonify({'events': events})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/2.1/new-event', methods=['POST'])
def upload_event():
    event_data = request.json

    try:
        # Insert the event data into the Events table
        cursor.execute("""
            INSERT INTO Events (Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_Picture, Event_Phone_No, Event_Mail,
            Event_End_Time, Event_Venue, Events_Ticket, Event_url, Event_Details, Event_Status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event_data['Event_Id'],
            event_data['Event_Name'],
            event_data['Event_Type'],
            event_data['Event_Day'],
            event_data['Event_Date'],
            event_data['Event_Start_Time'],
            event_data['Event_End_Time'],
            event_data['Event_Venue'],
            event_data['Events_Ticket'],
            event_data['Event_url'],
            event_data['Event_Details'],
            event_data['Event_Picture'],
            event_data['Event_Phone_No'],
            event_data['Event_Mail'],
            'Pending'  # Set the initial status to 'Pending'
        ))
        cnxn.commit()

        return jsonify({'message': 'Event uploaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Event data: Get total events by each club approved by month, year, and date
@app.route('/2.1/event-data', methods=['GET'])
def event_data():
    try:
        # Retrieve total events by each club approved by month, year, and date
        cursor.execute("""
            SELECT Club_Name, MONTH(Event_Date) AS Month, YEAR(Event_Date) AS Year, 
            DAY(Event_Date) AS Day, COUNT(*) AS Total_Events
            FROM Events
            JOIN Clubs ON Events.Club_Id = Clubs.Club_Id
            WHERE Event_Status = 'Approved'
            GROUP BY Club_Name, MONTH(Event_Date), YEAR(Event_Date), DAY(Event_Date)
        """)
        event_data = cursor.fetchall()

        return jsonify({'event_data': event_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/2.51', methods=['GET'])
def event_report_two_51():
    try:
        current_date = datetime.now().date()

        # Retrieve approved and done events after the event date
        cursor.execute(f"SELECT * FROM Events WHERE Event_Status = 'Pending' AND Event_Date < '{current_date}'")
        events = cursor.fetchall()

        return jsonify({'events': events})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/2.51/2.52/Pending', methods=['GET'])
def event_report_two_52():
    try:
        current_date = datetime.now().date()

        # Retrieve approved and done events after the event date
        cursor.execute(f"SELECT * FROM Events WHERE Event_Status = 'Pending'")
        events = cursor.fetchall()

        return jsonify({'events': events})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/2.51/2.52/Past', methods=['GET'])
def event_report_two_52_p():
    try:
        current_date = datetime.now().date()

        # Retrieve approved and done events after the event date
        cursor.execute(f"SELECT * FROM Events WHERE Event_Status = 'Pending' AND Event_Date < '{current_date}'")
        events = cursor.fetchall()

        return jsonify({'events': events})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/2.53/<int:event_id>', methods=['GET'])
def get_event_details(event_id):
    try:
        # Fetch event details from the database
        cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Ticket, Event_URL, Event_Details, Event_Status, Event_Picture, Event_Phone_No, Event_Mail FROM Events WHERE Event_Id = ?", (event_id,))
        row = cursor.fetchone()

        if row:
            # Extract event details from the fetched row
            event = {
                'Event_Id': row[0],
                'Event_Name': row[1],
                'Event_Type': row[2],
                'Event_Day': row[3],
                'Event_Date': row[4],
                'Event_Start_Time': row[5],
                'Event_End_Time': row[6],
                'Event_Venue': row[7],
                'Event_Ticket': row[8],
                'Event_URL': row[9],
                'Event_Details': row[10],
                'Event_Status': row[11],
                'Event_Picture': row[12],
                'Event_Phone_No': row[13],
                'Event_Mail': row[14]
            }

            return jsonify(event)
        else:
            return jsonify({'error': 'Event not found'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/102')
def one_02():
    cursor = cnxn.cursor()
    cursor.execute("SELECT User_Student_Welfare_Name, User_Student_Welfare_Id, User_Student_Welfare_Type, User_Student_Welfare_Club_Id FROM User_Student_Welfare")
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = {
            'User_Student_Welfare_Name': row[0],
            'User_Student_Welfare_Id': row[1],
            'User_Student_Welfare_Type': row[2],
            'User_Student_Welfare_Club_Id': row[3]
        }
        users.append(user)
    return jsonify(users)

@app.route('/104')
def one_04():
    cursor = cnxn.cursor()
    cursor.execute("""
        SELECT usw.User_Student_Welfare_Name, usw.User_Student_Welfare_Id, usw.User_Student_Welfare_Type, usw.User_Student_Welfare_Office, usw.User_Student_Welfare_Club_Id, c.Club_Name
        FROM User_Student_Welfare usw
        JOIN Clubs c ON usw.User_Student_Welfare_Club_Id = c.Club_Id
    """)
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = {
            'User_Student_Welfare_Name': row[0],
            'User_Student_Welfare_Id': row[1],
            'User_Student_Welfare_Type': row[2],
            'User_Student_Welfare_Office': row[3],
            'User_Student_Welfare_Club_Id': row[4],
            'Club_Name': row[5]
        }
        users.append(user)
    return jsonify(users)

@app.route('/2.91')
def two_91():
    cursor = cnxn.cursor()
    cursor.execute("SELECT e.Event_Name, e.Club_Id, c.Club_Picture, e.Event_Date, e.Event_Day, e.Event_Start_Time FROM Events e INNER JOIN Clubs c ON e.Club_Id = c.Club_Id")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        event = {
            'Event_Name': row[0],
            'Club_Id': row[1],
            'Club_Picture': row[2],
            'Event_Date': row[3],
            'Event_Day': row[4],
            'Event_Start_Time': row[5]
        }
        data.append(event)
    
    return jsonify(data)

@app.route('/2.91/2.92')
def two_92():
    cursor = cnxn.cursor()
    cursor.execute("SELECT e.Event_Name, e.Club_Id, c.Club_Picture, e.Event_Date, e.Event_Day, e.Event_Start_Time FROM Events e INNER JOIN Clubs c ON e.Club_Id = c.Club_Id")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        event = {
            'Event_Name': row[0],
            'Club_Id': row[1],
            'Club_Picture': row[2],
            'Event_Date': row[3],
            'Event_Day': row[4],
            'Event_Start_Time': row[5]
        }
        data.append(event)
    
    return jsonify(data)

@app.route('/2.71')
def two_71():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Picture FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Type': row[2],
            'Event_Day': row[3],
            'Event_Date': row[4],
            'Event_Start_Time': row[5],
            'Event_End_Time': row[6],
            'Event_Venue': row[7],
            'Event_Picture': row[8]
        }
        events.append(event)
    return jsonify(events)

@app.route('/2.71/2.72')
def two_72():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Type, Event_Day, Event_Date FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Type': row[0],
            'Event_Day': row[1],
            'Event_Date': row[2]
        }
        events.append(event)
    return jsonify(events)


@app.route('/2.71/2.72/2.73')
def two_73():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Mail, Event_Phone_No, Event_Budget, Event_Ticket, Event_url, Event_Picture FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Type': row[2],
            'Event_Day': row[3],
            'Event_Date': row[4],
            'Event_Start_Time': row[5],
            'Event_End_Time': row[6],
            'Event_Venue': row[7],
            'Event_Mail': row[8],
            'Event_Phone_No': row[9],
            'Event_Budget': row[10],
            'Event_Ticket': row[11],
            'Event_url': row[12],
            'Event_Picture': row[13]
        }
        events.append(event)
    return jsonify(events)

@app.route('/2.71/2.72/2.73/2.74')
def two_74():
    cursor = cnxn.cursor()
    cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Picture FROM Events")
    rows = cursor.fetchall()
    events = []
    for row in rows:
        event = {
            'Event_Id': row[0],
            'Event_Name': row[1],
            'Event_Type': row[2],
            'Event_Day': row[3],
            'Event_Date': row[4],
            'Event_Start_Time': row[5],
            'Event_End_Time': row[6],
            'Event_Venue': row[7],
            'Event_Picture': row[8]
        }
        events.append(event)
    return jsonify(events)

#Faculty co-ordinator interface
@app.route('/3.61')
def three_61():
    cursor = cnxn.cursor()
    cursor.execute("SELECT e.Event_Name, e.Club_Id, c.Club_Picture, e.Event_Date, e.Event_Day, e.Event_Start_Time FROM Events e INNER JOIN Clubs c ON e.Club_Id = c.Club_Id")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        event = {
            'Event_Name': row[0],
            'Club_Id': row[1],
            'Club_Picture': row[2],
            'Event_Date': row[3],
            'Event_Day': row[4],
            'Event_Start_Time': row[5]
        }
        data.append(event)
    
    return jsonify(data)

@app.route('/3.61/3.62')
def three_62():
    cursor = cnxn.cursor()
    cursor.execute("""
        SELECT e.Event_Name, e.Club_Id, c.Club_Picture, e.Event_Date, e.Event_Day, e.Event_Start_Time, e.Event_Status
        FROM Events e
        INNER JOIN Clubs c ON e.Club_Id = c.Club_Id
    """)
    rows = cursor.fetchall()
    data = []
    for row in rows:
        event = {
            'Event_Name': row[0],
            'Club_Id': row[1],
            'Club_Picture': row[2],
            'Event_Date': row[3],
            'Event_Day': row[4],
            'Event_Start_Time': row[5],
            'Event_Status': row[6]
        }
        data.append(event)

    return jsonify(data)

@app.route('/103')
def one_03():
    cursor = cnxn.cursor()
    cursor.execute("""
        SELECT c.Club_Name, c.Club_Type, c.Club_Faculty_Cordinator_Name
        FROM Clubs c
    """)
    rows = cursor.fetchall()
    clubs = []
    for row in rows:
        club = {
            'Club_Name': row[0],
            'Club_Type': row[1],
            'Club_Faculty_Cordinator_Name': row[2]
        }
        clubs.append(club)
    return jsonify(clubs)

@app.route('/3.4', methods=['GET', 'PUT'])
def clubs():
    if request.method == 'GET':
        try:
            cursor.execute("""
                SELECT Club_Id, Club_Name, Club_Type, Club_Faculty_Cordinator_Name, Club_Mail,
                Club_Activity, Club_Total_Events, Club_Details, Club_Photos_Viwer, Club_Picture
                FROM Clubs
            """)
            rows = cursor.fetchall()
            clubs = []
            for row in rows:
                club = {
                    'Club_Id': row[0],
                    'Club_Name': row[1],
                    'Club_Type': row[2],
                    'Club_Faculty_Cordinator_Name': row[3],
                    'Club_Mail': row[4],
                    'Club_Activity': row[5],
                    'Club_Total_Events': row[6],
                    'Club_Details': row[7],
                    'Club_Photos_Viwer': row[8],
                    'Club_Picture': row[9]
                }
                clubs.append(club)
            return jsonify(clubs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    elif request.method == 'PUT':
        try:
            club_data = request.json
            club_id = club_data['Club_Id']
            
            # Update club details in the database
            cursor.execute("""
                UPDATE Clubs
                SET Club_Name = ?, Club_Type = ?, Club_Faculty_Cordinator_Name = ?, Club_Mail = ?,
                Club_Activity = ?, Club_Total_Events = ?, Club_Details = ?, Club_Photos_Viwer = ?, Club_Picture = ?
                WHERE Club_Id = ?
            """, (
                club_data['Club_Name'],
                club_data['Club_Type'],
                club_data['Club_Faculty_Cordinator_Name'],
                club_data['Club_Mail'],
                club_data['Club_Activity'],
                club_data['Club_Total_Events'],
                club_data['Club_Details'],
                club_data['Club_Photos_Viwer'],
                club_data['Club_Picture'],
                club_id
            ))
            cnxn.commit()
            
            return jsonify({'message': 'Club details updated successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Event report: Get approved and done events after the event date
@app.route('/3.1/event-report', methods=['GET'])
def event_report_31():
    try:
        current_date = datetime.now().date()

        # Retrieve approved and done events after the event date
        cursor.execute(f"SELECT * FROM Events WHERE Event_Status = 'Pending' AND Event_Date < '{current_date}'")
        events = cursor.fetchall()

        return jsonify({'events': events})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
# Directory to store uploaded event pictures
UPLOAD_FOLDER = 'event_pictures'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/3.21/3.22/clubs/<int:club_id>/events', methods=['GET', 'PUT'])
@app.route('/3.21/3.22/clubs/<int:club_id>/events/<int:event_id>/picture', methods=['GET'])
def club_events(club_id, event_id=None):
    if request.method == 'GET':
        if event_id is None:
            # Fetch all events for the given club_id
            cursor.execute("SELECT * FROM Events WHERE Club_Id = ?", (club_id,))
            rows = cursor.fetchall()
            events = []
            for row in rows:
                event = {
                    'Event_Id': row[0],
                    'Event_Name': row[1],
                    'Event_Type': row[2],
                    'Event_Date': row[3],
                    'Club_Id': row[4]
                }
                events.append(event)
            return jsonify(events)
        else:
            # Fetch the event picture for the given club_id and event_id
            cursor.execute("SELECT Event_Picture FROM Events WHERE Club_Id = ? AND Event_Id = ?", (club_id, event_id))
            row = cursor.fetchone()
            if row:
                event_picture = row[0]
                # You can implement code here to download and view the event picture
                # For example, return a response with the image file
                return send_file(event_picture, mimetype='image/jpeg')
            else:
                return jsonify({'error': 'Event not found'})
    elif request.method == 'PUT':
        # Handle the modification of event details (PUT request)
        # Extract the updated event details from the request JSON data
        updated_event_details = request.json

        # Update the event details in the database for the given club_id and event_id
        cursor.execute("""
            UPDATE Events
            SET Event_Name = ?,
                Event_Type = ?,
                Event_Date = ?
            WHERE Club_Id = ? AND Event_Id = ?
        """, (
            updated_event_details['Event_Name'],
            updated_event_details['Event_Type'],
            updated_event_details['Event_Date'],
            club_id,
            event_id
        ))
        cnxn.commit()

        return jsonify({'message': 'Event details updated successfully'})
    
@app.route('/3.31/3.33/<int:event_id>', methods=['GET'])
def get_event_details_A(event_id):
    try:
        # Fetch event details from the database based on event_id and approval status
        cursor.execute("SELECT * FROM Events WHERE Event_Id = ? AND Event_Status IN ('Approved')", (event_id,))
        row = cursor.fetchone()

        if row:
            # Extract event details from the fetched row
            event = {
                'Event_Id': row[0],
                'Event_Name': row[1],
                'Event_Type': row[2],
                'Event_Day': row[3],
                'Event_Date': row[4],
                'Event_Start_Time': row[5],
                'Event_End_Time': row[6],
                'Event_Venue': row[7],
                'Event_Ticket': row[8],
                'Event_URL': row[9],
                'Event_Details': row[10],
                'Event_Status': row[11],
                'Event_Picture': row[12],
                'Event_Phone_No': row[13],
                'Event_Mail': row[14]
            }

            return jsonify(event)
        else:
            return jsonify({'error': 'Event not found or not approved/denied/pending'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/3.31/3.34/<int:event_id>', methods=['GET'])
def get_event_details_D(event_id):
    try:
        # Fetch event details from the database based on event_id and approval status
        cursor.execute("SELECT * FROM Events WHERE Event_Id = ? AND Event_Status IN ('Denied')", (event_id,))
        row = cursor.fetchone()

        if row:
            # Extract event details from the fetched row
            event = {
                'Event_Id': row[0],
                'Event_Name': row[1],
                'Event_Type': row[2],
                'Event_Day': row[3],
                'Event_Date': row[4],
                'Event_Start_Time': row[5],
                'Event_End_Time': row[6],
                'Event_Venue': row[7],
                'Event_Ticket': row[8],
                'Event_URL': row[9],
                'Event_Details': row[10],
                'Event_Status': row[11],
                'Event_Picture': row[12],
                'Event_Phone_No': row[13],
                'Event_Mail': row[14]
            }

            return jsonify(event)
        else:
            return jsonify({'error': 'Event not found or not approved/denied/pending'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/3.31/3.33.225/<int:event_id>', methods=['GET'])
def get_event_details_P(event_id):
    try:
        # Fetch event details from the database based on event_id and approval status
        cursor.execute("SELECT * FROM Events WHERE Event_Id = ? AND Event_Status IN ('Pending')", (event_id,))
        row = cursor.fetchone()

        if row:
            # Extract event details from the fetched row
            event = {
                'Event_Id': row[0],
                'Event_Name': row[1],
                'Event_Type': row[2],
                'Event_Day': row[3],
                'Event_Date': row[4],
                'Event_Start_Time': row[5],
                'Event_End_Time': row[6],
                'Event_Venue': row[7],
                'Event_Ticket': row[8],
                'Event_URL': row[9],
                'Event_Details': row[10],
                'Event_Status': row[11],
                'Event_Picture': row[12],
                'Event_Phone_No': row[13],
                'Event_Mail': row[14]
            }

            return jsonify(event)
        else:
            return jsonify({'error': 'Event not found or not approved/denied/pending'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# New event: Upload event data
@app.route('/3.31/3.32', methods=['POST'])
def Event_approval():
    event_data = request.json

    try:
        # Insert the event data into the Events table
        cursor.execute("""
            INSERT INTO Events (Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_Picture, Event_Phone_No, Event_Mail,
            Event_End_Time, Event_Venue, Events_Ticket, Event_url, Event_Details, Event_Status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            event_data['Event_Id'],
            event_data['Event_Name'],
            event_data['Event_Type'],
            event_data['Event_Day'],
            event_data['Event_Date'],
            event_data['Event_Start_Time'],
            event_data['Event_End_Time'],
            event_data['Event_Venue'],
            event_data['Events_Ticket'],
            event_data['Event_url'],
            event_data['Event_Details'],
            event_data['Event_Picture'],
            event_data['Event_Phone_No'],
            event_data['Event_Mail'],
            'Pending'  # Set the initial status to 'Pending'
        ))
        cnxn.commit()

        return jsonify({'message': 'Event uploaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/3.31')
def get_events_3():
    try:
        current_date = datetime.now().date()

        # Fetch events based on status and date
        cursor.execute("SELECT Event_Id, Event_Name, Event_Type, Event_Day, Event_Date, Event_Start_Time, Event_End_Time, Event_Venue, Event_Ticket, Event_URL, Event_Details, Event_Status, Event_Picture, Event_Phone_No, Event_Mail FROM Events WHERE Event_Date >= ? AND Event_Status IN ('Denied', 'Pending', 'Approved')", (current_date,))
        rows = cursor.fetchall()

        events = []
        for row in rows:
            event = {
                'Event_Id': row[0],
                'Event_Name': row[1],
                'Event_Type': row[2],
                'Event_Day': row[3],
                'Event_Date': row[4],
                'Event_Start_Time': row[5],
                'Event_End_Time': row[6],
                'Event_Venue': row[7],
                'Event_Ticket': row[8],
                'Event_URL': row[9],
                'Event_Details': row[10],
                'Event_Status': row[11],
                'Event_Picture': row[12],
                'Event_Phone_No': row[13],
                'Event_Mail': row[14]
            }
            events.append(event)

        return jsonify(events)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/3.31/move_to_past_events', methods=['POST'])
def move_to_past_events():
    try:
        current_date = datetime.now().date()

        # Move events with the event date in the past to "Past Events"
        cursor.execute("UPDATE Events SET Event_Status = 'Past Events' WHERE Event_Date < ?", (current_date,))
        cnxn.commit()

        return jsonify({'message': 'Events moved to Past Events successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# # Define a route for getting all clubs
# @app.route('/clubs')
# def get_clubs():
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT * FROM Clubs")
#     rows = cursor.fetchall()
#     clubs = []
#     for row in rows:
#         club = {
#         'Club_Id': row[0],
#         'Club_Name': row[1],
#         'Club_Type': row[2],
#         'Club_Faculty_Cordinator_Name': row[3],
#         'Club_Mail': row[4],
#         'Club_Activity': row[5],
#         'Club_Total_Events': row[6],
#         'Club_Details': row[7],
#         'Club_Photos_Viwer': row[8],
#         'Club_Picture': row[9]
#         }
#         clubs.append(club)
#     return jsonify(clubs)

# # Define a route for getting all user students
# @app.route('/user_students')
# def get_user_students():
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT * FROM User_Student")
#     rows = cursor.fetchall()
#     user_students = []
#     for row in rows:
#         user_student = {
#         'User_Student_Name': row[0],
#         'User_Student_Id': row[1],
#         'User_Student_Type': row[2],
#         'User_Student_Club_Id': row[3]
#         }
#         user_students.append(user_student)
#     return jsonify(user_students)

# # Define a route for getting all user faculty
# @app.route('/user_faculty')
# def get_user_faculty():
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT * FROM User_Faculty")
#     rows = cursor.fetchall()
#     user_faculty = []
#     for row in rows:
#         user = {
#         'User_Faculty_Name': row[0],
#         'User_Faculty_Id': row[1],
#         'User_Faculty_Type': row[2],
#         'User_Faculty_Club_Id': row[3]
#         }
#         user_faculty.append(user)
#     return jsonify(user_faculty)

# # Define a route for getting all user student welfare
# @app.route('/user_student_welfare')
# def get_user_student_welfare():
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT * FROM User_Student_Welfare")
#     rows = cursor.fetchall()
#     user_student_welfare = []
#     for row in rows:
#         user = {
#         'User_Student_Welfare_Name': row[0],
#         'User_Student_Welfare_Id': row[1],
#         'User_Student_Welfare_Type': row[2],
#         'User_Student_Welfare_Club_Id': row[3]
#         }
#         user_student_welfare.append(user)
#     return jsonify(user_student_welfare)

def get_local_ip():
    try:
        # Create a temporary socket to get the local IP address
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))  # Connect to a known external IP address
        local_ip = temp_socket.getsockname()[0]  # Get the local IP address
        temp_socket.close()  # Close the temporary socket
        return local_ip
    except socket.error:
        return None

# Get the local IP address
local_ip = get_local_ip()
print(local_ip)

# Run the Flask application
if __name__ == '__main__':
    app.run(host=local_ip, port=5000)