# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubjectConsultation'
        db.create_table('mayak_nucleum_subjectconsultation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal('mayak_nucleum', ['SubjectConsultation'])

        # Deleting field 'Consiliario.specialization'
        db.delete_column('mayak_nucleum_consiliario', 'specialization')

        # Adding field 'Consiliario.subject'
        db.add_column('mayak_nucleum_consiliario', 'subject',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='consiliario_list', to=orm['mayak_nucleum.SubjectConsultation']),
                      keep_default=False)


        # Changing field 'Question.message'
        db.alter_column('mayak_nucleum_question', 'message', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting model 'SubjectConsultation'
        db.delete_table('mayak_nucleum_subjectconsultation')

        # Adding field 'Consiliario.specialization'
        db.add_column('mayak_nucleum_consiliario', 'specialization',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Deleting field 'Consiliario.subject'
        db.delete_column('mayak_nucleum_consiliario', 'subject_id')


        # Changing field 'Question.message'
        db.alter_column('mayak_nucleum_question', 'message', self.gf('ckeditor.fields.RichTextField')())

    models = {
        'mayak_nucleum.consiliario': {
            'Meta': {'object_name': 'Consiliario'},
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_min': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'consiliario_list'", 'to': "orm['mayak_nucleum.SubjectConsultation']"})
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
            'Meta': {'ordering': "['-m_time']", 'object_name': 'Question'},
            'answer': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'consiliario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'question_list'", 'to': "orm['mayak_nucleum.Consiliario']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'm_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
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
        },
        'mayak_nucleum.subjectconsultation': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'SubjectConsultation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mayak_nucleum']