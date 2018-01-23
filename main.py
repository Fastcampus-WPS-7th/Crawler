import re

source = '''<td><div class="wrap">
<div class="wrap_song_info">
    <div class="ellipsis rank01"><span>
        <a href="javascript:melon.play.playSong('19030101',30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>
    </span></div><br>
    <div class="ellipsis rank02">
        <a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a><span class="checkEllipsis" style="display: none;"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a></span>
    </div>
</div>
</div></td>'''

# 위의 소스에서 <div class="ellipsis rank01> ~ </div>부분의 텍스트를
# div_rank01 변수에 할당
pattern_div_rank01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
div_rank01 = re.search(pattern_div_rank01, source).group()
print(div_rank01)

# div_rank01 변수에 있는 문자열에서
# <a href=....>(내용)</a>
# 위의 (내용)그룹에 해당하는 부분을 title변수에 할당
pattern_a_content = re.compile(r'<a.*?>(.*?)</a>')
title = re.search(pattern_a_content, div_rank01).group(1)
print(title)
