# -*- coding: utf-8 -*-
"""
    sphinxcontrib.latexjlreq
"""
from __future__ import absolute_import


def setup(app):
    from sphinxcontrib.latexjlreq import jlreqruby, jlreqkenten, jlreqkasen, jlreqkansuji

    # delegate to submodules
    jlreqruby.setup(app)
    jlreqkenten.setup(app)
    jlreqkasen.setup(app)
    jlreqkansuji.setup(app)
