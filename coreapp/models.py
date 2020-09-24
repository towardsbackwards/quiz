from django.db import models


class CoreModel(models.Model):
    """ 'Ядро' всех моделей """
    class Meta:
        verbose_name = 'Базовая модель'
        verbose_name_plural = 'Базовые модели'
    title = models.CharField('Заголовок', max_length=256, blank=True, null=True)
    description = models.TextField('Описание', max_length=2048, blank=True, null=True)
    active = models.BooleanField('Активен ли объект', default=True, db_index=True)

    def inactive(self):
        self.active = False
        self.save()

    def __str__(self):
        return f'{self.title}'


class ImageModel(models.Model):
    """ Связанные изображения для каждой модели """
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField(upload_to='static/images')
    related_obj = models.ForeignKey(CoreModel, verbose_name='images',
                                    related_name='images', on_delete=models.CASCADE)
