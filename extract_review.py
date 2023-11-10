import csv

# Function to read CSV and convert to review object
def getReviewsFromCSV(csv_file_path):
    reviews = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            review = {
                'source': row['Source'],
                'date': row['Date'],
                'rating': row['Rating'],
                'review': row['Reviews'].strip('"'),
                'price': row['Price'],
            }
            reviews.append(review)
    return reviews

# Path to your CSV file
csv_file_path = 'reviews.csv'  # Replace with your CSV file path

# Call the function and print the result
review_objects = getReviewsFromCSV(csv_file_path)

for obj in review_objects:
    obj_str = ", ".join([f"{k}: '{v}'" if isinstance(v, str) else f"{k}: {v}" for k, v in obj.items()])
    print("{" + obj_str + "},")
