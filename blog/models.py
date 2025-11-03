from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(
        upload_to='posts/%Y/%m/%d/', 
        null=True, 
        blank=True,
        verbose_name='이미지'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    class Meta:
        ordering = ['-created_at']
        verbose_name = '게시글'
        verbose_name_plural = '게시글 목록'

    def __str__(self):
        return self.title