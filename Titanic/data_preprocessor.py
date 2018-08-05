import csv


def is_number(it):
	try:
		float(it)
	except ValueError:
		return False
	return True


def main():
	with open("train.csv") as f_original, open("processed_train.csv", 'w', newline='') as f_processed:
		reader = csv.reader(f_original)
		writer = csv.writer(f_processed)
		d_processed = []
		for column in zip(*reader):
			if is_number(column[1]):  # TODO: Account for empty cells on the first row
				if column[0] == "PassengerId":
					continue
				d_processed.append(column)
			elif column[0] != "Name" and column[0] != "Ticket" and column[0] != "Cabin":  # Convert non-numerical features to indicator variables
				classes = set(column[1:])
				print(classes)
				try: classes.remove('')  # Remove the empty 'class'
				except KeyError: pass
				print(classes)
				for c in classes:
					d_processed.append([c] + [int(f == c) for f in column[1:]])
		for r in zip(*d_processed):
			writer.writerow(r)


if __name__ == "__main__":
	main()
