from modeltranslation.translator import translator, TranslationOptions, register
from website.models import Post

# @register(Post)
# class PostTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')



# Define translation options for the Post model
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

# Register the Post model with its translation options
translator.register(Post, PostTranslationOptions)
