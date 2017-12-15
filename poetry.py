import random
f = open("./phoentics.txt","r")
wiki = open("./knowledge.txt","r")
contents = f.readlines()
wiki_contents = wiki.readlines() #Expected to be list of strings of words

thresh = 3
rel_con = [] #relevant content (aka phonetics from the file)
word_dict = {}
wiki_dict = {}
#thresh = 2

def follow_rhyme_words(fword):
	#words that follow from it
	words = []
	for w in word_dict.keys():
		if word_rhyme(word_dict[fword],word_dict[w]):
			words.append(w)
	return words

def word_rhyme(fword,sword): #GIVE IT LIST OF PHONETICS
	#does fword morph into sword phoentically?
	fl = fword[-thresh:]
	sl = sword[:thresh]
	return fword[-thresh:] == sword[-thresh:]

	#return fword[-1] == sword[-1]
	#return reversed(fl) == sl

def initialize_phoentics():
    global contents, word_dict
    for l in contents:
            if ";" not in l:
                    d = l.split(" ")
                    d[-1] = d[-1][:-1]
                    rel_con.append(d)


    for l in rel_con:
            word_dict[l[0]] = l[2:]

def initialize_wiki():
    global wiki_dict, wiki_contents
    for string_phrase in wiki_contents:
        temp_split = string_phrase.split(" ")
        for temp_word in range(len(temp_split)-1):
            if temp_split[temp_word] not in wiki_dict.keys():
                wiki_dict[temp_split[temp_word]] = {temp_split[temp_word+1]:1}
            else:
                if temp_split[temp_word+1] not in wiki_dict[temp_split[temp_word]].keys():
                    wiki_dict[temp_split[temp_word]][temp_split[temp_word+1]] = 1
                else:
                    wiki_dict[temp_split[temp_word]][temp_split[temp_word+1]] += 1
        #print string_phrase

def next_wiki_word(wword):
    nword = random.choice(wiki_dict[wword].keys())
    return nword

def write_pair_lines(): #npairs = number of pair rhymes
    cur_word = random.choice(wiki_dict.keys())
    first_line = ""
    second_line = ""
    
    for i in range(7):
        first_line +=  cur_word + " "
        try:
            cur_word = next_wiki_word(cur_word)
        except:
            pass
    start_rhyme = random.choice(word_dict.keys())
    next_rhyme = random.choice(follow_rhyme_words(start_rhyme))

    first_line += start_rhyme

    print "\n"

    cur_word = random.choice(wiki_dict.keys())
    for i in range(7):
        second_line += cur_word + " "
        try:
            cur_word = next_wiki_word(cur_word)
        except:
            pass
    second_line += next_rhyme

    print first_line
    print second_line
    
    

initialize_phoentics()
initialize_wiki()

write_pair_lines()
write_pair_lines()
write_pair_lines()

"""
rhymestring = "AMPLE"
currhymeword = "AMPLE"

for i in range(4):
        currhymeword = random.choice(follow_rhyme_words(currhymeword))
        rhymestring += " " + currhymeword
print rhymestring

"""


"""


#g = follow_words("TRAIN")
##h = follow_words("INTRUDERS")
###print word_dict["TRAIN"], "TRAIN"
##print word_dict["TRAIN"],word_dict["AIM"]
##print word_connects(word_dict["TRAIN"],word_dict["AIM"])
###print g
###print g
##print word_dict[g[0]], g[0]
##print word_dict[h[0]], h[0]
"""
