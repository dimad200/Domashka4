first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
# В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
first_result = [len(element_iz_first_strings) for element_iz_first_strings in first_strings if
                len(element_iz_first_strings) > 5]
second_result = [(pervoe, vtoroe) for pervoe in first_strings for vtoroe in second_strings if
                 len(pervoe) == len(vtoroe)]
third_result ={stroka:len(stroka)  for stroka in first_strings + second_strings if not len(stroka)%2

}
print(first_result)
print(second_result)
print(third_result)