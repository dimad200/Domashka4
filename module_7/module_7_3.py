class WordsFinder():

    def __init__(self,*files_name):
        self.file_names=[]
        for i in files_name:
            self.file_names.append(i)

    def get_all_words(self, *files_name):
        all_words = {}
        replace = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for i in self.file_names:
            with open(i, encoding="utf-8") as file:
                a = file.read()
                a = a.lower()
                for k in replace:
                    a = a.replace(k, '')
                a = a.split()
            all_words[i] = a
        return all_words

    def find(self, word):
        self.word = word.lower()
        znachenie = None
        slowar = self.get_all_words()
        for k, v in slowar.items():
            for i in range(len(v)):
                if self.word == v[i]:
                    znachenie = i + 1
                    return {k: znachenie}
    def count(self, word):
        self.word = word.lower()
        znachenie = 0
        slowar = self.get_all_words()
        for k, v in slowar.items():
            for i in range(len(v)):
                if self.word == v[i]:
                    znachenie+=1
        return {k: znachenie}
# проверка
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
