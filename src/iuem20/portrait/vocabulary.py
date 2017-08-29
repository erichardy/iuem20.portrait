# -*- coding: utf-8 -*-

from plonetheme.iuem20.utils import getSettingValue
from plonetheme.iuem20.utils import make_voc
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory

import logging


logger = logging.getLogger('iuem20.portrait.vocabulary')


@implementer(IVocabularyFactory)
class _Jobs(object):
    """Voc. without grok"""

    def __call__(self, context):
        prefix = 'iuem20.portrait.interfaces.IIuem20PortraitSettings.'
        xjobs = getSettingValue('jobs', prefix=prefix)
        terms = []
        voc = make_voc(terms, xjobs)
        # import pdb;pdb.set_trace()
        return voc


@implementer(IVocabularyFactory)
class _localPortraits(object):

    def __call__(self, context):
        logger.info(context.absolute_url())
        portraits = ['a', 'b']
        terms = []
        voc = make_voc(terms, portraits)
        return voc


jobs = _Jobs()
localPortraits = _localPortraits()
