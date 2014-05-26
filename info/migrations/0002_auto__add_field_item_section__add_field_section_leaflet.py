# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.section'
        db.add_column(u'info_item', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['info.Section']),
                      keep_default=False)

        # Adding field 'Section.leaflet'
        db.add_column(u'info_section', 'leaflet',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['info.Leaflet']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.section'
        db.delete_column(u'info_item', 'section_id')

        # Deleting field 'Section.leaflet'
        db.delete_column(u'info_section', 'leaflet_id')


    models = {
        u'info.item': {
            'Meta': {'object_name': 'Item'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['info.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'info.leaflet': {
            'Meta': {'object_name': 'Leaflet'},
            'email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_QR': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url_QR': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'info.section': {
            'Meta': {'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaflet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['info.Leaflet']"}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['info']