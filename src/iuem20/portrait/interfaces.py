# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective import dexteritytextindexer
from iuem20.portrait import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides
from zope.interface import Invalid
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import ASCIILine
from zope.schema import List
from zope.schema import Set
from zope.schema import TextLine
from zope.schema import URI

import logging
import re


logger = logging.getLogger('iuem20.portrait')


class IIuem20PortraitLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


# for controlpanel
jobList = []
jobList.append(u'Chercheur')
jobList.append(u'Plongeur')
jobList.append(u'Photographe')
jobList.append(u'Danseuse/Danseur')
jobList.append(u'')


class IIuem20PortraitSettings(model.Schema):

    portraits_title = TextLine(
        title=_(u'title for folder which present all portraits'),
        default=u'The team',
        required=False,
        )
    jobs = List(title=_(u'position, jobs, etc...'),
                description=_(u'One job per line'),
                value_type=TextLine(),
                default=jobList,
                )


class IIuem20PortraitSettingsForm(RegistryEditForm):
    schema = IIuem20PortraitSettings
    label = _(u'iuem20 portrait Settings')
    description = _(u'iuem20 portrait Settings Description')

    """
    def updateFields(self):
        super(IIuemAgreementsSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(IIuemAgreementsSettingsForm, self).updateWidgets()
    """


class IIuem20PortraitSettingsControlPanel(ControlPanelFormWrapper):
    form = IIuem20PortraitSettingsForm
# END controlpanel


checkEmail = re.compile(
    r'[a-zA-Z0-9._%-]+@([a-zA-Z0-9-]+\.)*[a-zA-Z]{2,4}').match


def validateEmail(value):
    if not checkEmail(value):
        raise Invalid(_(u'Invalid adress email'))
    return True


class IPortrait(model.Schema):
    """
    Schema du type de contenu ``iuem20.portrait``.
    """

    model.fieldset('indentification',
                   label=_(u'identification'),
                   fields=['family_name',
                           'first_name',
                           'description',
                           'email',
                           'image',
                           'img_author',
                           'thumbnail',
                           ])
    directives.omitted('title')
    dexteritytextindexer.searchable('title')
    title = TextLine(title=_(u'Form title'),)

    dexteritytextindexer.searchable('description')
    description = TextLine(title=_(u'very short portrait description'),
                           required=False,
                           )
    dexteritytextindexer.searchable('family_name')
    family_name = TextLine(title=_(u'person family name'),
                           required=True,
                           )
    dexteritytextindexer.searchable('first_name')
    first_name = TextLine(title=_(u'person first name'),
                          required=True,
                          )
    dexteritytextindexer.searchable('email')
    email = ASCIILine(title=_(u'email address'),
                      constraint=validateEmail,
                      required=False,
                      )
    image = NamedBlobImage(title=_(u'main photo'),
                           required=True
                           )
    img_author = TextLine(title=_(u'picture author'),
                          required=False,
                          )
    thumbnail = NamedBlobImage(title=_(u'small photo'),
                               required=True
                               )
    """
    status : technicien, ingenieur, chercheur (ne pas faire apparaitre)
    affiliation : 3 max, 3 champs libres.
    !!! supprimer le champ employer !
    Proposer l'affichage de la version anglaise. Par defaut : oui
    PHOTO : supprimer leadimage, champ photo + champ auteur de la photo !
    """
    #
    model.fieldset('biography',
                   label=_(u'biography'),
                   fields=['bio_title',
                           'bio',
                           ])
    dexteritytextindexer.searchable('bio_title')
    bio_title = TextLine(title=_(u'biography title'),
                         required=True,
                         default=u'Biography'
                         )
    dexteritytextindexer.searchable('bio')
    bio = RichText(title=_(u'biography'),
                   required=False,
                   )
    #
    model.fieldset('position',
                   label=_(u'position'),
                   fields=['jobs',
                           'status',
                           'affiliation1',
                           'affiliation2',
                           'affiliation3',
                           ])
    dexteritytextindexer.searchable('jobs')
    directives.widget(jobs='z3c.form.browser.checkbox.CheckBoxFieldWidget')
    jobs = Set(title=_(u'jobs'),
               description=_(u'select your jobs'),
               value_type=schema.Choice(
               vocabulary=u'iuem20.portrait.jobs'
               ),
               )
    dexteritytextindexer.searchable('status')
    status = TextLine(title=_(u'status'),
                      required=False,
                      )
    dexteritytextindexer.searchable('affiliation1')
    affiliation1 = TextLine(title=_(u'main affiliation'),
                            required=True,
                            )
    dexteritytextindexer.searchable('affiliation2')
    affiliation2 = TextLine(title=_(u'second affiliation'),
                            required=False,
                            )
    dexteritytextindexer.searchable('affiliation3')
    affiliation3 = TextLine(title=_(u'third affiliation'),
                            required=False,
                            )
    #
    model.fieldset('web',
                   label=_(u'web'),
                   fields=['personal_page', 'unit_page', 'research'])
    personal_page = URI(title=_(u'personal page'),
                        # constraint=validateURL,
                        required=False,
                        )
    unit_page = URI(title=_(u'web site of the research unit'),
                    # constraint=validateURL,
                    required=False,
                    )
    research = URI(title=_(u'web page of your researches'),
                   # constraint=validateURL,
                   required=False,
                   )


alsoProvides(IPortrait, IFormFieldProvider)
