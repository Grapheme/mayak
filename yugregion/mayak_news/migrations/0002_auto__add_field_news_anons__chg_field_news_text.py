# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.anons'
        db.add_column('mayak_news_news', 'anons',
                      self.gf('ckeditor.fields.RichTextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'News.text'
        db.alter_column('mayak_news_news', 'text', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):
        # Deleting field 'News.anons'
        db.delete_column('mayak_news_news', 'anons')


        # Changing field 'News.text'
        db.alter_column('mayak_news_news', 'text', self.gf('tinymce.models.HTMLField')())

    models = {
        'mayak_news.news': {
            'Meta': {'ordering': "('-date', '-time')", 'object_name': 'News'},
            'anons': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mayak_news']