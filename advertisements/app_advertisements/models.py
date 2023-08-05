from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):
    # Товар
    # Строковое поле небольших размеров
    # 'Заголовок' - verbouse_name - название поля извне
    title = models.CharField('Заголовок', max_length=128)

    # Инофрмация о товаре
    # Большое текствовое поле
    description = models.TextField('Описание')

    # Имя продовца + контакты

    # Цена
    # Специальный тип данных с фикс. точкой
    price = models.DecimalField('Цена', max_digits=10,decimal_places=2)

    # Дата публикации
    # Поле записывается при создании обьявления
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения
    # Поле меняется при каждом обновлении
    updated_at = models.DateTimeField(auto_now=True)

    # Состояние обьявления(продано или нет)

    # Колличество товара

    # Уместен ли торг
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')

    # Возможен ли обмен

    # Адрес продажи

    # Б/У товар или нет

    @admin.display(description = 'Дата создания')
    def created_date(self):
            from django.utils import timezone
            if self.created_at.date() == timezone.now().date():
                created_date = self.created_at.strftime("%H:%M:%S")
                return format_html('<span style="color:green; font-weight:bold;">Сегодня в {} </span>', created_date)
            return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>"

    class Meta:
        db_table = "advertisements"

    @admin.display(description = 'Дата изменения')
    def updated_date(self):
            from django.utils import timezone
            if self.updated_at.date() == timezone.now().date():
                updated_date = self.updated_at.strftime("%H:%M:%S")
                return format_html('<span style="color:red; font-weight:bold;">Сегодня в {} </span>', updated_date)
            return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")


