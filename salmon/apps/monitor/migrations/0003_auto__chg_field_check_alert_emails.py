# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Check.alert_emails'
        db.alter_column(u'monitor_check', 'alert_emails', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    def backwards(self, orm):

        # Changing field 'Check.alert_emails'
        db.alter_column(u'monitor_check', 'alert_emails', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        u'monitor.check': {
            'Meta': {'object_name': 'Check'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alert_emails': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'monitor.minion': {
            'Meta': {'object_name': 'Minion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'monitor.result': {
            'Meta': {'object_name': 'Result'},
            'check': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Check']"}),
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Minion']"}),
            'notified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'result': ('django.db.models.fields.TextField', [], {}),
            'result_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['monitor']