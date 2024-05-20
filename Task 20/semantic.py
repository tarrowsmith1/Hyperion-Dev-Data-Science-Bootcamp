import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# cat and monkey are both mammals so have biggest similarity between the 3.
# monkey and banana have second biggest similarity because monkeys are
# frugivorous omnivores and famously eat bananas.
# cat and banana have lowest simlirity score as cats are carnivores and do not
# eat bananas but they still have some similarity which is intriguing.

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - " + str(similarity))

nlp_example = spacy.load('en_core_web_sm')
example1 = nlp_example("chocolate")
example2 = nlp_example("cow")
example3 = nlp_example("grass")
print(example1.similarity(example2))
print(example3.similarity(example2))
print(example3.similarity(example1))

# The model you're using has no word vectors loaded, so the result of the
# Doc.similarity method will be based on the tagger, parser and NER,
# which may not give useful similarity judgements. This may happen if
# you're using one of the small models, e.g. `en_core_web_sm`, which don't
# ship with word vectors and only use context-sensitive tensors. You can
# always add your own word vectors, or use one of the larger models
# instead if available
