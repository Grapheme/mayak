# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProgramsArchive'
        db.create_table('shanson_nucleum_programsarchive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shanson_nucleum.Programs'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 4, 11, 0, 0))),
            ('time_s', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2013, 4, 11, 0, 0))),
            ('time_e', self.gf('django.db.models.fields.TimeField')(default=datetime.datetime(2013, 4, 11, 0, 0))),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('soundcloud', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('shanson_nucleum', ['ProgramsArchive'])

        # Adding model 'ProgramsArchivePhoto'
        db.create_table('shanson_nucleum_programsarchivephoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shanson_nucleum.ProgramsArchive'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('shanson_nucleum', ['ProgramsArchivePhoto'])


    def backwards(self, orm):
        # Deleting model 'ProgramsArchive'
        db.delete_table('shanson_nucleum_programsarchive')

        # Deleting model 'ProgramsArchivePhoto'
        db.delete_table('shanson_nucleum_programsarchivephoto')


    models = {
        'shanson_nucleum.press': {
            'Meta': {'ordering': "('weight', '-id')", 'object_name': 'Press'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'magazine': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.programs': {
            'Meta': {'ordering': "('-display', 'title')", 'object_name': 'Programs'},
            'anons': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'display': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '21'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'staff'", 'blank': 'True', 'to': "orm['shanson_nucleum.Staff']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.programsarchive': {
            'Meta': {'ordering': "('date', 'time_s')", 'object_name': 'ProgramsArchive'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 4, 11, 0, 0)'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shanson_nucleum.Programs']"}),
            'soundcloud': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time_e': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2013, 4, 11, 0, 0)'}),
            'time_s': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2013, 4, 11, 0, 0)'})
        },
        'shanson_nucleum.programsarchivephoto': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'ProgramsArchivePhoto'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shanson_nucleum.ProgramsArchive']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.programsphoto': {
            'Meta': {'object_name': 'ProgramsPhoto'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shanson_nucleum.Programs']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.promo': {
            'Meta': {'ordering': "('weight', 'title')", 'object_name': 'Promo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shanson_nucleum.Programs']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.staff': {
            'Meta': {'ordering': "('surname', 'name')", 'object_name': 'Staff'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name_t': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_min': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'programs'", 'blank': 'True', 'to': "orm['shanson_nucleum.Programs']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'surname_t': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['shanson_nucleum']