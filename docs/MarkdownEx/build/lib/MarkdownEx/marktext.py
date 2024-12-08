from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor

MARK_RE =r'(\?{3}|={2})(.*?)(\?{3}|={2})'

class MarkdownMark(Extension):
    def extendMarkdown(self, md):
        mark_proc = SimpleTagInlineProcessor(MARK_RE, 'mark')
        md.inlinePatterns.register(mark_proc, 'mark', 200)


def makeExtension(**kwargs):
    return MarkdownMark(**kwargs)
