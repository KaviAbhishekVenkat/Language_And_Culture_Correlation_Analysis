import re, sys
# Imports the Google Cloud client library

from google.cloud import translate
file_encoding = 'utf-8'
file_name = "KP3C2.srt"
with open(file_name, encoding=file_encoding, errors='replace') as f:
        lines = f.readlines()
# Instantiates a client
new_lines=[]
translate_client = translate.Client()

# The target language
target = 'en'
for word in lines:
    # Translates some text into english
    translation = translate_client.translate(
        word,
        target_language=target)
    new_lines.append(translation['translatedText'])
new_file_name = file_name[:-4] + '.txt'
with open(new_file_name, 'w') as f:
    for line in new_lines:
        f.write(line+" ")
# # print(u'Text: {}'.format(text))
# print(u'Translation: {}'.format(translation['translatedText']))