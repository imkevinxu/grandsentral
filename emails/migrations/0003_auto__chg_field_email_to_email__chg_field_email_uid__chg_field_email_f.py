# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Email.to_email'
        db.alter_column('emails_email', 'to_email', self.gf('django.db.models.fields.EmailField')(max_length=75))

        # Changing field 'Email.uid'
        db.alter_column('emails_email', 'uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32, primary_key=True))

        # Changing field 'Email.from_email'
        db.alter_column('emails_email', 'from_email', self.gf('django.db.models.fields.EmailField')(max_length=75))

        # Changing field 'Confirm.uid'
        db.alter_column('emails_confirm', 'uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32, primary_key=True))


    def backwards(self, orm):
        
        # Changing field 'Email.to_email'
        db.alter_column('emails_email', 'to_email', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Email.uid'
        db.alter_column('emails_email', 'uid', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True, primary_key=True))

        # Changing field 'Email.from_email'
        db.alter_column('emails_email', 'from_email', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Confirm.uid'
        db.alter_column('emails_confirm', 'uid', self.gf('django.db.models.fields.CharField')(max_length=16, unique=True, primary_key=True))


    models = {
        'emails.confirm': {
            'Meta': {'object_name': 'Confirm'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'emails': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emails.Email']", 'symmetrical': 'False'}),
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'})
        },
        'emails.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'to_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'})
        }
    }

    complete_apps = ['emails']
