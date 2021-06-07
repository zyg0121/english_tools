# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Instance(models.Model):
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
    sentence = models.ForeignKey('Sentence', on_delete=models.CASCADE)

    class Meta:
        # managed = False
        db_table = 'Instance'


class Sentence(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    sentence = models.CharField(unique=True, max_length=255, verbose_name="句子内容")
    translation = models.CharField(max_length=255, blank=True, null=True, verbose_name="句子翻译")

    def __str__(self):
        return self.sentence

    class Meta:
        managed = False
        db_table = 'sentence'
        verbose_name = u'句子内容'
        verbose_name_plural = u'句子管理'


class Translate(models.Model):
    word = models.ForeignKey('Word', models.DO_NOTHING)
    trans = models.ForeignKey('Translation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'translate'


class Translation(models.Model):
    trans_id = models.AutoField(primary_key=True)
    property = models.CharField(max_length=10, blank=True, null=True, verbose_name="单词词性")
    translation = models.CharField(max_length=100, verbose_name="单词含义")

    def __str__(self):
        return self.property+" "+self.translation

    class Meta:
        managed = False
        db_table = 'translation'
        verbose_name = u'词汇翻译'
        verbose_name_plural = u'词汇翻译管理'


class Word(models.Model):
    WORD_LEVEL_CHOICE = [
        ('', '空'),
        ('level_1', '等级一'),
        ('level_2', '等级二'),
        ('level_3', '等级三'),
        ('level_4', '等级四'),
        ('level_5', '等级五'),
    ]

    word_id = models.AutoField(primary_key=True)
    word = models.CharField(unique=True, max_length=40, verbose_name="单词名称")
    levels = models.CharField(max_length=10, blank=True, null=True, choices=WORD_LEVEL_CHOICE, verbose_name="单词等级")

    sentences = models.ManyToManyField(Sentence, through="Instance")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = u'单词'
        verbose_name_plural = u'单词管理'
        managed = False
        db_table = 'word'
