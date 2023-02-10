import re


def main():
    print(parse(input('HTML: ')))


def parse(s):
    if re.search(r'<iframe(.)*><\/iframe>', s):
        if url_pattern := re.search(r'(http(s)?:\/\/(www\.)?youtube\.com\/embed\/)([a-zA-Z0-9_]+)', s):    #si se añadiera al principio ?: a los grupos 1 y 2, solo contaria el 3er grupo del final (como 1º)
            split_url = url_pattern.groups()
            return 'https://youtu.be/' + split_url[3]


if __name__ == '__main__':
    main()