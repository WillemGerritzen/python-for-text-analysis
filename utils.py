import os
import operator
from nltk.tokenize import sent_tokenize, word_tokenize


def get_paths(input_folder: str) -> list[str]:
    """
    Finds the .txt files that do not start with 'top' in a given directory
    :param input_folder:
    :return: A list of the files that fit the requirements
    """

    return [f for f in os.listdir(input_folder) if f[-4:] == '.txt' and f[:3] != 'top']


def get_basic_stats(txt_path: str) -> dict[str, int]:
    """
    Takes a path to a .txt file and outputs basic statistics on the contents of the file. Then writes the top 30 tokens to file
    :param txt_path: The path the to file
    :return: Basic satistics relevant to the contents of the file
    """

    with open('Data/books/' + txt_path, 'r', encoding=' utf-8') as f:
        s = f.read()

    sen = sent_tokenize(s)
    tok = word_tokenize(s)
    u_tok = set(tok)

    # Adapt the trigger word for chapter given the file
    if txt_path == 'HuckFinn.txt':
        ch = [word for word in tok if word == 'CHAPTER']

    elif txt_path == 'AnnaKarenina.txt':
        ch = [word for word in tok if word == 'Chapter ']

    else:
        ch = [word for word in tok if word == 'ACT']

    freq_tok = {}

    # Check if the file already exists. If not, runs the token count. If it does, does nothing
    if not os.path.isfile('Data/books/top_30_' + txt_path):

        for token in tok:
            if token in freq_tok.keys():
                continue

            freq_tok[token] = tok.count(token)

        top_30_tokens = sorted(freq_tok.items(), key=operator.itemgetter(1), reverse=True)[:30]

        with open('Data/books/top_30_' + txt_path, 'w', encoding='utf-8') as f:

            for token, freq in top_30_tokens:
                f.write(str(token) + ' ' + str(freq) + '\n')

    return {'num_sents': len(sen), 'num_tokens': len(tok), 'vocab_size': len(u_tok), 'num_chapters_or_acts': len(ch)}
