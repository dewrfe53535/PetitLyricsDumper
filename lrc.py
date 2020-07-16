# -*- coding: utf-8 -*-

# get lrc from xml
from xml.dom.minidom import parseString
from main import getLyrics

def format_time(t,offset = 0 ):
    if offset :
        t = int(t)
        t += offset
        t = str(t)
    ti = int(t)
    minute = int(ti/1000/60)
    second = int(ti/1000-minute*60)
    millisecond =t[-3:]
    return '[{0}:{1}.{2}] '.format(str(minute).zfill(2),str(second).zfill(2),millisecond)

def get_lrc(xml,outputname,offset = -80):
    DOMTree = parseString(xml)
    wsy = DOMTree.documentElement
    line = wsy.getElementsByTagName("line")
    lrc_str  = ''
    for l in line:
        linestring = l.getElementsByTagName("linestring")[0]
        if len(linestring.childNodes) > 0: # 歌词是文字同期情况下的处理
            line_lyric = linestring.childNodes[0].data
            time = l.getElementsByTagName("word")[0].getElementsByTagName("starttime")[0].childNodes[0].data
            lrc_str += format_time(time,offset)+line_lyric+'\n'
    file = open(outputname,'w+',encoding='utf-8')
    file.write(lrc_str)
    file.close()

if __name__ == "__main__":
    lId = input("Please input Lyric ID from Petit Lyrics: ")
    get_lrc(getLyrics(lId=lId),lId+'.lrc')