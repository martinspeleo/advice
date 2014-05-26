# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Leaflet'
        db.create_table('info_leaflet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url_QR', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('long_QR', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('text', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('info', ['Leaflet'])

        # Adding model 'Section'
        db.create_table('info_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('info', ['Section'])

        # Adding model 'Item'
        db.create_table('info_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('info', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Leaflet'
        db.delete_table('info_leaflet')

        # Deleting model 'Section'
        db.delete_table('info_section')

        # Deleting model 'Item'
        db.delete_table('info_item')


    models = {
        'info.item': {
            'Meta': {'object_name': 'Item'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'info.leaflet': {
            'Meta': {'object_name': 'Leaflet'},
            'email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_QR': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'url_QR': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'info.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['info']