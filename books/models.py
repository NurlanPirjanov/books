from django.db import models
from django.urls import reverse

class Kafedra(models.Model):
    """Kafedra jadvali"""
    kaf_name = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.kaf_name}'
    
    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = 'Kafedralar'

class BookLanguage(models.Model):
    """Kitob tili"""
    lang = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.lang}'

    class Meta:
        verbose_name = 'Til'
        verbose_name_plural = 'Tillar'

class Qanigelik(models.Model):
    """Talim yo`nalishi"""
    yonalish = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.yonalish}'
    class Meta:
        verbose_name = 'Ta`lim yo`nalishi'
        verbose_name_plural = 'Ta`lim yo`nalishlari'

class Books(models.Model):
    """Adbiyotlar"""
    SEM_CHOICES = (
        ("I", "I"),
        ("II", "II"),
        ("III", "III"),
        ("IV", "IV"),
        ("V", "V"),
        ("VI", "VI"),
        ("VII", "VII"),
        ("VIII", "VIII"),
        ("IX", "IX"),
        ("X", "X"),
    )
    sem = models.CharField(max_length=4,
                           choices=SEM_CHOICES,
                           default="I")
    KURS_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    kurs = models.CharField(max_length=1,
                            choices=KURS_CHOICES,
                            default="1")
    book_name = models.CharField(max_length=255, verbose_name='Kitob nomi')
    book_author = models.CharField(max_length=255, verbose_name='Kitob Avtorlari')
    year = models.DateField(verbose_name="Nashr yili", null=True, blank=True)
    isbn = models.CharField(verbose_name='ISBN yoki ISSN', max_length=15, null=True, blank=True)
    printing_office = models.CharField(max_length=100, verbose_name='Bosmaxona', null=True, blank=True)
    lang = models.ForeignKey(BookLanguage, on_delete=models.CASCADE, verbose_name='Kitob tili', default=1)
    yunalish = models.ForeignKey(Qanigelik, on_delete=models.CASCADE, verbose_name='Yunalish',default=1)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE, verbose_name="Kafedra", default=1) 
    science = models.CharField(max_length=100, verbose_name='Fan nomi', null=True, blank=True)
    teacher = models.CharField(max_length=100, verbose_name='O`qituvchi ismi, familyasi va sharifi', blank=True, null=True)
    book_number = models.IntegerField(verbose_name='Kibobxonadagi kitoblar soni', null=True, blank=True)
    elektron_bool = models.BooleanField(verbose_name='Elektron shakilda mavjudligi', default=False, null=True, blank=True)
    book_url_file = models.URLField(verbose_name='Kitob URL adresi', null=True, blank=True)

    def __str__(self):
        return f'{self.book_name}'

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'