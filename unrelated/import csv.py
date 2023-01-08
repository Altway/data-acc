import csv

# Open the Dragon Shield CSV file for reading
with open('dragon_shield.csv', 'r') as dragon_shield_csv:
    # Use the csv module to read the file
    reader = csv.reader(dragon_shield_csv)

    # Open the Moxfield CSV file for writing
    with open('moxfield.csv', 'w') as moxfield_csv:
        # Use the csv module to write to the file
        writer = csv.writer(moxfield_csv)

        # Iterate over the rows in the Dragon Shield CSV
        for row in reader:
            # Extract the card name, quantity, and set from the row
            card_name = row[0]
            quantity = row[1]
            card_set = row[2]

            # Create a new row in the Moxfield CSV with the extracted data
            writer.writerow([card_name, quantity, card_set])
