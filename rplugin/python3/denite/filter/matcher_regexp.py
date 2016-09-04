# ============================================================================
# FILE: matcher_regexp.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import re
from .base import Base
from denite.util import split_input


class Filter(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'matcher_regexp'
        self.description = 'regexp matcher'

    def filter(self, context, candidates):
        if context['input'] == '':
            return candidates
        for pattern in split_input(context['input']):
            try:
                p = re.compile(pattern, flags=re.IGNORECASE
                               if context['ignorecase'] else 0)
            except Exception:
                return []
            candidates = [x for x in candidates if p.search(x['word'])]
        return candidates
