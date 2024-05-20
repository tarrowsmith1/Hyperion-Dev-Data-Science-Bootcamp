import spacy

def movie_recommender(description: str):
    nlp = spacy.load('en_core_web_md')


    #read movies.txt file
    with open('Task 20/movies.txt', 'r') as file:
        lines = []
        movies = []
        for line in file:
            line = line.strip()
            # to get only the descriptions
            lines.append(line[9:])
            # to get the movie names
            movies.append(line[0:7])

    model_sentence = nlp(description)

    # create a list of similarity scores for all movie descriptions
    similarity_scores = []
    for sentence in lines:
        similarity = nlp(sentence).similarity(model_sentence)
        similarity_scores.append(similarity)

    # create a dictionary of movies and their similarity scores
    similarity_scores_dict = dict(zip(movies, similarity_scores))

    # find the key-value pair with the highest value value
    most_similar = max(similarity_scores_dict.items(), key=lambda x: x[1])

    return f'Most similar movie is: {most_similar[0]}'

sentence_to_compare = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
print(movie_recommender(sentence_to_compare))