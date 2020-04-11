def encode(text):
    textlist=list(text.replace('\n', ' ').split())
    word_to_number_map={}
    numbers=[]
    c=1
    for Sentence in textlist:
        if not Sentence.isalnum():
            for x in Sentence:
                if not x.isalnum():
                    Sentence=Sentence.replace(x,'')
        if not len(Sentence)==0:
            if Sentence in word_to_number_map:
                    numbers.append(word_to_number_map[Sentence])
            else:
                word_to_number_map[Sentence]=c
                c+=1
                numbers.append(word_to_number_map[Sentence])
            

    return word_to_number_map,numbers
text = """
:: #ali# $quera$
quera a'l'i ali
quera  
"""

print(encode(text))