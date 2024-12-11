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
                    a = a.replace(k, "")
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






#find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item(). a


a= WordsFinder('file1.txt, file2.txt', 'file3.txt')
print(a.file_names)
finder2 = WordsFinder('test_file.txt','test_file2.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту