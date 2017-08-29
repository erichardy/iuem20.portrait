# -*- coding: utf-8 -*-

from plone.app.textfield.value import RichTextValue


lorem = """
Vivamus dictum, nunc a tincidunt semper, lectus justo maximus neque,
et pulvinar ipsum dolor at nisl. Maecenas porttitor dolor nec ante cursus
viverra. Maecenas massa nunc, semper vitae pulvinar at, semper
at metus. Cras a fermentum diam. Sed a lobortis
risus, efficitur tincidunt lorem.
"""

bio_fr_text = """
<h4>Savoir-faire opérationnels</h4>
<ul>
<li>Utiliser les méthodes de prévention et
de gestion des risques<br/></li>
</ul>
<h4>Lieu d'exercice</h4>
<ul>
<li>L’activité s’exerce généralement au sein d'un service informatique<br/>
</li>
</ul>
<h3>Dipl&ocirc;me exig&eacute;</h3>
<ul>
<li>Doctorat, diplôme d’ingénieur<br/></li>
</ul>
<h3>Formations et expérience professionnelle souhaitables</h3>
<ul><li>Filière informatique</li></ul>
"""

bio_alt1_text = """
<h2>ALT 1 The RichTextValue<a class="headerlink" href="#the-richtextvalue"
title="Permalink to this headline">¶</a></h2>
<p>The <code class="docutils literal"><span class="pre">RichText</span>
</code> field does not store a string. Instead, it stores a
<code class="docutils literal"><span class="pre">RichTextValue</span>
</code> object. This is an immutable object that has the
following properties:</p>
<dl class="docutils">
<dt><code class="docutils literal"><span class="pre">raw</span></code></dt>
<dd>a unicode string with the original input markup;</dd>
<dt><code class="docutils literal"><span class="pre">mimeType</span></code>
</dt>
<dd>the MIME type of the original markup, e.g.
<code class="docutils literal"><span class="pre">text/html</span></code> or
<code class="docutils literal"><span class="pre">text/structured</span>
</code>;</dd>
<dt><code class="docutils literal"><span class="pre">encoding</span></code>
</dt>
<dd>the default character encoding used when transforming the input markup.
Most likely, this will be UTF-8;</dd>
<dt><code class="docutils literal"><span class="pre">raw_encoded</span>
</code></dt>
<dd>the raw input encoded in the given encoding;</dd>
<dt><code class="docutils literal"><span class="pre">outputMimeType</span>
</code></dt>
<dd>the MIME type of the default output, taken from the field at the time of
instantiation;</dd>
<dt><code class="docutils literal"><span class="pre">output</span></code></dt>
<dd>a unicode object representing the transformed output. If possible, this
is cached persistently until the <code class="docutils literal">
<span class="pre">RichTextValue</span></code> is replaced with a
new one (as happens when an edit form is saved, for example).</dd>
</dl>
"""
bio_alt2_text = """
<h2>ALT 2 The RichTextValue<a class="headerlink" href="#the-richtextvalue"
title="Permalink to this headline">¶</a></h2>
<p>The <code class="docutils literal"><span class="pre">RichText</span>
</code> field does not store a string. Instead, it stores a
<code class="docutils literal"><span class="pre">RichTextValue</span>
</code> object. This is an immutable object that has the
following properties:</p>
<dl class="docutils">
<dt><code class="docutils literal"><span class="pre">raw</span></code></dt>
<dd>a unicode string with the original input markup;</dd>
<dt><code class="docutils literal"><span class="pre">mimeType</span></code>
</dt>
<dd>the MIME type of the original markup, e.g.
<code class="docutils literal"><span class="pre">text/html</span></code> or
<code class="docutils literal"><span class="pre">text/structured</span>
</code>;</dd>
<dt><code class="docutils literal"><span class="pre">encoding</span></code>
</dt>
<dd>the default character encoding used when transforming the input markup.
Most likely, this will be UTF-8;</dd>
<dt><code class="docutils literal"><span class="pre">raw_encoded</span>
</code></dt>
<dd>the raw input encoded in the given encoding;</dd>
<dt><code class="docutils literal"><span class="pre">outputMimeType</span>
</code></dt>
<dd>the MIME type of the default output, taken from the field at the time of
instantiation;</dd>
<dt><code class="docutils literal"><span class="pre">output</span></code></dt>
<dd>a unicode object representing the transformed output. If possible, this
is cached persistently until the <code class="docutils literal">
<span class="pre">RichTextValue</span></code> is replaced with a
new one (as happens when an edit form is saved, for example).</dd>
</dl>
"""

bio_fr = RichTextValue(bio_fr_text, 'text/plain', 'text/html')
bio_alt1 = RichTextValue(bio_alt1_text, 'text/plain', 'text/html')
bio_alt2 = RichTextValue(bio_alt2_text, 'text/plain', 'text/html')

