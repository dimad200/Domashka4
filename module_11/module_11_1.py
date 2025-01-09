import datetime
import multiprocessing

def read_info(name):
    all_data=[]
    with open(name,"r") as file:
        while True:
            stroka = file.readline()
            all_data.append(stroka)
            if not stroka:
                break



filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

# start=datetime.datetime.now()
# for _ in filenames:
#     read_info(_)
# end=datetime.datetime.now()
# print(end-start)

# Многопроцессный
if __name__ == '__main__':
    start=datetime.datetime.now()
    with multiprocessing.Pool(4) as p:
        print(p.map(read_info, filenames))

    end=datetime.datetime.now()
    print(end-start)