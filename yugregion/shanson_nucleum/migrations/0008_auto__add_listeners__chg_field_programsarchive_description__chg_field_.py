# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Listeners'
        db.create_table('shanson_nucleum_listeners', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('m_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('shanson_nucleum', ['Listeners'])


        # Changing field 'ProgramsArchive.description'
        db.alter_column('shanson_nucleum_programsarchive', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Programs.description'
        db.alter_column('shanson_nucleum_programs', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Programs.schedule'
        db.alter_column('shanson_nucleum_programs', 'schedule', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Programs.anons'
        db.alter_column('shanson_nucleum_programs', 'anons', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'ProgramsPhoto.description'
        db.alter_column('shanson_nucleum_programsphoto', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Staff.text'
        db.alter_column('shanson_nucleum_staff', 'text', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'ProgramsArchivePhoto.description'
        db.alter_column('shanson_nucleum_programsarchivephoto', 'description', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):
        # Deleting model 'Listeners'
        db.delete_table('shanson_nucleum_listeners')


        # Changing field 'ProgramsArchive.description'
        db.alter_column('shanson_nucleum_programsarchive', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Programs.description'
        db.alter_column('shanson_nucleum_programs', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Programs.schedule'
        db.alter_column('shanson_nucleum_programs', 'schedule', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Programs.anons'
        db.alter_column('shanson_nucleum_programs', 'anons', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ProgramsPhoto.description'
        db.alter_column('shanson_nucleum_programsphoto', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Staff.text'
        db.alter_column('shanson_nucleum_staff', 'text', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ProgramsArchivePhoto.description'
        db.alter_column('shanson_nucleum_programsarchivephoto', 'description', self.gf('tinymce.models.HTMLField')())

    models = {
        'shanson_nucleum.listeners': {
            'Meta': {'ordering': "('-m_time',)", 'object_name': 'Listeners'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'm_time': ('django.db.models.fields.DateTimeField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
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
            'anons': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'display': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '21'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'staff'", 'blank': 'True', 'to': "orm['shanson_nucleum.Staff']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.programsarchive': {
            'Meta': {'ordering': "('-date', '-time_s')", 'object_name': 'ProgramsArchive'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 5, 0, 0)'}),
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shanson_nucleum.Programs']"}),
            'soundcloud': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time_e': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 6, 5, 0, 0)'}),
            'time_s': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 6, 5, 0, 0)'})
        },
        'shanson_nucleum.programsarchivephoto': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'ProgramsArchivePhoto'},
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shanson_nucleum.ProgramsArchive']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.programsphoto': {
            'Meta': {'object_name': 'ProgramsPhoto'},
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'weight': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'shanson_nucleum.staff': {
            'Meta': {'ordering': "('weight', 'surname', 'name')", 'object_name': 'Staff'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_t': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_min': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'programs'", 'blank': 'True', 'to': "orm['shanson_nucleum.Programs']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'surname_t': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['shanson_nucleum']