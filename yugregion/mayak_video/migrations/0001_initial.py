# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table('mayak_video_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mayak_nucleum.Programs'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 3, 0, 0))),
            ('time_s', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2013, 10, 3, 0, 0))),
            ('time_e', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2013, 10, 3, 0, 0))),
            ('video', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('mayak_video', ['Video'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table('mayak_video_video')


    models = {
        'mayak_nucleum.programs': {
            'Meta': {'ordering': "('-display', 'weight')", 'object_name': 'Programs'},
            'anons': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'display': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '21'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'staff'", 'blank': 'True', 'to': "orm['mayak_nucleum.Staff']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_nucleum.staff': {
            'Meta': {'ordering': "('weight', 'surname', 'name')", 'object_name': 'Staff'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_t': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_min': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'programs'", 'blank': 'True', 'to': "orm['mayak_nucleum.Programs']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'surname_t': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_video.video': {
            'Meta': {'ordering': "['-date', '-time_s']", 'object_name': 'Video'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 10, 3, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.Programs']"}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'time_e': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2013, 10, 3, 0, 0)'}),
            'time_s': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2013, 10, 3, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mayak_video']