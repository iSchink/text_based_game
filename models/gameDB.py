# -*- coding: utf-8 -*-
db.define_table('Story',
                Field('Textteil', 'text', requires = IS_NOT_EMPTY()),
                Field('Antwort1'),
                Field ('Konsequenz1', 'integer'),
                Field ('Antwort2'),
                Field('Konsequenz2', 'integer'),
                )
