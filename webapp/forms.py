from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from .models import BlogPost, BlogSection, BlogFAQ
import re


# ======================================================
# CONTACT FORM
# ======================================================
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        min_length=3,
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
        max_length=1000,
        min_length=10,
        widget=forms.Textarea(attrs={
            "placeholder": "Enter Message",
            "rows": 5,
            "class": "w-full px-4 py-3 border rounded-lg"
        })
    )

    # -------------------------
    # NAME VALIDATION
    # -------------------------
    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()

        if not name:
            raise ValidationError("Name cannot be empty.")

        # Allow only letters and spaces
        if not re.match(r"^[A-Za-z ]+$", name):
            raise ValidationError("Name must contain only letters and spaces.")

        if len(name) < 3:
            raise ValidationError("Name must be at least 3 characters long.")

        return name.title()


    # -------------------------
    # PHONE VALIDATION
    # -------------------------
    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()

        if not phone:
            raise ValidationError("Phone number is required.")

        # Remove spaces and dashes
        phone = phone.replace(" ", "").replace("-", "")

        # Support Indian numbers (10 digits or +91XXXXXXXXXX)
        pattern = r"^(\+91)?[6-9]\d{9}$"

        if not re.match(pattern, phone):
            raise ValidationError(
                "Enter a valid 10-digit Indian phone number."
            )

        return phone


    # -------------------------
    # MESSAGE VALIDATION
    # -------------------------
    def clean_message(self):
        message = self.cleaned_data.get("message", "").strip()

        if not message:
            raise ValidationError("Message cannot be empty.")

        if len(message) < 10:
            raise ValidationError("Message must be at least 10 characters long.")

        if len(message) > 1000:
            raise ValidationError("Message must be under 1000 characters.")

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
            'published_at', 
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
'published_at': forms.DateTimeInput(
    format='%Y-%m-%dT%H:%M',
    attrs={
        'type': 'datetime-local',
        'step': '1',
        'class': 'w-full px-4 py-3 border rounded-lg'
    }
),
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
            'image',
            'is_logo' ,
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
            'is_logo': forms.CheckboxInput(attrs={
    'class': 'h-5 w-5 text-purple-600'
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
