# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table('mayak_advertisers_action', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_s', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 26, 0, 0))),
            ('date_e', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 26, 0, 0))),
            ('anons', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Gallery'], null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('mayak_advertisers', ['Action'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table('mayak_advertisers_action')


    models = {
        'gallery.gallery': {
            'Meta': {'ordering': "('weight', '-id')", 'object_name': 'Gallery'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_advertisers.action': {
            'Meta': {'ordering': "('weight', 'date_s')", 'object_name': 'Action'},
            'anons': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'date_e': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 3, 26, 0, 0)'}),
            'date_s': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 3, 26, 0, 0)'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_advertisers.managers': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'Managers'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['mayak_advertisers']