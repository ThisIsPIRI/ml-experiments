import csv


def is_number(it):
	try:
		float(it)
	except ValueError:
		return False
	return True


class SafeSet(set):
	def safe_remove(self, element):
		"""Removes element. Does not throw a KeyError even if element isn't present. Returns the SafeSet itself."""
		try:
			self.remove(element)
		except KeyError:
			pass
		return self


def main():
	with open("train.csv") as f_original, open("processed_train.csv", 'w', newline='') as f_processed:
		reader = csv.reader(f_original)
		writer = csv.writer(f_processed)
		result_transposed = []
		discarded = {"PassengerId", "Name", "Ticket", "Cabin"}
		for column in zip(*reader):
			if column[0] in discarded:
				continue
			if is_number(column[1]):  # TODO: Account for empty cells on the first row
				result_transposed.append(column)
			else:  # Convert non-numerical features to indicator variables.
				for c in SafeSet(column[1:]).safe_remove(''):
					result_transposed.append([c] + [int(f == c) for f in column[1:]])
		for r in zip(*result_transposed):
			writer.writerow(r)


if __name__ == "__main__":
	main()
