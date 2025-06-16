# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Budgets(models.Model):
    id_movie = models.AutoField(primary_key=True)
    value = models.PositiveBigIntegerField(blank=True, null=True)
    currency = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budgets'


class CompaniesNow(models.Model):
    id_movie = models.AutoField(primary_key=True)
    string_dict = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies_now'


class Countries(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'countries'
        unique_together = (('id', 'name'),)


class Facts(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    spoiler = models.IntegerField(blank=True, null=True)
    id_movie = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facts'


class FactsMovie(models.Model):
    id_movie = models.AutoField(primary_key=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facts_movie'


class FactsPerson(models.Model):
    id_person = models.AutoField(primary_key=True)
    string_dict = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facts_person'


class FilmCountries(models.Model):
    id_film = models.IntegerField()
    id_country = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'film_countries'
        unique_together = (('id_film', 'id_country'),)


class FilmFact(models.Model):
    id_movie = models.IntegerField()
    id_fact = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'film_fact'
        unique_together = (('id_movie', 'id_fact'),)


class FilmGenres(models.Model):
    id_film = models.IntegerField()
    id_genres = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'film_genres'
        unique_together = (('id_film', 'id_genres'),)


class FilmPerson(models.Model):
    id_movie = models.IntegerField()
    id_person = models.IntegerField()
    id_proffesion = models.IntegerField()
    description = models.CharField(max_length=120, blank=True, null=True)
    place_kinopoisk = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_person'
        unique_together = (('id_movie', 'id_person', 'id_proffesion'),)


class Genres(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'genres'
        unique_together = (('id', 'name'),)


class KinopoiskApi(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(blank=True, null=True)
    update_data = models.DateField(blank=True, null=True)
    max_value = models.IntegerField()
    work = models.IntegerField(blank=True, null=True)
    name_of_people = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kinopoisk_api'
        unique_together = (('id', 'name'),)


class Logs(models.Model):
    log_time = models.DateTimeField(blank=True, null=True)
    log_type = models.IntegerField(blank=True, null=True)
    log_message = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class MySpisok(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    name_my = models.CharField(max_length=150, blank=True, null=True)
    my_rate = models.FloatField(blank=True, null=True)
    kp_rate = models.FloatField(blank=True, null=True)
    imdb_rate = models.FloatField(blank=True, null=True)
    voice = models.CharField(max_length=150, blank=True, null=True)
    watch = models.CharField(max_length=150, blank=True, null=True)
    poster = models.TextField(blank=True, null=True)
    isseries = models.IntegerField(db_column='isSeries', blank=True, null=True)  # Field name made lowercase.
    serieslength = models.IntegerField(db_column='seriesLength', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    age_rating = models.IntegerField(blank=True, null=True)
    year_create = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.CharField(max_length=25, blank=True, null=True)
    add_id_tg = models.IntegerField(blank=True, null=True)
    type_number = models.IntegerField(blank=True, null=True)
    total_series_length = models.IntegerField(blank=True, null=True)
    backdrop = models.TextField(blank=True, null=True)
    movie_length = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_spisok'


class PersonSpouse(models.Model):
    id_person = models.PositiveIntegerField()
    id_spouse = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'person_spouse'
        unique_together = (('id_person', 'id_spouse'),)


class Persons(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=150)
    enname = models.CharField(db_column='enName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=10, blank=True, null=True)
    growth = models.PositiveIntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    death = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class PinFilm(models.Model):
    id_film = models.IntegerField()
    id_telegram = models.IntegerField()
    data_pin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pin_film'
        unique_together = (('id_film', 'id_telegram'),)


class Proffesions(models.Model):
    name = models.CharField(max_length=50)
    eng_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proffesions'


class RateTitle(models.Model):
    id_telegram = models.IntegerField()
    id_film = models.IntegerField()
    rate = models.FloatField()
    date_rate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rate_title'


class ReasonSkipApiTask(models.Model):
    id_task = models.AutoField(primary_key=True)
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'reason_skip_api_task'


class RulesMachine(models.Model):
    id_machine = models.AutoField(primary_key=True)
    count_last_api = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rules_machine'


class SequelsAndPrequels(models.Model):
    id_movie = models.IntegerField()
    id_sap_film = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sequels_and_prequels'
        unique_together = (('id_movie', 'id_sap_film'),)


class SimilarMovies(models.Model):
    id_movie = models.IntegerField()
    id_similar_film = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'similar_movies'
        unique_together = (('id_movie', 'id_similar_film'),)


class Spouses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    divorced = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    divorced_reason = models.CharField(max_length=50, blank=True, null=True)
    relation = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spouses'


class TelegramUserSettings(models.Model):
    id_telegram = models.AutoField(primary_key=True)
    premium_user = models.IntegerField()
    date_end_premium = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    last_action = models.DateTimeField(blank=True, null=True)
    show_photos_in_open_title_flag = models.IntegerField(blank=True, null=True)
    show_photos_in_pin_titles_flag = models.IntegerField(blank=True, null=True)
    show_photos_in_top_titles_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telegram_user_settings'


class TrailersNow(models.Model):
    id_movie = models.AutoField(primary_key=True)
    string_dict = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trailers_now'


class TypeTitle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'type_title'
