from django.db import models




class Ingredient(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']




class Recipe(models.Model):
    title = models.CharField(max_length=255)


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
