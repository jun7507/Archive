from django.db import models

# Create your models here.


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
        