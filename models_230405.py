# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hazardprofile(models.Model):
    Facility_classification_large = models.TextField(db_column='시설물분류(대)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Facility_classification_medium = models.TextField(db_column='시설물분류(중)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Facility_classification_small= models.TextField(db_column='시설물분류(소)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Work_type_classification_Large = models.TextField(db_column='공종분류(대)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Construction_type_classification_middle = models.TextField(db_column='공종분류(중)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Classification_of_hazardous_objects_Large = models.TextField(db_column='위험발생객체분류(대)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Classification_of_hazardous_objects = models.TextField(db_column='위험발생객체분류(중)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Hazardous_location_classification_large = models.TextField(db_column='위험발생위치분류(대)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Danger_occurrence_location_code_middle = models.FloatField(db_column='위험발생위치코드(중)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Hazardous_location_classification_medium = models.TextField(db_column='위험발생위치분류(중)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    Hazardous_location_classification_small = models.TextField(db_column='위험발생위치분류(소)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    work_process = models.TextField(db_column='작업프로세스명', blank=True, null=True)
    blood_red_blood = models.TextField(db_column='물적피해', blank=True, null=True)
    human_blood = models.TextField(db_column='인적피해', blank=True, null=True)
    accident_center = models.TextField(db_column='사고원인', blank=True, null=True)
    Accident_possible = models.TextField(db_column='사고가능성', blank=True, null=True)
    Serious_accident = models.TextField(db_column='사고심각성', blank=True, null=True)
    design_team = models.TextField(db_column='설계단계', blank=True, null=True)
    Construction_team = models.TextField(db_column='시공단계', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HazardProfile'


class Riskfactorsprofile(models.Model):
    Facility_classification_large = models.TextField(db_column='시설물분류_대', blank=True, null=True)
    Facility_classification_medium = models.TextField(db_column='시설물분류_중', blank=True, null=True)
    Facility_classification_small = models.TextField(db_column='시설물분류_소', blank=True, null=True)
    Construction_type_classification_Large = models.TextField(db_column='공종분류_대', blank=True, null=True)
    Construction_type_classification_middle = models.TextField(db_column='공종분류_중', blank=True, null=True)
    Risk_generating_object_Large = models.TextField(db_column='위험발생객체_대', blank=True, null=True)
    Dangerous_object_medium = models.TextField(db_column='위험발생객체_중', blank=True, null=True)
    Danger_occurrence_location_large = models.TextField(db_column='위험발생위치_대', blank=True, null=True)
    Danger_occurrence_location_middle = models.TextField(db_column='위험발생위치_중', blank=True, null=True)
    Location_of_risk_small = models.TextField(db_column='위험발생위치_소', blank=True, null=True)
    work_process = models.TextField(db_column='작업프로세스', blank=True, null=True)
    material_damage = models.TextField(db_column='물적피해', blank=True, null=True)
    human_damage = models.TextField(db_column='인적피해', blank=True, null=True)
    Accident_cause_code = models.TextField(db_column='사고원인코드', blank=True, null=True)
    possibility_of_accident = models.TextField(db_column='사고가능성', blank=True, null=True)
    Accident_severity = models.TextField(db_column='사고심각성', blank=True, null=True)
    Reduction_measures_design = models.TextField(db_column='저감대책_설계', blank=True, null=True)
    Reduction_measures_construction = models.TextField(db_column='저감대책_시공', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RiskFactorsProfile'


class AdulAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('AuthUser', models.DO_NOTHING)
    question = models.ForeignKey('AdulQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adul_answer'


class AdulAnswerVoter(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.ForeignKey(AdulAnswer, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adul_answer_voter'
        unique_together = (('answer', 'user'),)


class AdulQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adul_question'


class AdulQuestionVoter(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(AdulQuestion, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'adul_question_voter'
        unique_together = (('question', 'user'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BomAssemlist(models.Model):
    title = models.CharField(db_column='Title', primary_key=True, max_length=50)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=200, blank=True, null=True)  # Field name made lowercase.
    matl = models.CharField(db_column='Matl', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    b = models.IntegerField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t1 = models.IntegerField(blank=True, null=True)
    t2 = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    paint = models.IntegerField(db_column='Paint', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bom_assemlist'


class BomList(models.Model):
    bcode = models.IntegerField(db_column='Bcode', primary_key=True)  # Field name made lowercase.
    assmark = models.ForeignKey(BomAssemlist, models.DO_NOTHING, db_column='AssMark')  # Field name made lowercase.
    partmark = models.CharField(db_column='PartMark', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200, blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    b = models.IntegerField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t1 = models.IntegerField(blank=True, null=True)
    t2 = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    unit = models.IntegerField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area = models.IntegerField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    weight = models.PositiveIntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bom_list'


class BomPartlist(models.Model):
    mark = models.CharField(db_column='Mark', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='Profile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    b = models.IntegerField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    t1 = models.IntegerField(blank=True, null=True)
    t2 = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area = models.IntegerField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    unit = models.IntegerField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    weight_1 = models.IntegerField(db_column='Weight_1', blank=True, null=True)  # Field name made lowercase.
    weight_2 = models.IntegerField(db_column='Weight_2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bom_partlist'


class BomPlatelist(models.Model):
    mark = models.CharField(db_column='Mark', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='Profile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    h = models.IntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area = models.IntegerField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    weight_1 = models.IntegerField(db_column='Weight_1', blank=True, null=True)  # Field name made lowercase.
    weight_2 = models.IntegerField(db_column='Weight_2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bom_platelist'


class BookList(models.Model):
    bcode = models.IntegerField(db_column='BCODE', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year_of_publication = models.CharField(db_column='YEAR-OF-PUBLICATION', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher = models.ForeignKey('BookStore', models.DO_NOTHING, db_column='PUBLISHER', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_list'


class BookStore(models.Model):
    bscode = models.IntegerField(db_column='BSCODE', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_store'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FileData(models.Model):
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_data'


class MartShtreg(models.Model):
    ��⸻�Ҵ��� = models.CharField(max_length=33, blank=True, null=True)
    ����_����_�ڵ� = models.CharField(max_length=1, blank=True, null=True)
    ����_����_�ڵ�_�� = models.CharField(max_length=100, blank=True, null=True)
    ����_����_�ڵ� = models.CharField(max_length=5, blank=True, null=True)
    ����_����_�ڵ�_�� = models.CharField(max_length=1, blank=True, null=True)
    ����_��ġ = models.CharField(max_length=100, blank=True, null=True)
    ���θ�_����_��ġ = models.CharField(max_length=500, blank=True, null=True)
    �ǹ�_�� = models.CharField(max_length=400, blank=True, null=True)
    �ñ���_�ڵ� = models.CharField(max_length=100, blank=True, null=True)
    ������_�ڵ� = models.CharField(max_length=5, blank=True, null=True)
    ����_����_�ڵ� = models.CharField(max_length=1, blank=True, null=True)
    �� = models.CharField(max_length=4, blank=True, null=True)
    �� = models.CharField(max_length=4, blank=True, null=True)
    Ư����_�� = models.CharField(max_length=200, blank=True, null=True)
    ���� = models.CharField(max_length=20, blank=True, null=True)
    ��Ʈ = models.CharField(max_length=20, blank=True, null=True)
    ������_�� = models.IntegerField(blank=True, null=True)
    ���ּ�_����_�ڵ� = models.CharField(max_length=12, blank=True, null=True)
    ���ּ�_������_�ڵ� = models.CharField(max_length=5, blank=True, null=True)
    ���ּ�_��������_�ڵ� = models.CharField(max_length=1, blank=True, null=True)
    ���ּ�_��_�� = models.IntegerField(blank=True, null=True)
    ���ּ�_��_�� = models.IntegerField(blank=True, null=True)
    ���ð��� = models.IntegerField(blank=True, null=True)
    ����_���� = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mart_shtreg'


class Meterial(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meterial'


class YesList(models.Model):
    bcode = models.IntegerField(db_column='BCODE', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year_of_publication = models.CharField(db_column='YEAR-OF-PUBLICATION', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher = models.ForeignKey(BookStore, models.DO_NOTHING, db_column='PUBLISHER', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yes_list'


class YesStore(models.Model):
    bscode = models.IntegerField(db_column='BSCODE', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yes_store'
