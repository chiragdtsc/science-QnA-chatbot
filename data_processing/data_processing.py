import re
import pandas as pd
import numpy as np
from gensim.parsing.preprocessing import remove_stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

SBERT_MODEL = SentenceTransformer('bert-base-nli-mean-tokens')

class DataProcessing:

    def __init__(self) -> None:
        self.df = pd.read_csv('data/Science_knowledge_base.csv')
        self.cleaned_sentences = self.get_cleaned_sentences()

    def get_cleaned_sentences(self, stopwords = False):
        cleaned_sentences=[]
    
        for index, row in self.df.iterrows():
            cleaned= self.clean_sentence(row["questions"],stopwords)
            cleaned_sentences.append(cleaned)
        return cleaned_sentences

    def clean_sentence(self, sentence, stopwords = False):
        sentence=sentence.lower().strip()
        sentence= re.sub(r'[^a-z0-9\s]','', sentence)
        
        if stopwords:
            sentence=remove_stopwords(sentence)
        
        return sentence

    def retrieve_answer(self, question):
        question = self.clean_sentence(question, stopwords=False)
        question_embedding = SBERT_MODEL.encode([question])
        sentence_embeddings = np.load('data/knowledge_base_embeddings.npy')
        max_sim=-1
        index_sim=-1
        for index,faq_embedding in enumerate(sentence_embeddings):
            sim = cosine_similarity(faq_embedding,question_embedding)[0][0]
            if sim>max_sim:
                max_sim=sim
                index_sim=index
        if max_sim>0.91:
            return self.df.iloc[index_sim,2]
        else: return None

    def knowledge_training(self):
        sent_bertphrase_embeddings=[]
        for sentence in self.cleaned_sentences:
            print(sentence)
            sent_bertphrase_embeddings.append(SBERT_MODEL.encode([sentence]))
        np.save('knowledge_base_embeddings.npy', sent_bertphrase_embeddings)