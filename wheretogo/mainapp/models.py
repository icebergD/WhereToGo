from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

User = get_user_model()


class Organization(models.Model):

	image = models.ImageField(verbose_name='Изображение')
	title = models.CharField(max_length=255, verbose_name='Наименование')
	slug = models.SlugField(unique=True)
	description = models.TextField(verbose_name='Описание', null=True)
	geo = models.CharField(max_length=255, verbose_name='Геопозиция')
	price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Средний чек')
	time_start_work = models.TimeField(verbose_name='Время начала работы')
	time_stop_work = models.TimeField(verbose_name='Время конца работы')
	creation_date = models.DateTimeField(verbose_name='Дата создания организации', default=timezone.now)

	def __str__(self):
		return str(self.title)



class Like(models.Model):
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	organization_id = models.ForeignKey(Organization, verbose_name='Понравившаяся организация', on_delete=models.CASCADE)

	def __str__(self):
		return '{} : {}'.format(self.user.name,self.liked_company.title)



class OrganizationHashtag(models.Model):

	organization_id = models.ForeignKey(Organization, verbose_name='Понравившаяся организация', on_delete=models.CASCADE)

	sport = models.PositiveIntegerField(verbose_name='спорт', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	art = models.PositiveIntegerField(verbose_name='искуство', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	health = models.PositiveIntegerField(verbose_name='здоровье', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	alone = models.PositiveIntegerField(verbose_name='один', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	withcompany = models.PositiveIntegerField(verbose_name='с компанией', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	adult = models.PositiveIntegerField(verbose_name='совершеннолетний', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	children = models.PositiveIntegerField(verbose_name='с детьми', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	male = models.PositiveIntegerField(verbose_name='мужчина', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	female = models.PositiveIntegerField(verbose_name='женщина', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	active = models.PositiveIntegerField(verbose_name='активный отдых', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	passiv = models.PositiveIntegerField(verbose_name='пассивный отдых', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

	def __str__(self):
			return str(self.organization_id.title)

class UserHashtag(models.Model):
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	
	sport = models.PositiveIntegerField(verbose_name='спорт', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	art = models.PositiveIntegerField(verbose_name='искуство', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	health = models.PositiveIntegerField(verbose_name='здоровье', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	alone = models.PositiveIntegerField(verbose_name='один', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	withcompany = models.PositiveIntegerField(verbose_name='с компанией', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	adult = models.PositiveIntegerField(verbose_name='совершеннолетний', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	children = models.PositiveIntegerField(verbose_name='с детьми', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	male = models.PositiveIntegerField(verbose_name='мужчина', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	female = models.PositiveIntegerField(verbose_name='женщина', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	active = models.PositiveIntegerField(verbose_name='активный отдых', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
	passiv = models.PositiveIntegerField(verbose_name='пассивный отдых', default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

	def __str__(self):
			return str(self.user.name)














# class Preference(models.Model):
# 	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
# 	interested_organization = models.ForeignKey(Organization, verbose_name='Понравившаяся организация', on_delete=models.CASCADE)

# 	def __str__(self):
# 		return '{} : {}'.format(self.user.name,self.liked_company.title)


# class Hashtag(models.Model):
# 	SPORT = 'sport'
# 	ART = 'art'
# 	HEALTH = 'health'
# 	ALONE = 'alone'
# 	WITHCOMPANY = 'withcompany'
# 	ADULT = 'adult'
# 	CHILDREN = 'children'
# 	MALE = 'male'
# 	FEMALE = 'female'
# 	ACTIVE = 'active'
# 	PASSIV = 'passiv'


# 	TAGS = (
# 		(SPORT, 'спорт'),
# 		(ART, 'искуство'),
# 		(HEALTH, 'здоровье'),
# 		(ALONE, 'один'),
# 		(WITHCOMPANY, 'с компанией'),
# 		(ADULT, 'совершеннолетний'),
# 		(CHILDREN, 'с детьми'),
# 		(MALE, 'мужчина'),
# 		(FEMALE, 'женщина'),
# 		(ACTIVE, 'активный отдых'),
# 		(PASSIV, 'пассивный отдых'),

# 	)

# 	birth_date = models.DateField(verbose_name='respondrs birth date', null=True, blank=True)
# 	tag = models.CharField(
# 		max_length=40, 
# 		verbose_name='теги для фильтрации',
# 		choices=TAGS,
# 		default=ALONE
# 	)

# 	organization = models.ForeignKey(Organization, verbose_name='Понравившаяся организация', on_delete=models.CASCADE)

# 	def __str__(self):
# 		return '{} : {}'.format(self.organization.title, self.tag)
