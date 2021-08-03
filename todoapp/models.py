from django.db import models

# Create your models here.

class Todo(models.Model):
    PRIORITY_CHOICES=(
        (1,"Weak"),
        (2,"Low"),
        (3,"Medium"),
        (4,"High"),
        (5,"Highest")
    )
    title       = models.CharField(max_length=250)
    description = models.TextField()
    # priority    = models.IntegerField()
    priority    = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=1)
    created_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # @property
    # def priority_display(self):
    #     mydec = {
    #         1 : "Weak",
    #         2 : "Low",
    #         3 : "Medium",
    #         4 : "High",
    #         5 : "Highest"
    #     }
    #     return mydec[self.priority] if self.priority in mydec else "Not Found"
