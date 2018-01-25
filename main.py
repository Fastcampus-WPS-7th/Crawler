import re

# Patterns
# <div class="ellipsis rank01> ~ </div>부분의 텍스트
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# <a href=....>(내용)</a>
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')


def get_tag_attribute(attribute_name, tag_string):
    """
    특정 tag문자열(tag_string)에서 attribute_name에 해당하는 속성의 값을 리턴하는 함수
    :param attribute_name: 태그가 가진 속성명
    :return: 속성이 가진 값
    """
    # 문자열 포맷에 이름 붙이고, format()에서 키워드인수로 전달
    p = re.compile(r'^<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
        attribute_name=attribute_name
    ), re.DOTALL)
    m = re.search(p, tag_string)
    if m:
        return m.group('value')
    return ''


# example1 = '<a href="https://google.co.kr">Google</a>'
example1 = '<div><span class="sdf">ASDF</span></div>'
get_tag_attribute('href', example1)


def get_tag_content(tag_string):
    """
    특정 tag문자열(tag_string)이 가진 내용을 리턴
    tag문자열이 스스로 열고 닫는 태그 (ex: img태그)일 경우엔 공백을 반환
    :param tag_string:
    :return:
    """


example2 = '<div>Content</div>'
get_tag_content(example2)
# -> Content


# 로컬 HTML문서 불러오기
source = open('melon.html', 'rt').read()

# 전체 문서에서 PATTERN_DIV_RANK01에 해당하는 match object목록을 순회
match_list = re.finditer(PATTERN_DIV_RANK01, source)
for match_div_rank01 in match_list:
    # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
    div_rank01_content = match_div_rank01.group()

    # 부분 문자열에서 a태그의 내용을 title변수에 할당
    match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
    title = match_title.group(1)
    print(title)

"""
숙제
(좋아요 개수는 하지마세요)
print(chart) 했을 때
[
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
    {'rank': 1, 'title': '다른사람을 사랑하고 있어', 'artist': '수지 (SUZY)', 'album': 'Faces of Love',}
]
이렇게 나오도록 나머지 정규표현식 구현을 완성
"""

"""

    
"""
