# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubjectConsultation'
        db.create_table('mayak_consultation_subjectconsultation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal('mayak_consultation', ['SubjectConsultation'])

        # Adding model 'Consiliario'
        db.create_table('mayak_consultation_consiliario', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='consiliario_list', to=orm['mayak_consultation.SubjectConsultation'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo_min', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('is_archive', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('mayak_consultation', ['Consiliario'])

        # Adding model 'Question'
        db.create_table('mayak_consultation_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('consiliario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='question_list', to=orm['mayak_consultation.Consiliario'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('m_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('mayak_consultation', ['Question'])


    def backwards(self, orm):
        # Deleting model 'SubjectConsultation'
        db.delete_table('mayak_consultation_subjectconsultation')

        # Deleting model 'Consiliario'
        db.delete_table('mayak_consultation_consiliario')

        # Deleting model 'Question'
        db.delete_table('mayak_consultation_question')


    models = {
        'mayak_consultation.consiliario': {
            'Meta': {'object_name': 'Consiliario'},
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_archive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_min': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'consiliario_list'", 'to': "orm['mayak_consultation.SubjectConsultation']"})
        },
        'mayak_consultation.question': {
            'Meta': {'ordering': "['-m_time']", 'object_name': 'Question'},
            'answer': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'consiliario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'question_list'", 'to': "orm['mayak_consultation.Consiliario']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'm_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mayak_consultation.subjectconsultation': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'SubjectConsultation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mayak_consultation']