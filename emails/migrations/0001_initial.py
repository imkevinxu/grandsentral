# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Email'
        db.create_table('emails_email', (
            ('from_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('from_email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('to_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('to_email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('email_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('unique_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16, primary_key=True)),
        ))
        db.send_create_signal('emails', ['Email'])


    def backwards(self, orm):
        
        # Deleting model 'Email'
        db.delete_table('emails_email')


    models = {
        'emails.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'email_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'to_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'primary_key': 'True'})
        }
    }

    complete_apps = ['emails']
