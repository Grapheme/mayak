# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.anons'
        db.add_column('shanson_news_news', 'anons',
                      self.gf('tinymce.models.HTMLField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'News.photo'
        db.alter_column('shanson_news_news', 'photo', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))

    def backwards(self, orm):
        # Deleting field 'News.anons'
        db.delete_column('shanson_news_news', 'anons')


        # Changing field 'News.photo'
        db.alter_column('shanson_news_news', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    models = {
        'shanson_news.news': {
            'Meta': {'ordering': "('-date', '-time')", 'object_name': 'News'},
            'anons': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['shanson_news']