from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, RadioField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime

import wtforms
import csv
import os
import uuid

# Define choices for gi and no-gi ranks
GI_RANK_CHOICES = [('White'), ('Blue'), ('Purple'), ('Brown'), ('Black')]
NO_GI_RANK_CHOICES = [('Beginner'), ('Intermediate'),  ('Advanced')]

# Create the Flask application
app = Flask(__name__, static_folder="static")

# Dictionary to store athlete data
athlete_data = {}

# Class to create instances of athlete data
class Athlete:
    def __init__(self, first_name, middle_name, last_name, dob, registration_type, gi_rank, no_gi_rank, gym, weight):
        self.uuid = str(uuid.uuid4())
        self.first_name = first_name.strip()
        self.middle_name = middle_name
        self.last_name = last_name.strip()
        self.dob = dob
        self.registration_type = registration_type
        self.gi_rank = gi_rank
        self.no_gi_rank = no_gi_rank
        self.gym = gym
        self.weight = weight

# Function to validate date format
def val_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to determine weight class
def determine_weight_class(weight):
    if weight <= 155:
        return 'Light'
    elif weight <= 205:
        return 'Middle'
    else:
        return 'Heavy'

# Route for the index page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Route for the registration page
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # Extract and validate form data
        first_name = request.form['first_name']
        middle_name = request.form.get('middle_name', '')
        last_name = request.form['last_name']
        dob = request.form['dob']
        registration_type = request.form['registration_type']
        gi_rank = request.form.get('gi_rank')
        no_gi_rank = request.form.get('no_gi_rank')
        gym = request.form['gym']
        weight = float(request.form['weight'])

        # Validate date format
        if not val_date(dob):
            # Handle invalid date format, possibly redirecting or showing an error message
            return "Invalid date format", 400

        # Determine weight class
        weight_class = determine_weight_class(weight)

        # Validate gi and no-gi rank
        if gi_rank not in [choice[0] for choice in GI_RANK_CHOICES]:
            return "Invalid gi rank", 400
        if no_gi_rank not in [choice[0] for choice in NO_GI_RANK_CHOICES]:
            return "Invalid no-gi rank", 400

        # Construct athlete key
        key = f"{last_name.lower()}_{first_name.lower()}_{middle_name.lower()}_{dob}"
        if key in athlete_data:
            athlete = athlete_data[key]
        else:
            # Create new athlete instance
            athlete = Athlete(first_name, middle_name, last_name, dob, gi_rank, no_gi_rank, gym, weight, registration_type)
            athlete_data[key] = athlete

        # Append athlete data to a CSV file
        # Ensure the CSV file handling logic is correct and csv_directory is defined
        athletes_csv_file = f'{athlete.registration_type}_athletes.csv'
        with open(athletes_csv_file, mode='a', newline='') as file:
            fieldnames = ['uuid', 'first_name', 'middle_name', 'last_name', 'dob', 'gi_rank', 'no_gi_rank', 'gym', 'weight', 'weight_class', 'registration_type']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                'uuid': athlete.uuid,
                'first_name': athlete.first_name,
                'middle_name': athlete.middle_name,
                'last_name': athlete.last_name,
                'dob': athlete.dob,
                'registration_type': athlete.registration_type,
                'gi_rank': athlete.gi_rank,
                'no_gi_rank': athlete.no_gi_rank,
                'gym': athlete.gym,
                'weight': athlete.weight,
                'weight_class': weight_class,
            })

        return redirect(url_for('index'))

    # Render the registration form
    return render_template('registration_form.html', athlete_data=athlete_data, gi_rank_choices=GI_RANK_CHOICES, no_gi_rank_choices=NO_GI_RANK_CHOICES, registration_type_choices=['Gi', 'No-Gi', 'Gi Absolute', 'No-Gi Absolute'])

if __name__ == '__main__':
    app.run(debug=True)