import csv
def CSV_Write(file_name, sorted_array):
    with open(file_name, 'w', newline='\n') as f:
        writer = csv.writer(f)
        for element in sorted_array:
            writer.writerow([element])