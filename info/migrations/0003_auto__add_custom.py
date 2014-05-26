# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Custom'
        db.create_table(u'info_custom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'info', ['Custom'])


    def backwards(self, orm):
        # Deleting model 'Custom'
        db.delete_table(u'info_custom')


    models = {
        u'info.custom': {
            'Meta': {'object_name': 'Custom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
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