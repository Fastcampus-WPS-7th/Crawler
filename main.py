import re
from bs4 import BeautifulSoup

source = open('melon.html', 'rt').read()
soup = BeautifulSoup(source, 'lxml')



if __name__ == '__main__':
    result = get_top100_list()
    for item in result:
        print(item)
