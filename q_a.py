import spacy
from spacy.lang.en.examples import sentences 
from transformers import pipeline
from information_retrieval.query_processor import ContextRetrieval
from information_retrieval.answer_extractor import AnswerExtractor
from data_processing.data_processing import DataProcessing

class FindAnswer:
    def __init__(self, query):
        self.query = query
        self.qa_model = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')


    def extractKnowledge (self):
        data_processor = DataProcessing()
        answer = data_processor.retrieve_answer(self.query)
        if answer: return answer
        else: return self.retrieveInformation()
    
    def retrieveInformation(self):
        context_retrieval = ContextRetrieval(self.query)
        answer_extractor = AnswerExtractor(self.qa_model)
        results = context_retrieval.web_search()
        answer = answer_extractor.extract(self.query, results)
        return answer