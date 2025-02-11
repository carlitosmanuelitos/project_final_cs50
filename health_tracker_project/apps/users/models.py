from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser, PermissionsMixin):
    """Extended User model"""
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    theme = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=10, null=True, blank=True)
    reset_token = models.CharField(max_length=100, unique=True, null=True, blank=True)
    reset_token_expires = models.DateTimeField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    # Required fields when extending AbstractUser
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    """User profile for health and fitness data"""
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
        PREFER_NOT_TO_SAY = 'N', _('Prefer not to say')

    class FitnessGoal(models.TextChoices):
        WEIGHT_LOSS = 'WL', _('Weight Loss')
        MUSCLE_GAIN = 'MG', _('Muscle Gain')
        MAINTENANCE = 'MT', _('Maintenance')
        GENERAL_FITNESS = 'GF', _('General Fitness')
        ATHLETIC_PERFORMANCE = 'AP', _('Athletic Performance')

    # Core relationship
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profile'
    )

    # Basic Information
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.PREFER_NOT_TO_SAY
    )
    height = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Height in centimeters"
    )
    current_weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Weight in kilograms"
    )
    target_weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Target weight in kilograms"
    )

    # Health Information
    medical_conditions = models.JSONField(default=list, blank=True)
    medications = models.JSONField(default=list, blank=True)
    allergies = models.JSONField(default=list, blank=True)
    dietary_restrictions = models.JSONField(default=list, blank=True)

    # Fitness Information
    fitness_goal = models.CharField(
        max_length=2,
        choices=FitnessGoal.choices,
        default=FitnessGoal.GENERAL_FITNESS
    )
    activity_level = models.PositiveSmallIntegerField(
        choices=[
            (1, _('Sedentary')),
            (2, _('Lightly Active')),
            (3, _('Moderately Active')),
            (4, _('Very Active')),
            (5, _('Extremely Active'))
        ],
        default=1
    )
    exercise_preferences = models.JSONField(default=list)

    # Nutrition Goals
    daily_calorie_goal = models.PositiveIntegerField(null=True, blank=True)
    macros_preferences = models.JSONField(
        default=dict,
        help_text="JSON containing protein, carbs, and fat goals in grams"
    )
    meal_preference = models.JSONField(
        default=dict,
        help_text="JSON containing meal timing and frequency preferences"
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def calculate_bmr(self):
        """Calculate Basal Metabolic Rate"""
        # Implementation here
        pass

    def calculate_tdee(self):
        """Calculate Total Daily Energy Expenditure"""
        # Implementation here
        pass