
"""
Python Basic Lab 1-1
Word Count with 2 lists
without 'dict'

word_cnt_list(path)
    interface that interacts with user

word_cnt_db(path)
    making 2 lists 'words' and 'cnts'
"""
import re
def word_cnt_db(path):
    """
    :param path: path of file
    :return: [words, cnts]
    """
    # try open file at 'path' (parameter)

    # making 2 lists words & cnts
    # words's index and cnts's index are corresponding
    words = list()  # store words (dict's key)
    cnts = list()  # store counts (dict's val)

    # CAUTION : word's len < 1
    #           end with white space or [, . ? : ; ' " \n]
    #           ignore n:n
    #           be careful '\n' : using strip()
    fh = []
    try:
        fh = open(path)
    except:
        exit(0)
    templist = list()
    for line in fh:
        line = line.rstrip()
        line = line.rstrip(',.?:;\'\"')

        line = line.rstrip().rstrip(',')
        #line = re.sub(r'[^\d+:\d+]', '', line)
        templist.extend(line.split())
      

    print(len(templist))

    for word in templist:
        if not word in words:
            words.append(word)
            cnts.append(0)
        else:
            index =words.index(word)
            cnts[index]  +=  1


    print(len(words))
    print(len(cnts))


    return [words, cnts]


def word_cnt_list(path):
    """
    :param path: path file
    :return: None
    """
    # use 'word_cnt_db(path)' get Database

    # while user enter "EXITprogram" get word to find
    # CAUTION : get input without prompt
    #   -> just call input() not input( 'anything' )

    # CAUTION : if there are no 'word2find' in words print '0'

    # exit program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'

    words, cnts= word_cnt_db(path)
    print(words)
    
    while(True):
        data=input()
        if(data == 'EXITprogram'):
            break
        if data in words:
            index = words.index(data)
            print(cnts[index])
        else:
            #print('not exist in the list')
            print(0)
    
    exit(0)


if __name__ == '__main__':
    path = './genesis.txt'
    word_cnt_list(path)
