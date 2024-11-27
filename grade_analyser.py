import csv

def classify_grade(average_grade):
    if average_grade >= 70:
        return "1"
    elif average_grade >= 60:
        return "2:1"
    elif average_grade >= 50:
        return "2:2"
    elif average_grade >= 40:
        return "3"
    else:
        return "F"

def process_student_data():
    input_file = input("Enter the filename of the student file: ")
    output_file = input_file + "_out.csv"
    
    with open(input_file, mode="r") as infile, open(output_file, mode="w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            student_id = row[0]
            grades = [float(grade) for grade in row[1:] if grade.strip()]
            average_grade = sum(grades) / len(grades)
            classification = classify_grade(average_grade)
            writer.writerow([student_id, f"{average_grade:.2f}", classification])

    print(f"Processed data written to {output_file}")

# run 
process_student_data()
