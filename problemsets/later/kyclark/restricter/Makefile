INPUT1 = tests/inputs/input1.fa
INPUT2 = tests/inputs/input2.fa

input1:
	./find_rsites.py -s 'GACGT^CT' -f $(INPUT1)

lookup:
	./find_rsites_lookup.py -l bionet.txt -e AarI -f $(INPUT1)

apol:
	./find_rsites.py -s 'R^AATTY' -f $(INPUT2)

get:
	curl -O ftp://ftp.neb.com/pub/rebase/bionet.txt
