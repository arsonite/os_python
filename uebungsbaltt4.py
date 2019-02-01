import os
import pickle


def readFile(f):
    words=[]
    with open(f,'r') as txt:
        for line in txt:
            for word in line.split():
                words.append(word)
    return words

def createDict():
    words_in_text={}
    for f in os.listdir(os.getcwd()):
        if(f.endswith('.txt')):
            for word in readFile(f):
                if word in words_in_text:
                    words_in_text[word].append(f)
                else:
                    words_in_text[word]=[f]
    return words_in_text



d=createDict()
pickle_out=open("dict.pickle","wb")
pickle.dump(d,pickle_out)
pickle_out.close()
