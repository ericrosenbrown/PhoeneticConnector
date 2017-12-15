import random
f = open("./phoentics.txt","r")
contents = f.readlines()

thresh = 1
#thresh = 2

def follow_words(fword):
	#words that follow from it
	words = []
	for w in word_dict.keys():
		if word_connects(word_dict[fword],word_dict[w]):
			words.append(w)
	return words

def follow_rhyme_words(fword):
	#words that follow from it
	words = []
	for w in word_dict.keys():
		if word_rhyme(word_dict[fword],word_dict[w]):
			words.append(w)
	return words

def word_connects(fword,sword): #GIVE IT LIST OF PHONETICS
	#does fword morph into sword phoentically?
	fl = fword[-thresh:]
	sl = sword[:thresh]
	#print fl,sl
	return len([i for i in fl if i in sl]) > 0
	#return reversed(fl) == sl

def word_rhyme(fword,sword): #GIVE IT LIST OF PHONETICS
	#does fword morph into sword phoentically?
	fl = fword[-thresh:]
	sl = sword[:thresh]
	#print fl,sl
	return fword[-1] == sword[-1]
	#return reversed(fl) == sl

rel_con = [] #relevant content (aka phonetics from the file)
for l in contents:
	if ";" not in l:
		d = l.split(" ")
		d[-1] = d[-1][:-1]
		rel_con.append(d)

word_dict = {}
for l in rel_con:
	word_dict[l[0]] = l[2:]

mystring = "DESK"
curword = "DESK"
for i in range(4):
        curword = random.choice(follow_words(curword))
        mystring += " " + curword
print mystring

rhymestring = "FLYING"
currhymeword = "FLYING"

for i in range(4):
        currhymeword = random.choice(follow_rhyme_words(currhymeword))
        rhymestring += " " + currhymeword
print rhymestring

#g = follow_words("TRAIN")
##h = follow_words("INTRUDERS")
###print word_dict["TRAIN"], "TRAIN"
##print word_dict["TRAIN"],word_dict["AIM"]
##print word_connects(word_dict["TRAIN"],word_dict["AIM"])
###print g
###print g
##print word_dict[g[0]], g[0]
##print word_dict[h[0]], h[0]


