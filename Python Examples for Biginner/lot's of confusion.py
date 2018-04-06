import random
from urllib import urlopen
import sys

WORD_URL = "www://thearticlesandnews.com"
WORDS = []

PHRASES ={
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init___(self, ***)":
    "class %%% has-a ___init___ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** finction, and call it with parameters sel, @@@",
    "***.***='***'":
    "From *** get the *** attribibute and set it to '***'"
}

# do thay want to drill pharses first
PHARSE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "enlish":
    PHARSE_FIRST = True

# load up the word from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_name = random.sample(WORDS, snippet.count("***"))
    result = []
    param_name = []
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_name.append(', '.join(random.sample(WORDS, param_count)))

        for sentence in snippet, phrase:
            result = sentence[:]

            #fack class names

        for word in class_names:
            result = result.replace("%%%", word, 1)

            #fack other names
        for word in other_name:
            result = result.replace("***", word, 1)

        # fack parameter list
        for word in param_name:
            results = result.replace("@@@", word, 1)

        result.append(result)

    return results


#keep going until they hit CTRL+D
try:
    while True:
        snippt = PHRASES.key()
        random.shuffle(snippets)

        for snippet in snippets:
            parase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHARSE_FIRST:
                question, answer = answer, question

            print question

            raw_input('> ')
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\Bye"    
