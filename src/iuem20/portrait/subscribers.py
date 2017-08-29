# -*- coding: utf-8 -*-
import logging


# from zope.traversing.interfaces import IBeforeTraverseEvent
# from plone import api
# from plone.i18n.normalizer.interfaces import INormalizer
# from zope.component import getUtility


logger = logging.getLogger('iuem20.portrait')


def setPortraitTitle(context, event):
    # normalizer = getUtility(INormalizer)
    context.title = context.family_name + '-' + context.first_name
    # context.id = normalizer.normalize(context.title)
    context.reindexObject()


def trav(context, event):
    logger.info(event.request.keys())
    logger.info(event.request.get('HTTP_REFERER'))
    logger.info(event.request.get('ACTUAL_URL'))
    # import pdb;pdb.set_trace()
