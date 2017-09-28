# -*- coding: utf-8 -*-
"""
Nous auront besoin des references :
http://docs.plone.org/external/plone.app.dexterity/docs/advanced/references.html
pour associer un projet a des missions et des portraits.
"""

from iuem20.portrait import _
# from iuem20.portrait import _
from iuem20.portrait.interfaces import IPortrait
from plone.dexterity.browser.add import DefaultAddForm
from plone.dexterity.browser.add import DefaultAddView
from plone.dexterity.browser import edit
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from plone.dexterity.content import Container
# from plonetheme.iuem20.utils import getSettingValue
from plonetheme.iuem20.utils import getTitleFromVoc
from plonetheme.iuem20.utils import reverse_email
from z3c.form import button
# from zope.interface import alsoProvides
from zope.interface import implementer
from zope.publisher.browser import BrowserView

import logging


logger = logging.getLogger('iuem20.portrait')


class PortraitView(BrowserView):

    def mailEncoded(self):
        try:
            if len(self.context.email) == 0:
                return False
        except Exception:
            return False
        return reverse_email(self.context.email)

    def getJobs(self):
        jobs = []
        for job in self.context.jobs:
            j = getTitleFromVoc('iuem20.portrait.jobs', job)
            jobs.append(j)
        return (', ').join(jobs)

    def getAffiliations(self):
        c = self.context
        aff = u''
        if c.affiliation1:
            aff += c.affiliation1
        if c.affiliation2:
            aff += ', ' + c.affiliation2
        if c.affiliation3:
            aff += ', ' + c.affiliation3
        return aff

    def getPortraitAttr(self, field):
        # p = self.context
        try:
            value = eval('self.context.' + field)
            if value:
                return value
            else:
                return False
        except Exception:
            return False

    def encodeEmail(self, email):
        return 'blabla'

    def displayEN(self):
        return self.context.display_en

    def bio(self):
        try:
            return len(self.context.bio.raw) > 4
        except Exception:
            return False

    def getPictFilename(self):
        try:
            return self.context.image.filename
        except Exception:
            return False

    def bio_title(self):
        if len(self.context.bio_title) < 2:
            return u''
        return self.context.bio_title


"""
class editForm(edit.DefaultEditForm):
    pass
"""


@implementer(IPortrait)
class portrait(Container):

    def mailEncoded(self):
        return reverse_email(self.email)

    def getJobs(self):
        jobs = []
        for job in self.jobs:
            j = getTitleFromVoc('iuem20.portrait.jobs', job)
            jobs.append(j)
        return (', ').join(jobs)

    def getAffiliations(self):
        c = self
        aff = u''
        if c.affiliation1:
            aff += c.affiliation1
        if c.affiliation2:
            aff += ', ' + c.affiliation2
        if c.affiliation3:
            aff += ', ' + c.affiliation3
        return aff

    def getPortraitAttr(self, field):
        # p = self
        try:
            value = eval('self.' + field)
            if value:
                return value
            else:
                return False
        except Exception:
            return False

    def encodeEmail(self, email):
        return 'blabla'

    def displayEN(self):
        return self.display_en

    def bioFR(self):
        try:
            return len(self.bio_fr.raw) > 4
        except Exception:
            return False

    def bioEN(self):
        try:
            return len(self.bio_en.raw) > 4
        except Exception:
            return False

    def getPictFilename(self):
        try:
            return self.main_pict.filename
        except Exception:
            return False


class AddForm(DefaultAddForm):
    portal_type = 'iuem20.portrait'
    # ignoreContext = True
    label = _(u'Add a new portrait !')

    def getWidgetInGroups(self, f):
        """
        :param f: le champ recherché
        :type f: str
        :returns: le champ (objet ``field``) recherché dans les groupes
            ou ``False`` si non trouvé
        """
        for group in self.groups:
            logger.info(group)
            w = group.fields.get(f)
            if w is not None:
                return (w, group)
        return (False, False)

    def getWidgetAndGroup(self, f):
        # import pdb;pdb.set_trace()
        for group in self.groups:
            fields = group.fields
            logger.info(group.label)

            if fields.get(f):
                logger.info(group.label)

    def update(self):
        super(DefaultAddForm, self).update()
        DefaultAddForm.update(self)
        # logger.info('in update addForm portrait')
        # logger.info(self.context)
        # import pdb;pdb.set_trace()

    def updateWidgets(self):
        # import pdb;pdb.set_trace()
        super(DefaultAddForm, self).updateWidgets()
        # self.getWidgetAndGroup('email')
        # logger.info(self.context)

    @button.buttonAndHandler(_(u'Save this portrait'),
                             name='save_this_portrait')
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = _('Please correct errors')
            return
        try:
            obj = self.createAndAdd(data)
            # logger.info(obj)
            # logger.info(u'=-=-=-=-=')
            context = self.context
            objId = obj.getId()
            url = context[objId].absolute_url()
            self.request.response.redirect(url)
        except Exception:
            raise

    @button.buttonAndHandler(_(u'Cancel this portrait'))
    def handleCancel(self, action):
        data, errors = self.extractData()
        # context is the thesis repo
        contextURL = self.context.absolute_url()
        self.request.response.redirect(contextURL)


class AddView(DefaultAddView):
    form = AddForm
    # template = ViewPageTemplateFile("portrait_addForm.pt")
    # index = template


class EditForm(edit.DefaultEditForm):
    # template = ViewPageTemplateFile("portrait_addForm.pt")
    pass


"""
$("#formfield-form-widgets-IThumbnail-thumbnail").insertAfter('#formfield-form-widgets-thumb_pict')
$("#autotoc-item-autotoc-0").hide()
"""
