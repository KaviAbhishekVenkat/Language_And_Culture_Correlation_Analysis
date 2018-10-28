import re,sys

def main(args):
    # read file line by line
    file_name = args[1]
    file_encoding = 'utf-8' if len(args) < 3 else args[2]
    with open(file_name, encoding=file_encoding, errors='replace') as f:
        lines = f.readlines()

    text = ''
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
            text += ' ' + line
        new_lines = text.lstrip()
    new_file_name = file_name[:-4] + '2.srt'
    with open(new_file_name, 'w') as f:
        for line in new_lines:
            f.write(line)


if __name__ == '__main__':
    main(sys.argv)