import re

# Patterns
# <div class="ellipsis rank01> ~ </div>부분의 텍스트
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# <a href=....>(내용)</a>
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

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

