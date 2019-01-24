import string
import numpy
import itertools
import random
import statistics

class GenerateImpostors:
    all_documents = ''
    impostors = []

    def __init__(self, documents, num_of_impostors):
        self.all_documents = self.concat_lists(documents)
        words_list = self.get_words_without_punctuation(self.all_documents)
        impostor_size = statistics.median([len(x) for x in documents])
        for i in range(0,num_of_impostors):
            self.impostors.append(self.get_single_impostor(words_list, impostor_size))



    def get_words_without_punctuation(self, str):
        str = str.replace(',',' ')
        str = str.replace('.',' ')
        only_words = ''.join([x for x in str if x in string.ascii_letters + '\\\n\' '])
        only_words = [x.replace('\\','') for x in only_words.split()]
        return only_words

    def concat_lists(self, lists):
        concated_list = ''
        for l in lists:
            concated_list += l
        return concated_list

    def strip_list_of_lists_from_char(self,char):
        return self.concat_lists()

    def get_single_impostor(self, words, chunk_size):
        impostor = ''
        words_length = len(words)
        for i in range(chunk_size):
            rand_idx = int(random.uniform(0, words_length))
            impostor += ' ' + words[rand_idx]
        return impostor[1:]


