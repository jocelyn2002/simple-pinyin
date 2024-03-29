'''
数据集的接口, 读取数据集
'''

# words_path = './data/test_words.txt'
words_path = './data/global_wordfreq.release.txt'

def set_words_path(path):
    global words_path
    words_path = path

def is_Chinese(word):
    '''
    判断一个字符串是否全由汉字组成, 用于过滤文本
    '''
    return all('\u4e00' <= ch <= '\u9fff' for ch in word)

def iter_word_and_freq():
    """
    词频数据集, 迭代地返回 (word, freq)
    """
    with open(words_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                word, frequency = line.split()
                # 进行过滤
                if is_Chinese(word):
                    yield word, int(frequency)
            except Exception as e:
                pass
