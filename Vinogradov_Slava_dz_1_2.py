from collections import Counter


def remote_addr():
    with open("nginx_logs.txt", "r", encoding="utf-8") as f:
        for ip in f:
            yield ip.split()[0]


def request_type():
    with open("nginx_logs.txt", "r", encoding="utf-8") as f:
        for req_type in f:
            yield req_type.split()[5].replace('"', "")


def requested_resource():
    with open("nginx_logs.txt", "r", encoding="utf-8") as f:
        for req_res in f:
            yield req_res.split()[6]


result = list(zip(remote_addr(), request_type(), requested_resource()))  # Список кортежей с данными
spamer = list(remote_addr())
s = Counter(spamer).most_common(1)
print(f'ID спамера: {s[0][0]} - кол-во запросов: {s[0][1]}')
