







def reported_dict(file, col_a, col_b):
	with open(file, 'r') as f:
		rdict = {}
		for line in f:
			values = line.split('\t')
			key = values[col_a].strip()
			value = values[col_b].strip()
			if key.startswith("CPDC") and value.startswith("c."):
				rdict.update({key:value})
	return rdict

def samples_dict(file, col_a, col_b):
	with open(file, 'r') as f:
		sdict = {}
		for line in f:
			values = line.split('\t')
			key = values[col_a].strip()
			value = values[col_b].strip()
			icd = value.split(",")
			if key.startswith("CPDC"):
				# check if icd code is not blank and starts with letter
				for x in icd:
					if x and x[0].isalpha():
						sdict.setdefault(key,[])
						x=x.strip()
						sdict[key].append(x)
	return sdict
def main():
	muts = reported_dict("/Users/ash/Desktop/network_dev/ReportedVariants.txt", 21, 10)
	icds = samples_dict("/Users/ash/Desktop/network_dev/ClinicalSamples.txt", 10, 5)

	# comebine mutations and icd codes on CPD ID
	with open("/Users/ash/Desktop/network_dev/icd_mut.igraph.bipartite.txt", 'w+') as out:
		for k,v in muts.iteritems():
			print icds.get(k)
			if icds.get(k) is None:
				continue
			for x in icds.get(k):
				out.write(x + "\t" + muts[k] + "\n")


if __name__== "__main__":
  main()