from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
import re

class ColorInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('font')
        el.set('color', '#'+m.group(1))
        el.text = m.group(2)
        return el, m.start(0), m.end(0)


class ColorExtension(Extension):
    """
    文本排版
    匹配：%(#color)[text]
    输出：<font color:#color>Colored Text</font>
    """

    def extendMarkdown(self, md):
        COLOR_PATTERN = r'\%\(#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})\)\[((.*?))\]'  # like %(#colour)[colored text]
        md.inlinePatterns.register(ColorInlineProcessor(COLOR_PATTERN, md), 'color', 180)
        
def makeExtension(**kwargs):
    return ColorExtension(**kwargs)