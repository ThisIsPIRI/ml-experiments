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
	hparams = '{'  # The JSON string of all divisors
	result_transposed = []
	filename = input("The filename: ")
	is_train = input("Is it a training dataset?(y/n): ") == 'y'
	# Read and process. Assumes column[0] contains the name of the column.
	with open(filename) as f_original:
		reader = csv.reader(f_original)
		to_discard = {"PassengerId", "Name", "Ticket", "Cabin"}
		for column in zip(*reader):
			if column[0] in to_discard:
				continue
			if is_number(column[1]):  # TODO: Account for empty cells on the first row
				float_column = [float(x) if is_number(x) else 0. for x in column[1:]]
				hparams += f"\"{column[0]}_divisor\": {max(float_column) - min(float_column)}, "
				result_transposed.append([column[0]] + [x / (max(float_column) - min(float_column)) for x in float_column])
			else:  # Convert non-numerical features to indicator variables.
				for c in SafeSet(column[1:]).safe_remove(''):
					result_transposed.append([c] + [int(f == c) for f in column[1:]])
	# Write the data
	with open("processed_" + filename, 'w', newline='') as f_processed:
		writer = csv.writer(f_processed)
		for r in zip(*result_transposed):
			writer.writerow(r)
	# Write the divisors
	if is_train:
		hparams = hparams[:-2] + '}'  # Remove the trailing comma
		with open("ScalingDivisors.json", 'w', newline='') as f_hparams:
			f_hparams.write(hparams)


if __name__ == "__main__":
	main()
