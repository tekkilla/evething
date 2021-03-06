# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CharacterDetails.clone_name'
        db.delete_column(u'thing_characterdetails', 'clone_name')

        # Deleting field 'CharacterDetails.clone_skill_points'
        db.delete_column(u'thing_characterdetails', 'clone_skill_points')


    def backwards(self, orm):
        # Adding field 'CharacterDetails.clone_name'
        db.add_column(u'thing_characterdetails', 'clone_name',
                      self.gf('django.db.models.fields.CharField')(default='Clone Grade Alpha', max_length=32),
                      keep_default=False)

        # Adding field 'CharacterDetails.clone_skill_points'
        db.add_column(u'thing_characterdetails', 'clone_skill_points',
                      self.gf('django.db.models.fields.IntegerField')(default=900000),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'thing.alliance': {
            'Meta': {'object_name': 'Alliance'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'thing.apikey': {
            'Meta': {'ordering': "('keyid',)", 'object_name': 'APIKey'},
            'access_mask': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'apikeyinfo_errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'apikeys'", 'symmetrical': 'False', 'to': "orm['thing.Character']"}),
            'corp_character': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'corporate_apikey'", 'null': 'True', 'to': "orm['thing.Character']"}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            'keyid': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'needs_apikeyinfo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'override_mask': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'paid_until': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'vcode': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.apikeyfailure': {
            'Meta': {'object_name': 'APIKeyFailure'},
            'fail_reason': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fail_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyid': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'thing.asset': {
            'Meta': {'object_name': 'Asset'},
            'asset_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'corporation_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inv_flag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.InventoryFlag']"}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'parent': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'raw_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'singleton': ('django.db.models.fields.BooleanField', [], {}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Station']", 'null': 'True', 'blank': 'True'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.System']"})
        },
        'thing.assetsummary': {
            'Meta': {'object_name': 'AssetSummary'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'corporation_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Station']", 'null': 'True', 'blank': 'True'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.System']"}),
            'total_items': ('django.db.models.fields.BigIntegerField', [], {}),
            'total_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'total_volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        'thing.blueprint': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Blueprint'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'productionLimit': ('django.db.models.fields.IntegerField', [], {})
        },
        'thing.blueprintcomponent': {
            'Meta': {'object_name': 'BlueprintComponent'},
            'activity': ('django.db.models.fields.IntegerField', [], {}),
            'blueprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Blueprint']"}),
            'consumed': ('django.db.models.fields.BooleanField', [], {}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Item']"})
        },
        'thing.blueprintinstance': {
            'Meta': {'ordering': "('blueprint',)", 'object_name': 'BlueprintInstance'},
            'blueprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Blueprint']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'original': ('django.db.models.fields.BooleanField', [], {}),
            'productivity_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'thing.blueprintproduct': {
            'Meta': {'object_name': 'BlueprintProduct'},
            'activity': ('django.db.models.fields.IntegerField', [], {}),
            'blueprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Blueprint']"}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Item']"})
        },
        'thing.campaign': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Campaign'},
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['thing.Character']", 'null': 'True', 'blank': 'True'}),
            'corp_wallets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['thing.CorpWallet']", 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'thing.character': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Character'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.characterconfig': {
            'Meta': {'object_name': 'CharacterConfig'},
            'anon_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'}),
            'character': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'config'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['thing.Character']"}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_clone': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_implants': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_skill_queue': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_standings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_wallet': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'thing.characterdetails': {
            'Meta': {'object_name': 'CharacterDetails'},
            'cha_attribute': ('django.db.models.fields.SmallIntegerField', [], {'default': '20'}),
            'character': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'details'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['thing.Character']"}),
            'implants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['thing.Implant']", 'symmetrical': 'False'}),
            'int_attribute': ('django.db.models.fields.SmallIntegerField', [], {'default': '20'}),
            'last_known_location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'mem_attribute': ('django.db.models.fields.SmallIntegerField', [], {'default': '20'}),
            'per_attribute': ('django.db.models.fields.SmallIntegerField', [], {'default': '20'}),
            'security_status': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '4'}),
            'ship_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Item']", 'null': 'True', 'blank': 'True'}),
            'ship_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128'}),
            'wallet_balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '18', 'decimal_places': '2'}),
            'wil_attribute': ('django.db.models.fields.SmallIntegerField', [], {'default': '19'})
        },
        'thing.characterskill': {
            'Meta': {'object_name': 'CharacterSkill'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.SmallIntegerField', [], {}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Skill']"})
        },
        'thing.colony': {
            'Meta': {'unique_together': "(('character', 'planet_id'),)", 'object_name': 'Colony'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'pins': ('django.db.models.fields.IntegerField', [], {}),
            'planet': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'planet_id': ('django.db.models.fields.IntegerField', [], {}),
            'planet_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.System']"})
        },
        'thing.constellation': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Constellation'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Region']"})
        },
        'thing.contract': {
            'Meta': {'ordering': "('-date_issued',)", 'object_name': 'Contract'},
            'acceptor_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'assignee_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'buyout': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'collateral': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'contract_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']", 'null': 'True', 'blank': 'True'}),
            'date_accepted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_expired': ('django.db.models.fields.DateTimeField', [], {}),
            'date_issued': ('django.db.models.fields.DateTimeField', [], {}),
            'end_station': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['thing.Station']"}),
            'for_corp': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer_char': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['thing.Character']"}),
            'issuer_corp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['thing.Corporation']"}),
            'num_days': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'public': ('django.db.models.fields.BooleanField', [], {}),
            'retrieved_items': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reward': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'start_station': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['thing.Station']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '4'})
        },
        'thing.contractitem': {
            'Meta': {'object_name': 'ContractItem'},
            'contract_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included': ('django.db.models.fields.BooleanField', [], {}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contract_items'", 'to': "orm['thing.Item']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'raw_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'singleton': ('django.db.models.fields.BooleanField', [], {})
        },
        'thing.corporation': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Corporation'},
            'alliance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Alliance']", 'null': 'True', 'blank': 'True'}),
            'division1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'division2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'division3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'division4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'division5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'division6': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'division7': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ticker': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'})
        },
        'thing.corporationstanding': {
            'Meta': {'ordering': "('-standing',)", 'object_name': 'CorporationStanding'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'standing': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        'thing.corpwallet': {
            'Meta': {'ordering': "('corporation', 'account_id')", 'object_name': 'CorpWallet'},
            'account_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'account_key': ('django.db.models.fields.IntegerField', [], {}),
            'balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.event': {
            'Meta': {'ordering': "('-issued', '-id')", 'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'thing.faction': {
            'Meta': {'object_name': 'Faction'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.factionstanding': {
            'Meta': {'ordering': "('-standing',)", 'object_name': 'FactionStanding'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'faction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Faction']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'standing': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        'thing.implant': {
            'Meta': {'object_name': 'Implant'},
            'charisma_modifier': ('django.db.models.fields.SmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'implant_slot': ('django.db.models.fields.SmallIntegerField', [], {}),
            'intelligence_modifier': ('django.db.models.fields.SmallIntegerField', [], {}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['thing.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'memory_modifier': ('django.db.models.fields.SmallIntegerField', [], {}),
            'perception_modifier': ('django.db.models.fields.SmallIntegerField', [], {}),
            'willpower_modifier': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'thing.industryjob': {
            'Meta': {'ordering': "('-end_date',)", 'object_name': 'IndustryJob'},
            'activity': ('django.db.models.fields.IntegerField', [], {}),
            'blueprint': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_installed_blueprints'", 'to': "orm['thing.Blueprint']"}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'completed_date': ('django.db.models.fields.DateTimeField', [], {}),
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']", 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installer_id': ('django.db.models.fields.IntegerField', [], {}),
            'job_id': ('django.db.models.fields.IntegerField', [], {}),
            'licensed_runs': ('django.db.models.fields.IntegerField', [], {}),
            'output_location_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'pause_date': ('django.db.models.fields.DateTimeField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_products'", 'null': 'True', 'to': "orm['thing.Item']"}),
            'runs': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.System']"}),
            'team_id': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'thing.inventoryflag': {
            'Meta': {'object_name': 'InventoryFlag'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'thing.item': {
            'Meta': {'object_name': 'Item'},
            'base_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2'}),
            'buy_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.ItemGroup']"}),
            'market_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.MarketGroup']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'portion_size': ('django.db.models.fields.IntegerField', [], {}),
            'sell_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '4'})
        },
        'thing.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.itemgroup': {
            'Meta': {'object_name': 'ItemGroup'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.ItemCategory']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.journalentry': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'JournalEntry'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'arg_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'arg_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '17', 'decimal_places': '2'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'corp_wallet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.CorpWallet']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner1_id': ('django.db.models.fields.IntegerField', [], {}),
            'owner2_id': ('django.db.models.fields.IntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ref_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'ref_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.RefType']"}),
            'tax_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'tax_corp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']", 'null': 'True', 'blank': 'True'})
        },
        'thing.mailinglist': {
            'Meta': {'object_name': 'MailingList'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'thing.mailmessage': {
            'Meta': {'ordering': "('-sent_date',)", 'object_name': 'MailMessage'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender_id': ('django.db.models.fields.IntegerField', [], {}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_characters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': "orm['thing.Character']"}),
            'to_corp_or_alliance_id': ('django.db.models.fields.IntegerField', [], {}),
            'to_list_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'thing.marketgroup': {
            'Meta': {'object_name': 'MarketGroup'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['thing.MarketGroup']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'thing.marketorder': {
            'Meta': {'ordering': "('buy_order', 'item__name')", 'object_name': 'MarketOrder'},
            'buy_order': ('django.db.models.fields.BooleanField', [], {}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'corp_wallet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.CorpWallet']", 'null': 'True', 'blank': 'True'}),
            'creator_character_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'escrow': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'issued': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Item']"}),
            'minimum_volume': ('django.db.models.fields.IntegerField', [], {}),
            'order_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Station']"}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '17', 'decimal_places': '2'}),
            'volume_entered': ('django.db.models.fields.IntegerField', [], {}),
            'volume_remaining': ('django.db.models.fields.IntegerField', [], {})
        },
        'thing.pin': {
            'Meta': {'object_name': 'Pin'},
            'colony': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Colony']"}),
            'content_size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '16', 'decimal_places': '4'}),
            'cycle_time': ('django.db.models.fields.IntegerField', [], {}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installed': ('django.db.models.fields.DateTimeField', [], {}),
            'last_launched': ('django.db.models.fields.DateTimeField', [], {}),
            'pin_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'quantity_per_cycle': ('django.db.models.fields.IntegerField', [], {}),
            'schematic': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['thing.Item']"})
        },
        'thing.pincontent': {
            'Meta': {'object_name': 'PinContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['thing.Item']"}),
            'pin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Pin']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'thing.pricehistory': {
            'Meta': {'ordering': "('-date',)", 'unique_together': "(('region', 'item', 'date'),)", 'object_name': 'PriceHistory'},
            'average': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Item']"}),
            'maximum': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'minimum': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '2'}),
            'movement': ('django.db.models.fields.BigIntegerField', [], {}),
            'orders': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Region']"})
        },
        'thing.reftype': {
            'Meta': {'object_name': 'RefType'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.region': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Region'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'thing.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['thing.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'primary_attribute': ('django.db.models.fields.SmallIntegerField', [], {}),
            'rank': ('django.db.models.fields.SmallIntegerField', [], {}),
            'secondary_attribute': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'thing.skillplan': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SkillPlan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'visibility': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'thing.skillqueue': {
            'Meta': {'ordering': "('start_time',)", 'object_name': 'SkillQueue'},
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'end_sp': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Skill']"}),
            'start_sp': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'to_level': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'thing.spentry': {
            'Meta': {'ordering': "('position',)", 'object_name': 'SPEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'skill_plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['thing.SkillPlan']"}),
            'sp_remap': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.SPRemap']", 'null': 'True', 'blank': 'True'}),
            'sp_skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.SPSkill']", 'null': 'True', 'blank': 'True'})
        },
        'thing.spremap': {
            'Meta': {'object_name': 'SPRemap'},
            'cha_stat': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int_stat': ('django.db.models.fields.IntegerField', [], {}),
            'mem_stat': ('django.db.models.fields.IntegerField', [], {}),
            'per_stat': ('django.db.models.fields.IntegerField', [], {}),
            'wil_stat': ('django.db.models.fields.IntegerField', [], {})
        },
        'thing.spskill': {
            'Meta': {'object_name': 'SPSkill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Skill']"})
        },
        'thing.station': {
            'Meta': {'object_name': 'Station'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'short_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.System']"})
        },
        'thing.system': {
            'Meta': {'ordering': "('name',)", 'object_name': 'System'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Constellation']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'thing.taskstate': {
            'Meta': {'object_name': 'TaskState'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyid': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'mod_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'next_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'parameter': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '64', 'db_index': 'True'})
        },
        'thing.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'buy_transaction': ('django.db.models.fields.BooleanField', [], {}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Character']"}),
            'corp_wallet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.CorpWallet']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Item']"}),
            'other_char': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'transaction_others'", 'null': 'True', 'to': "orm['thing.Character']"}),
            'other_corp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Corporation']", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['thing.Station']"}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '17', 'decimal_places': '2'}),
            'transaction_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'})
        },
        'thing.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'can_add_keys': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'entries_per_page': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'home_chars_per_row': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'home_hide_characters': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'home_highlight_backgrounds': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_highlight_borders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_show_locations': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_show_security': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_show_separators': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_sort_descending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_sort_order': ('django.db.models.fields.CharField', [], {'default': "'apiname'", 'max_length': '12'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'show_assets': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_blueprints': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_clock': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_contracts': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_industry': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_item_icons': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_orders': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_pi': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_trade': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_transactions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_wallet_journal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '32'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['thing']