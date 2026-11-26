from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    birth_date = models.DateField()

class Status(models.Model):
    name = models.CharField(max_length=150)

class Type(models.Model):
    name = models.CharField(max_length=150)

class Aboniment(models.Model):
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)
    type_ID = models.ForeignKey(Type, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

class Specialization(models.Model):
    name = models.CharField(max_length=150)

class Trainer(models.Model):
    full_name = models.CharField(max_length=200)
    specialization_ID = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class Weekday(models.Model):
    name = models.CharField(max_length=150)

class Hallroom(models.Model):
    name = models.CharField(max_length=150)

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    trainer_ID = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    weekday_ID = models.ForeignKey(Weekday, on_delete=models.CASCADE)
    timeExercise = models.TimeField()
    hallroom_ID = models.ForeignKey(Hallroom, on_delete=models.CASCADE)

class RegistrForExercise(models.Model):
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)
    exercise_ID = models.ForeignKey(Exercise, on_delete=models.CASCADE)