portraitA = {}
portraitA['family_name'] = u'Animal 1'
portraitA['first_name'] = u'Annesse 1'
portraitA['email'] = u'l.c@univ-brest.fr'
portraitA['image'] = u'1800-IMGA0212.JPG'
portraitA['img_author'] = u'Auth1'
portraitA['thumbnail'] = u'200-IMGA0212.JPG'
portraitA['bio_fr'] = bio_fr
portraitA['jobs'] = [u'plongeur', u'chercheur']
portraitA['status'] = u''
portraitA['affiliation1'] = u'CNRS'
portraitA['affiliation2'] = u'LEMAR'
portraitA['affiliation3'] = u'IUEM'
portraitA['personal_page'] = u'http://www.iuem.org/me'
portraitA['unit_page'] = u'http://www.iuem.org/unit'
portraitA['research'] = u'http://www.iuem.org/search'
portraitA['display_one'] = True
portraitA['presentation_one'] = bio_alt1
portraitA['display_two'] = True
portraitA['presentation_two'] = bio_alt2

portraitB = {}
portraitB['family_name'] = u'Animal 2'
portraitB['first_name'] = u'Annesse 2'
portraitB['email'] = u'la.A@canada.ca'
portraitB['image'] = u'1800-IMGA0214.JPG'
portraitB['img_author'] = u''
portraitB['thumbnail'] = u'200-IMGA0214.JPG'
portraitB['bio_fr'] = bio_fr
portraitB['jobs'] = [u'plongeur', u'chercheur']
portraitB['status'] = u'Chercheur'
portraitB['affiliation1'] = u'UQAR'
portraitB['affiliation2'] = u'CANADIAN Univ'
portraitB['affiliation3'] = u''
portraitB['personal_page'] = u'http://www.canada.ca/me'
portraitB['unit_page'] = u'http://www.canada.ca/myUnity'
portraitB['research'] = u'http://www.canada.ca/research'
portraitB['display_one'] = True
portraitB['presentation_one'] = bio_alt1
portraitB['display_two'] = False
portraitB['presentation_two'] = bio_alt2

portraitC = {}
portraitC['family_name'] = u'Animal 3'
portraitC['first_name'] = u'Annesse 3'
portraitC['email'] = u'e.a@iuem.org'
portraitC['image'] = u'1800-IMGA0215.JPG'
portraitC['img_author'] = u''
portraitC['thumbnail'] = u'200-IMGA0215.JPG'
portraitC['bio_fr'] = bio_fr
portraitC['jobs'] = [u'plongeur', u'photographe']
portraitC['status'] = u'Assistant ingénieur'
portraitC['affiliation1'] = u'CCNNRRSS'
portraitC['affiliation2'] = u'LEMAR'
portraitC['affiliation3'] = u''
portraitC['personal_page'] = u'http://www.cnrs.fr/me'
portraitC['unit_page'] = u'http://www.cnrs.fr/unit'
portraitC['research'] = u'http://www.cnrs.fr/search'
portraitC['display_one'] = True
portraitC['presentation_one'] = bio_alt1
portraitC['display_two'] = True
portraitC['presentation_two'] = bio_alt2

portraitD = {}
portraitD['family_name'] = u'Animal 4'
portraitD['first_name'] = u'Annesse 4'
portraitD['email'] = u'e.a@iuem.org'
portraitD['image'] = u'1800-IMGA0217.JPG'
portraitD['img_author'] = u''
portraitD['thumbnail'] = u'200-IMGA0217.JPG'
portraitD['bio_fr'] = bio_fr
portraitD['jobs'] = [u'plongeur', u'photographe']
portraitD['status'] = u'Assistant ingénieur'
portraitD['affiliation1'] = u'CCNNRRSS'
portraitD['affiliation2'] = u'LEMAR'
portraitD['affiliation3'] = u''
portraitD['personal_page'] = u'http://www.cnrs.fr/me'
portraitD['unit_page'] = u'http://www.cnrs.fr/unit'
portraitD['research'] = u'http://www.cnrs.fr/search'
portraitD['display_one'] = False
portraitD['presentation_one'] = bio_alt1
portraitD['display_two'] = True
portraitD['presentation_two'] = bio_alt2

portraitE = {}
portraitE['family_name'] = u'Animal 5'
portraitE['first_name'] = u'Annesse 5'
portraitE['email'] = u'e.a@iuem.org'
portraitE['image'] = u'1800-IMGA0220.JPG'
portraitE['img_author'] = u''
portraitE['thumbnail'] = u'200-IMGA0220.JPG'
portraitE['bio_fr'] = bio_fr
portraitE['jobs'] = [u'plongeur', u'photographe']
portraitE['status'] = u'Assistant ingénieur'
portraitE['affiliation1'] = u'CCNNRRSS'
portraitE['affiliation2'] = u'LEMAR'
portraitE['affiliation3'] = u''
portraitE['personal_page'] = u'http://www.cnrs.fr/me'
portraitE['unit_page'] = u'http://www.cnrs.fr/unit'
portraitE['research'] = u'http://www.cnrs.fr/search'
portraitE['display_one'] = True
portraitE['presentation_one'] = bio_alt1
portraitE['display_two'] = True
portraitE['presentation_two'] = bio_alt2

portraits = []
portraits.append(portraitA)
portraits.append(portraitB)
portraits.append(portraitC)
portraits.append(portraitD)
portraits.append(portraitE)
