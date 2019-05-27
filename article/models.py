from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
 
class article(models.Model):
    author = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length = 50,verbose_name="Başlık")
    content = RichTextField(verbose_name="Içerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    article_image = models.FileField(blank=True, null=True,verbose_name="Fotoğraf Ekleyin")
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.name = models.ForeignKey(article, related_name='comments', on_delete=models.CASCADE, verbose_name="Makale")
    comment_author =  models.CharField(max_length = 50,verbose_name= "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content



    
    