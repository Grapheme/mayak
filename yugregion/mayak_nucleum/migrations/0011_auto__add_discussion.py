# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Discussion'
        db.create_table('mayak_nucleum_discussion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('mayak_nucleum', ['Discussion'])


    def backwards(self, orm):
        # Deleting model 'Discussion'
        db.delete_table('mayak_nucleum_discussion')


    models = {
        'mayak_nucleum.discussion': {
            'Meta': {'object_name': 'Discussion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mayak_nucleum.hospes': {
            'Meta': {'ordering': "('transmission', 'surname', 'name')", 'object_name': 'Hospes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'transmission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.ProgramsArchive']", 'null': 'True', 'blank': 'True'})
        },
        'mayak_nucleum.press': {
            'Meta': {'ordering': "('weight', '-id')", 'object_name': 'Press'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'magazine': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
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
        'mayak_nucleum.programsarchive': {
            'Meta': {'ordering': "('-date', '-time_s')", 'object_name': 'ProgramsArchive'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 9, 0, 0)'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.Programs']"}),
            'soundcloud': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'time_e': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 1, 9, 0, 0)'}),
            'time_s': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 1, 9, 0, 0)'})
        },
        'mayak_nucleum.programsarchivephoto': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'ProgramsArchivePhoto'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.ProgramsArchive']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_nucleum.programsphoto': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'ProgramsPhoto'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.Programs']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_nucleum.promo': {
            'Meta': {'ordering': "('weight', 'title')", 'object_name': 'Promo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.Programs']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
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
        }
    }

    complete_apps = ['mayak_nucleum']