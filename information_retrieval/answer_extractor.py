
import operator
from transformers import DistilBertTokenizer, DistilBertModel

class AnswerExtractor:
    def __init__(self, qa_model):
        self.model = qa_model

    def extract(self, question, passages):
        answers = []
        for passage in passages:
            try:
                answer = self.model(question=question, context=passage)
                answer['text'] = passage
                answers.append(answer)
            except KeyError:
                pass
        answers.sort(key=operator.itemgetter('score'), reverse=True)
        return answers[0]['answer']