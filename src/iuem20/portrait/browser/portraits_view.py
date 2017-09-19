# -*- coding: utf-8 -*-

from iuem20.portrait import _
from plone import api
from plonetheme.iuem20.utils import getSettingValue
from zope.publisher.browser import BrowserView

import logging


# from plonetheme.bebest.utils import sort_by_position

logger = logging.getLogger('iuem20.portrait')


class portraitsView(BrowserView):

    title = _(u'portraits_view')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getViewTitle(self):
        prefix = 'iuem20.portrait.interfaces.IIuem20PortraitSettings.'
        return (getSettingValue('portraits_title', prefix=prefix))

    def getPortraitsObjs(self, effective=False):
        """
        :param effective: tri par date de publication
        :type effective: Boolean
        :return: liste des portraits triés par ordre alphabétique du nom,
          ou par ordre de date de publication. Pour les portraits,
          le tri se fait par ordre alphabétique du nom.
        """
        context = self.context
        founds = api.content.find(context=self.context,
                                  portal_type='iuem20.portrait',
                                  path='/'.join(context.getPhysicalPath()),
                                  depth=1,
                                  )
        if len(founds) == 0:
            return False
        objs = [found.getObject() for found in founds]
        if effective:
            sortedObjs = sorted(objs,
                                key=lambda obj: obj.effective(),
                                reverse=True)
            return sortedObjs
        return sorted(objs,
                      key=lambda obj: obj.Title(),
                      reverse=False)
