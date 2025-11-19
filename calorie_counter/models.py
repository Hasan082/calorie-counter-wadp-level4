from django.db import models


class Profile(models.Model):
    CHOOSE_GENDER = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(
        choices=CHOOSE_GENDER, max_length=10, null=True, blank=True
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    bmr = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    def calculate_bmr(self):
        if self.weight and self.height and self.age and self.gender:
            if self.gender == "male":
                bmr = (
                    66.47
                    + (13.75 * self.weight)
                    + (5.003 * self.height)
                    - (6.755 * self.age)
                )
                self.bmr = bmr
                self.save()
            else:
                bmr = (
                    655.1
                    + (9.563 * self.weight)
                    + (1.850 * self.height)
                    - (4.676 * self.age)
                )
                self.bmr = bmr
                self.save()


class CalorieConsumed(models.Model):
    user = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    date = models.DateField()
    item_name = models.CharField()
    calorie_consumed = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.profile.name} - {self.date} - {self.calories} kcal"
