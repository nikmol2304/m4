from django.db import models

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

    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>"

    class Meta:
        db_table = "advertisements"


