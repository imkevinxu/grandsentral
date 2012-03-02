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
            ('uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16, primary_key=True)),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('emails', ['Email'])

        # Adding model 'Confirm'
        db.create_table('emails_confirm', (
            ('uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16, primary_key=True)),
        ))
        db.send_create_signal('emails', ['Confirm'])

        # Adding M2M table for field email_ids on 'Confirm'
        db.create_table('emails_confirm_email_ids', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('confirm', models.ForeignKey(orm['emails.confirm'], null=False)),
            ('email', models.ForeignKey(orm['emails.email'], null=False))
        ))
        db.create_unique('emails_confirm_email_ids', ['confirm_id', 'email_id'])


    def backwards(self, orm):
        
        # Deleting model 'Email'
        db.delete_table('emails_email')

        # Deleting model 'Confirm'
        db.delete_table('emails_confirm')

        # Removing M2M table for field email_ids on 'Confirm'
        db.delete_table('emails_confirm_email_ids')


    models = {
        'emails.confirm': {
            'Meta': {'object_name': 'Confirm'},
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
