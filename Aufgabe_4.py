import os
import re
import pickle

w = {}
f = filter(lambda x : re.search("txt$", x), os.listdir("."))
print f
for td in f:
	for word in re.split("\W+", open(td).read()):
		if(len(word) > 0):
			if(word not in w):
				w[word] = [td]
			elif(td not in w[word]):
				w[word].append(td)
pickle.dump(w, open("text_dump.p", "wb"))

print w
