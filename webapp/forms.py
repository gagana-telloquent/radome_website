from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from .models import BlogPost, BlogSection, BlogFAQ


# ======================================================
# CONTACT FORM
# ======================================================

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter Name",
            "class": "w-full px-4 py-3 border rounded-lg"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter Email",
            "class": "w-full px-4 py-3 border rounded-lg"
        })
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter Phone Number",
            "class": "w-full px-4 py-3 border rounded-lg"
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Enter Message",
            "rows": 5,
            "class": "w-full px-4 py-3 border rounded-lg"
        })
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name.strip()) < 3:
            raise ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")

        if len(phone) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")

        return phone

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(message.strip()) < 10:
            raise ValidationError("Message must be at least 10 characters long.")
        return message


# ======================================================
# BLOG POST FORM
# ======================================================

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'short_description',
            'banner_image',
            'author',
            'meta_title',
            'meta_description',
            'meta_keywords',
            'is_published'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'placeholder': 'Enter blog title...'
            }),

            'short_description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'rows': 3,
                'placeholder': 'Short description for blog listing...'
            }),

            'banner_image': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm'
            }),

            'author': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg'
            }),

            'meta_title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'placeholder': 'SEO Title (50–60 characters)'
            }),

            'meta_description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'rows': 2,
                'placeholder': 'SEO Description (150–160 characters)'
            }),

            'meta_keywords': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'placeholder': 'Comma separated keywords'
            }),

            'is_published': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-purple-600'
            }),
        }

    # 🔥 Auto SEO fallback logic
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get("title")
        short_description = cleaned_data.get("short_description")
        meta_title = cleaned_data.get("meta_title")
        meta_description = cleaned_data.get("meta_description")

        # Auto fill meta title if empty
        if not meta_title and title:
            cleaned_data["meta_title"] = title[:60]

        # Auto fill meta description if empty
        if not meta_description and short_description:
            cleaned_data["meta_description"] = short_description[:160]

        # SEO length validation
        if meta_title and len(meta_title) > 60:
            self.add_error("meta_title", "Meta title should not exceed 60 characters.")

        if meta_description and len(meta_description) > 160:
            self.add_error("meta_description", "Meta description should not exceed 160 characters.")

        return cleaned_data


# ======================================================
# BLOG SECTION FORM
# ======================================================

class BlogSectionForm(forms.ModelForm):

    class Meta:
        model = BlogSection
        fields = [
            'section_type',
            'order',
            'title',
            'content',
            'image'
        ]

        widgets = {
            'section_type': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg'
            }),

            'order': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'min': 0
            }),

            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'placeholder': 'Section title (optional)...'
            }),

            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'rows': 4,
                'placeholder': 'Section content...'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm'
            }),
        }

    def clean_order(self):
        order = self.cleaned_data.get("order")
        if order is not None and order < 0:
            raise ValidationError("Order must be 0 or greater.")
        return order


# ======================================================
# BLOG FAQ FORM
# ======================================================

class BlogFAQForm(forms.ModelForm):

    class Meta:
        model = BlogFAQ
        fields = ['question', 'answer', 'order']

        widgets = {
            'question': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'placeholder': 'Enter FAQ question...'
            }),

            'answer': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'rows': 3,
                'placeholder': 'Enter FAQ answer...'
            }),

            'order': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border rounded-lg',
                'min': 0
            }),
        }

    def clean_order(self):
        order = self.cleaned_data.get("order")
        if order is not None and order < 0:
            raise ValidationError("Order must be 0 or greater.")
        return order
