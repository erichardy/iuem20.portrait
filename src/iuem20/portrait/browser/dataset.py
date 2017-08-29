# -*- coding: utf-8 -*-

from data import lorem
from data import portraits
from os.path import abspath
from os.path import dirname
from os.path import join
from plone import api
from plone.namedfile import NamedBlobImage
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.publisher.browser import BrowserView

import logging


PREFIX = abspath(dirname(__file__))
logger = logging.getLogger('iuem20.portrait: CREATEDATASET')


def input_image_path(f):
    return join(PREFIX, '../tests/images/', f)


class createDataSet(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        self.deletePortraits()
        self.createPortraits()

        url = portal.absolute_url() + '/folder_contents'
        self.request.response.redirect(url)

    def deletePortraits(self):
        portal = api.portal.get()
        try:
            api.content.delete(obj=portal['portraits'])
        except Exception:
            pass

    def createPortraits(self):
        portal = api.portal.get()
        portraitsFolder = api.content.create(type='Folder',
                                             title='Portraits',
                                             container=portal)

        for portrait in portraits:
            title = portrait['family_name'] + '-' + portrait['first_name']
            obj = api.content.create(type='iuem20.portrait',
                                     title=title,
                                     family_name=portrait['family_name'],
                                     first_name=portrait['first_name'],
                                     email=portrait['email'],
                                     bio=portrait['bio_fr'],
                                     bio_title=u'Ma Biographie',
                                     display_one=portrait['display_one'],
                                     presentation_one=portrait[
                                         'presentation_one'],
                                     display_two=portrait['display_two'],
                                     presentation_two=portrait[
                                         'presentation_two'],
                                     jobs=portrait['jobs'],
                                     status=portrait['status'],
                                     affiliation1=portrait['affiliation1'],
                                     affiliation2=portrait['affiliation2'],
                                     affiliation3=portrait['affiliation3'],
                                     personal_page=portrait['personal_page'],
                                     unit_page=portrait['unit_page'],
                                     research=portrait['research'],
                                     image=NamedBlobImage(),
                                     img_author=portrait['img_author'],
                                     thumbnail=NamedBlobImage(),
                                     container=portraitsFolder,
                                     )
            path_main = input_image_path(portrait['image'])
            fd = open(path_main, 'r')
            obj.image.data = fd.read()
            fd.close()
            obj.image.filename = portrait['image']
            obj.reindexObject()

            path_thumb = input_image_path(portrait['thumbnail'])
            fd = open(path_thumb, 'r')
            obj.thumbnail.data = fd.read()
            fd.close()
            obj.thumbnail.filename = portrait['thumbnail']
            obj.reindexObject()
            logger.info(obj.title + ' Created')

    def getPortraits(self):
        portal = api.portal.get()
        intids = getUtility(IIntIds)
        founds = api.content.find(context=portal,
                                  portal_type='iuem20.portrait',
                                  path='/'.join(portal.getPhysicalPath())
                                  )
        p_ids = []
        for found in founds:
            p_ids.append(intids.getId(found.getObject()))
        return p_ids

    def _loadImage(self, objField, image):
        imgPath = image.split('/')
        if len(imgPath) > 1:
            title = imgPath[len(imgPath) - 1]
        else:
            title = image
        path = input_image_path(image)
        fd = open(path, 'r')
        objField.data = fd.read()
        fd.close()
        objField.filename = title

    def _loadImagesInFolder(self, folderish, images):
        for img in images:
            imgPath = img.split('/')
            if len(imgPath) > 1:
                title = imgPath[len(imgPath) - 1]
            else:
                title = img
            image = api.content.create(type='Image',
                                       title=title,
                                       image=NamedBlobImage(),
                                       description=lorem,
                                       container=folderish)
            self._loadImage(image.image, img)
            image.reindexObject()
            api.content.transition(obj=image, transition='publish')
            image.reindexObject()
