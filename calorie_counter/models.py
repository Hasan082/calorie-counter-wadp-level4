from django.db import models


class Profile(models.Model):
    CHOOSE_GENDER = [
        ("", "Select"),
        ("male", "Male"),
        ("female", "Female"),
    ]
    user = models.OneToOneField(
        "auth.User", on_delete=models.CASCADE, related_name="user_profile"
    )
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
        """
        Calculate and update the Basal Metabolic Rate (BMR) for the profile.
        Uses the Harris-Benedict equation for male and female.
        Only updates if all required fields are present.
        """

        if None in (self.weight, self.height, self.age, self.gender):
            return

        weight = float(self.weight)  # type: ignore
        height = float(self.height)  # type: ignore
        age = float(self.age)  # type: ignore

        if self.gender == "male":
            bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        else:
            bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

        self.bmr = bmr
        self.save(update_fields=["bmr"])


class CalorieConsumed(models.Model):
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="consumed"
    )
    date = models.DateField(null=True, blank=True)
    item_name = models.CharField(max_length=200)
    calorie_consumed = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.item_name} - {self.date} - {self.calorie_consumed} kcal"
