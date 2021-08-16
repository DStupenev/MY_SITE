from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=150)
    article_text = models.TextField()
    publication_date = models.DateTimeField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=300)
