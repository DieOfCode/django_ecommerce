from django.contrib import admin
from django.forms import ModelForm
from PIL import Image
from mainshop import models
# Register your models here.
from django import forms


class SmartphoneAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if not instance.sd:
            self.fields["sd_volume_max"].widget.attrs.update({
                "readonly": True, "style": "background:lightgray"
            })

    def clean(self):
        if not self.cleaned_data["sd"]:
            self.cleaned_data["sd_volume_max"] = None
        return self.cleaned_data


class NotebookAdminForm(ModelForm):
    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].help_text = "Загружайте изображение с минимальным разрешением {}X{}".format(
            *self.MIN_RESOLUTION)

    def clean_image(self):
        picture = self.cleaned_data["image"]
        image = Image.open(picture)
        return picture


class NotebookAdmin(admin.ModelAdmin):
    form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return forms.ModelChoiceField(models.Category.objects.filter(slug="notebooks"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):
    change_form_template = "mainshop/admin.html"
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return forms.ModelChoiceField(models.Category.objects.filter(slug="smartphone"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(models.Category)
admin.site.register(models.Notebook, NotebookAdmin)
admin.site.register(models.Smartphone, SmartphoneAdmin)
admin.site.register(models.Customer)
admin.site.register(models.Cart)
admin.site.register(models.CartProduct)
admin.site.register(models.Order)
