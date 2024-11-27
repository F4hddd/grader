import csv

classification_boundaries = [
    (70, "1"),
    (60, "2:1"),
    (50, "2:2"),
    (40, "3"),
    (0, "F")
]

filename = input("Enter the filename: ")

with open(filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    results = []

    for row in reader:
        student_id = row[0]
        grades = [int(g) for g in row[1:] if g]
        avg_grade = sum(grades) / len(grades)
        classification = next(c for b, c in classification_boundaries if avg_grade >= b)
        results.append((student_id, f"{avg_grade:.2f}", classification))

output_filename = filename + "_out.csv"

with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(results)
