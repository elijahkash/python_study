#!/usr/bin/env python3

# task 2
# Имеется сервер, имеющий N каналов для подключений клиентов. Когда клиент не подключен к каналу, канал простаивает. Когда к каналу подключен клиент, он считается занятым, и к нему нельзя подключиться. Каждый канал ведет текстовый лог подключений/отключений клиентов, следующего вида:
#
# 4 22 59 <...>
#
# Каждая запись данного лога – это временная метка в секундах от старта сервера. Нечетные записи (по порядку, а не по значению) – подключения, четные – отключения. В данном примере имеем лог канала, к которому на 4-ой секунде подключился клиент, на 22 секунде – отключился, и на 59 секунде – подключился, то есть сейчас этот канал занят.
#
# Для определенности все эти периоды являются полуинтервалами: левая граница включена в период подключения, а правая не включена. Т.е. если лог имеет вид 1 2 2 4, то это значит что канал был занят с 1 по 4 секунду.
#
# Необходимо имея логи всех каналов, определить периоды когда все каналы были заняты.
#
# Формат описания входных данных:
# В первой строке записано количество каналов N. В следующих строках описания каждого из N логов.
# Каждое описание логов состоит из двух строк:
#
# кол-во записей в логе
# записи в логе, разделенные пробелом
# Гарантируется, что в каждом логе четное количество записей и что лог отсортирован в неубывающем порядке.
#
# Формат описания выходных данных:
# В первой строке кол-во записей в результате
# Во второй строке временные метки, где нечетные записи (по порядку, а не по значению) – подключения, четные – отключения (т.е. формат аналогичен формату логов).
#
# Ограничения:
# N <= 500
# Максимальное количество записей в одном логе <= 500
res = []

def solution(f_in, f_out):
    # INPUT
    i = 0
    threads_count: int
    tmp: int
    threads = []
    for line in f_in:
        if i == 0:
            threads_count = int(line)
        elif i % 2:
            tmp = int(line)
            if tmp == 0:
                print(0)
                return
        else:
            cur_thread = []
            thread_vals = line.split(' ', tmp)
            for j in range(0, tmp):
                cur_thread.append(int(thread_vals[j]))
            threads.append(cur_thread)
        i += 1

    # CALC
    def dels(list_of_threads, time):
        for item in list_of_threads:
            while len(item) and item[1] <= time:
                item.pop(0)
                item.pop(0)
                if not len(item):
                    return False
        return True

    while True:
        max_start = threads[0][0]
        min_end = threads[0][1]

        for item in threads:
            max_start = max(max_start, item[0])
            min_end = min(min_end, item[1])

        if max_start < min_end:
            res.append(max_start)
            res.append(min_end)
            max_start = min_end

        if not dels(threads, max_start):
            print(len(res))
            for val in res:
                print(val, end=' ')
            return

if __name__ == "__main__":
    import sys
    solution(sys.stdin, sys.stdout)

# task1
# На вход программе передается лог, в каждой строке содержащий время включения и выключения некоторого устройства.
#
# Формат каждой строки:
# секунды:минуты:часы - секунды:минуты:часы
# где
# первое время — время включения
# второе время — время выключения.
#
# Результатом работы программы должно быть общее время работы прибора в секундах.
# import sys
#
# res = 0
# for line in sys.stdin:
#     start_time, end_time = line.split('-')
#     start_time.strip()
#     end_time.strip()
#     # print(line, "===", start_time, "===", end_time)
#     s, m, h = end_time.split(':')
#     line_time = int(h) * 3600 + int(m) * 60 + int(s)
#     # print(h, m, s)
#     s, m, h = start_time.split(':')
#     line_time = line_time - (int(h) * 3600 + int(m) * 60 + int(s))
#     res += line_time
#     # print(line_time)
#
# print(res)
