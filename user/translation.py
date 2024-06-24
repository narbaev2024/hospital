from .models import Doctor
from modeltranslation.translator import TranslationOptions, register

@register(Doctor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('specialty',)
