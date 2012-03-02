# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Confirm.date'
        db.add_column('emails_confirm', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2012, 3, 1), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Confirm.date'
        db.delete_column('emails_confirm', 'date')


    models = {
        'emails.confirm': {
            'Meta': {'object_name': 'Confirm'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_ids': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['emails.Email']", 'symmetrical': 'False'}),
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'primary_key': 'True'})
        },
        'emails.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'email_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'to_email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'to_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'primary_key': 'True'})
        }
    }

    complete_apps = ['emails']
