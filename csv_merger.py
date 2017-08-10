import csv
import os
myfile = open("F:\\merged_csvs.csv", "a" )
writer = csv.writer(myfile)
counter = 0
file_list = os.listdir("C:\Users\Abdullah_A\Documents\Document Analysis\csv")
for file in file_list:
	counter += 1
	if file.endswith(".csv"):
		print(counter , file)
		with open(file, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if (row):
					writer.writerow(row)
			f.close()
myfile.close()
