import csv

def condition_wrapper(condition):
    dragon_shield_moxfield_condition_translation = {
        'NearMint': "Near Mint"
    }
    return dragon_shield_moxfield_condition_translation[condition]

with open('all_my_cards.csv', 'r') as dragon_shield_csv:
    # Use the csv module to read the file
    reader = csv.DictReader(dragon_shield_csv, delimiter=',')
    # Open the Moxfield CSV file for writing
    with open('import_to_moxfield.csv', 'w') as moxfield_csv:
        # Use the csv module to write to the file
        writer = csv.writer(moxfield_csv)

        writer.writerow([
            'Count',
            'Tradelist Count', 
            'Name',
            'Edition',
            'Condition',
            'Language',
            'Foil',
            'Tags',
            'Last Modified',
            'Collector Number',
            'Alter',
            'Proxy',
            'Purchase Price',
        ])
        # Iterate over the rows in the Dragon Shield CS
        for row in reader:
            print(row)
            # Extract the card name, quantity, and set from the row
            count=row['Quantity']
            tradelist_count=row['Trade Quantity']
            name=row['Card Name']
            edition=row['Set Name']
            condition=condition_wrapper(row['Condition'])
            language=row['Language']
            foil=row['Printing']
            tags=None
            last_modified=row['Date Bought']
            collector_number=row['Card Number']
            alter=None
            proxy=None
            purchase_price=row['Price Bought']
            
            # Create a new row in the Moxfield CSV with the extracted data
            writer.writerow([count, tradelist_count, name, edition, condition, language, foil, tags, last_modified, collector_number, alter, proxy,purchase_price])
