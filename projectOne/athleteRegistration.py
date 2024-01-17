                                                                                                              ###  Athlete registration and tracking

import csv
from datetime import datetime
import uuid


## FUNCTIONS

#check correct format for DOB input (YYYY-MM-DD)
def val_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# get athlete info
def get_athlete_info(existing_athletes):
    while True:
        try:
            first_name = input("Enter athlete's first name : ").strip()
            if ' ' in first_name:
                print("First name should not contain spaces. Please try again.")
                continue

            middle_name = input("Enter athlete's middle name : ")

            last_name = input("Enter athlete's last name : ").strip()
            if last_name.count(' ') > 2:
                print("Last name should not contain more than 2 spaces. Please try again.")
                continue

            while True:
                dob = input("Enter athlete's date of birth (YYYY-MM-DD): ")
                if val_date(dob):
                    break
                else:
                    print("Date of birth must be in YYYY-MM-DD format. Please try again.")
                    continue

            key = f"{last_name.lower()}_{first_name.lower()}_{middle_name.lower()}_{dob}"

            if key in existing_athletes:
                print("Athlete already registered. Using existing UUID.")
                uuid_str = existing_athletes[key]
            else:
                uuid_str = str(uuid.uuid4())
                existing_athletes[key] = uuid_str

            while True:
                registration_type = input("Register for gi, no-gi, or both? (gi/no-gi/both): ").lower()
                if registration_type in ['gi', 'no-gi', 'both']:
                    break
                else:
                    print("Invalid selection.")
                    continue

            gym = input("Enter athlete's gym: ")
            weight = float(input("Enter athlete's weight (lbs): "))

            gi_rank = no_gi_rank = None
            if registration_type in ['gi', 'both']:
                while True:
                    gi_rank = input("Enter gi rank (white/blue/purple/brown/black): ").lower()
                    if gi_rank in ['white', 'blue', 'purple', 'brown', 'black']:
                        break
                    else:
                        print("Invalid gi rank. Please enter 'white', 'blue', 'purple', 'brown', or 'black'.")
                if gi_rank == 'white':
                    no_gi_rank = 'beginner'
                elif gi_rank in ['blue', 'purple']:
                    no_gi_rank = 'intermediate'
                elif gi_rank in ['brown', 'black']:
                    no_gi_rank = 'advanced'

            if registration_type == 'no-gi':
                no_gi_rank = input("Enter no-gi rank (beginner/intermediate/advanced): ").lower()

            return {
                'uuid': uuid_str,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'dob': dob,
                'gi_rank': gi_rank,
                'no_gi_rank': no_gi_rank,
                'gym': gym,
                'weight': weight,
                'registration_type': registration_type
            }

        except ValueError:
            print("Invalid input, please try again.")

# determine weight class
def determine_weight_class(weight):
    if weight <= 155:
        return 'Light'
    elif weight <= 205:
        return 'Middle'
    else:
        return 'Heavy'

# loads existing athlete data from csv file into dictionary
def load_existing_athletes(filename):
    athletes = {}
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                middle_name = row['middle_name'].lower() if row['middle_name'] else ""
                key = f"{row['last_name'].lower()}_{row['first_name'].lower()}_{middle_name}_{row['dob']}"
                athletes[key] = row['uuid']
    except FileNotFoundError:
        pass
    return athletes


## MAIN
continue_registration = True  # Flag to control the main loop

while continue_registration:
    # initiates program, sets date and file name, loads existing data
    date_today = datetime.now().strftime('%Y%m%d')
    all_athletes_file = f'all_athletes_{date_today}.csv'
    existing_athletes = load_existing_athletes(all_athletes_file)

    # append main CSV file for today's registrations
    with open(all_athletes_file, mode='a', newline='') as file:
        fieldnames = ['uuid', 'first_name', 'middle_name', 'last_name', 'dob', 'gi_rank', 'no_gi_rank', 'gym', 'weight',
                      'weight_class','registration_type']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        while True:
            athlete = get_athlete_info(existing_athletes)
            athlete['weight_class'] = determine_weight_class(athlete['weight'])

            # append the new athlete's information to the main CSV file
            with open(all_athletes_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(athlete)

            # create console message confirming weight classes
            conf_message = []
            if athlete['registration_type'] == 'gi':
                conf_message.append(f"{athlete['gi_rank']} {athlete['weight_class']} for gi")
            elif athlete['registration_type'] == 'no-gi':
                conf_message.append(f"{athlete['no_gi_rank']} {athlete['weight_class']} for no-gi")
            elif athlete['registration_type'] == 'both':
                conf_message.append(f"{athlete['gi_rank']} {athlete['weight_class']} for gi")
                conf_message.append(f"{athlete['no_gi_rank']} {athlete['weight_class']} for no-gi")

            print(f"Registration complete. Athlete added to {' and '.join(conf_message)}.")

            another = input("Register another athlete? (yes/no): ").strip().lower()
            if another == 'no':
                    print("Registration complete.")
                    continue_registration = False
                    break
