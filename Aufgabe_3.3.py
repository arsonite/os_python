import os

for x in os.listdir("."):
	if 3 <= len(x) < 6:
		print x
