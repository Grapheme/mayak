# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Consiliario'
        db.create_table('mayak_nucleum_consiliario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('specialization', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('ckeditor.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal('mayak_nucleum', ['Consiliario'])

        # Adding model 'Question'
        db.create_table('mayak_nucleum_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('consiliario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='question_list', to=orm['mayak_nucleum.Consiliario'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('message', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('answer', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('m_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('mayak_nucleum', ['Question'])


        # Changing field 'Hospes.text'
        db.alter_column('mayak_nucleum_hospes', 'text', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Programs.description'
        db.alter_column('mayak_nucleum_programs', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Programs.schedule'
        db.alter_column('mayak_nucleum_programs', 'schedule', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Programs.anons'
        db.alter_column('mayak_nucleum_programs', 'anons', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'ProgramsArchive.description'
        db.alter_column('mayak_nucleum_programsarchive', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Discussion.text'
        db.alter_column('mayak_nucleum_discussion', 'text', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Discussion.tiser'
        db.alter_column('mayak_nucleum_discussion', 'tiser', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'ProgramsPhoto.description'
        db.alter_column('mayak_nucleum_programsphoto', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'ProgramsArchivePhoto.description'
        db.alter_column('mayak_nucleum_programsarchivephoto', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Staff.text'
        db.alter_column('mayak_nucleum_staff', 'text', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):
        # Deleting model 'Consiliario'
        db.delete_table('mayak_nucleum_consiliario')

        # Deleting model 'Question'
        db.delete_table('mayak_nucleum_question')


        # Changing field 'Hospes.text'
        db.alter_column('mayak_nucleum_hospes', 'text', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Programs.description'
        db.alter_column('mayak_nucleum_programs', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Programs.schedule'
        db.alter_column('mayak_nucleum_programs', 'schedule', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Programs.anons'
        db.alter_column('mayak_nucleum_programs', 'anons', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ProgramsArchive.description'
        db.alter_column('mayak_nucleum_programsarchive', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Discussion.text'
        db.alter_column('mayak_nucleum_discussion', 'text', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Discussion.tiser'
        db.alter_column('mayak_nucleum_discussion', 'tiser', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ProgramsPhoto.description'
        db.alter_column('mayak_nucleum_programsphoto', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ProgramsArchivePhoto.description'
        db.alter_column('mayak_nucleum_programsarchivephoto', 'description', self.gf('tinymce.models.HTMLField')())

        # Changing field 'Staff.text'
        db.alter_column('mayak_nucleum_staff', 'text', self.gf('tinymce.models.HTMLField')())

    models = {
        'mayak_nucleum.consiliario': {
            'Meta': {'object_name': 'Consiliario'},
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mayak_nucleum.discussion': {
            'Meta': {'object_name': 'Discussion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'tiser': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mayak_nucleum.hospes': {
            'Meta': {'ordering': "('transmission', 'surname', 'name')", 'object_name': 'Hospes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
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
            'anons': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'display': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '21'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'staff'", 'blank': 'True', 'to': "orm['mayak_nucleum.Staff']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_nucleum.programsarchive': {
            'Meta': {'ordering': "('-date', '-time_s')", 'object_name': 'ProgramsArchive'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 29, 0, 0)'}),
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.Programs']"}),
            'soundcloud': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'time_e': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 5, 29, 0, 0)'}),
            'time_s': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime(2014, 5, 29, 0, 0)'})
        },
        'mayak_nucleum.programsarchivephoto': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'ProgramsArchivePhoto'},
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.ProgramsArchive']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_nucleum.programsphoto': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'ProgramsPhoto'},
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
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
        'mayak_nucleum.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'consiliario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'question_list'", 'to': "orm['mayak_nucleum.Consiliario']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'm_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'message': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['mayak_nucleum']