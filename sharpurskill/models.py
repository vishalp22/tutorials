from django.db import models


# Create your models here.

class Main_Category(models.Model):
    main_topic = models.CharField(max_length=200)

    def __str__(self):
        return self.main_topic


class Sub_Category(models.Model):
    sub_topic = models.ForeignKey(Main_Category)
    Sub_topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.Sub_topic_name


class Course_Types(models.Model):
    sub_sub_topic = models.ManyToManyField(Sub_Category)
    sub_sub_catogery = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_sub_catogery


class Course(models.Model):
    main_topic = models.ForeignKey(Main_Category)
    Sub_Topic = models.ManyToManyField(Sub_Category)
    course_type = models.ForeignKey(Course_Types)
    Course_title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)

    def __str__(self):
        return self.Course_title
