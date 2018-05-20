import json


def http_headers_to_json(headers_path, results_path):               # Считываем заголовки в файл
    with open(headers_path) as f:
        head = f.readline().strip().split(' ')

        dic_head = {}

        if head[0].startswith('HTTP/1'):
            dic_head['protocol'] = head[0]
            dic_head['status_code'] = head[1]                       # Если заголовок начинается с HTTP/1
            dic_head['status_message'] = head[2]
            if len(head) > 3:
                for i in range(3, len(head)):                       # Если элементов в заголовке больше, то добавляем
                    dic_head['status_message'] += ' ' + head[i]     # i-ю строку
        
        elif head[0].startswith('HTTP/2'):                          # Если заголовок начинается с HTTP/2
            dic_head['protocol'] = head[0]
            dic_head['status_code'] = head[1]

        else:
            dic_head['method'] = head[0]
            dic_head['uri'] = head[1]
            dic_head['protocol'] = head[2]

        for line in f:
            res = line.replace('\n', '').split(': ')                # Заменяем переносы строк на пустой символ и
            if len(line) > 1:                                       # разделяем по двоеточию с пробелом
                dic_head[res[0]] = res[1]

    with open(results_path, 'w') as f:                              # Записываем результат в виде json заголовков
        json.dump(dic_head, f, indent=4)                            # в файл

