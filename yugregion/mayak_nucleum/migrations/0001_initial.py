# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hospes'
        db.create_table('mayak_nucleum_hospes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 6, 0, 0))),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mayak_nucleum.Programs'])),
        ))
        db.send_create_signal('mayak_nucleum', ['Hospes'])

        # Adding model 'Programs'
        db.create_table('mayak_nucleum_programs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('anons', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('schedule', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('display', self.gf('django.db.models.fields.CharField')(default='main', max_length=21)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('mayak_nucleum', ['Programs'])

        # Adding M2M table for field staff on 'Programs'
        db.create_table('Proxy_Mayak_Staff_Programs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programs', models.ForeignKey(orm['mayak_nucleum.programs'], null=False)),
            ('staff', models.ForeignKey(orm['mayak_nucleum.staff'], null=False))
        ))
        db.create_unique('Proxy_Mayak_Staff_Programs', ['programs_id', 'staff_id'])

        # Adding model 'ProgramsPhoto'
        db.create_table('mayak_nucleum_programsphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mayak_nucleum.Programs'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('mayak_nucleum', ['ProgramsPhoto'])

        # Adding model 'Staff'
        db.create_table('mayak_nucleum_staff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('name_t', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname_t', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo_min', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('text', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal('mayak_nucleum', ['Staff'])

        # Adding M2M table for field programs on 'Staff'
        # db.create_table('Proxy_Mayak_Staff_Programs', (
        #     ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
        #     ('staff', models.ForeignKey(orm['mayak_nucleum.staff'], null=False)),
        #     ('programs', models.ForeignKey(orm['mayak_nucleum.programs'], null=False))
        # ))
        # db.create_unique('Proxy_Mayak_Staff_Programs', ['staff_id', 'programs_id'])


    def backwards(self, orm):
        # Deleting model 'Hospes'
        db.delete_table('mayak_nucleum_hospes')

        # Deleting model 'Programs'
        db.delete_table('mayak_nucleum_programs')

        # Removing M2M table for field staff on 'Programs'
        db.delete_table('Proxy_Mayak_Staff_Programs')

        # Deleting model 'ProgramsPhoto'
        db.delete_table('mayak_nucleum_programsphoto')

        # Deleting model 'Staff'
        db.delete_table('mayak_nucleum_staff')

        # Removing M2M table for field programs on 'Staff'
        db.delete_table('Proxy_Mayak_Staff_Programs')


    models = {
        'mayak_nucleum.hospes': {
            'Meta': {'ordering': "('date', 'surname', 'name')", 'object_name': 'Hospes'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 3, 6, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.Programs']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        },
        'mayak_nucleum.programs': {
            'Meta': {'ordering': "('-display', 'title')", 'object_name': 'Programs'},
            'anons': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'display': ('django.db.models.fields.CharField', [], {'default': "'main'", 'max_length': '21'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'schedule': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'staff'", 'blank': 'True', 'to': "orm['mayak_nucleum.Staff']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_nucleum.programsphoto': {
            'Meta': {'object_name': 'ProgramsPhoto'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mayak_nucleum.Programs']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'mayak_nucleum.staff': {
            'Meta': {'ordering': "('surname', 'name')", 'object_name': 'Staff'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name_t': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo_min': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'programs'", 'blank': 'True', 'to': "orm['mayak_nucleum.Programs']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'surname_t': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'text': ('tinymce.models.HTMLField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['mayak_nucleum']