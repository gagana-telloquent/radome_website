from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
#Home Page Models
class PageBanner(models.Model):
    PAGE_CHOICES = [
        ("home", "Home"),
        ("our_work", "Our Work"),
        ("insights", "Insights"),
        ("blog", "Blog"),
        ("contact", "Contact"),
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES, unique=True)
    title = models.TextField()
    subtitle = models.TextField(blank=True)

    background_image = models.ImageField(upload_to="page_banners/images/", blank=True, null=True)
    background_video = models.FileField(upload_to="page_banners/videos/", blank=True, null=True)

    def __str__(self):
        return f"{self.get_page_display()} Banner"


# =========================
# HOME INTRO SECTION
# =========================
class Intro(models.Model):
    title = models.TextField(
        blank=True, null=True,
        help_text="Intro Title"
    )
    image = models.ImageField(
        upload_to="home/intro/",
        help_text="Intro section image"
    )
    description = models.TextField(
        help_text="Intro descriptive text"
    )

    class Meta:
        verbose_name = "Intro"
        verbose_name_plural = "Intro"

    def __str__(self):
        return "Intro Section"


# =========================
# COMPANY STATS
# =========================
class CompanyStat(models.Model):
    value = models.CharField(
        max_length=20,
        help_text="Stat value (e.g. 150+, 21, 2)"
    )
    label = models.CharField(
        max_length=100,
        help_text="Stat label (e.g. Models Built)"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Company Stat"
        verbose_name_plural = "Company Stats"

    def __str__(self):
        return f"{self.value} - {self.label}"


# =========================
# WHAT WE DO – RIGHT IMAGE
# =========================
class WhatWeDoImage(models.Model):
    image = models.ImageField(
        upload_to="home/what_we_do/",
        help_text="Right-side image for What We Do section"
    )

    class Meta:
        verbose_name = "What We Do Image"
        verbose_name_plural = "What We Do Image"

    def __str__(self):
        return "What We Do Image"


# =========================
# WHAT WE DO – ICON + TEXT (LOOP)
# =========================
class WhatWeDoItem(models.Model):
    icon = models.ImageField(
        upload_to="home/what_we_do/icons/",
        help_text="Icon image"
    )
    text = models.CharField(
        max_length=300,
        help_text="Description text"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "What We Do Item"
        verbose_name_plural = "What We Do Items"

    def __str__(self):
        return self.text


# =========================
# VALUE CARDS
# =========================
class ValueCard(models.Model):
    icon = models.ImageField(
        upload_to="home/value_icons/",
        help_text="Value card icon image"
    )
    text = models.CharField(
        max_length=200,
        help_text="Value card description"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Value Card"
        verbose_name_plural = "Value Cards"

    def __str__(self):
        return self.text


# =========================
# PORTFOLIO IMAGES
# =========================
class PortfolioImage(models.Model):
    image = models.ImageField(
        upload_to="radome/portfolio/",
        help_text="Portfolio image"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Portfolio Image"
        verbose_name_plural = "Portfolio Images"

    def __str__(self):
        return f"Portfolio Image {self.order}"


# =========================
# REEL VIDEO
# =========================
class ReelVideo(models.Model):
    video = models.FileField(
        upload_to="radome/reel/",
        help_text="Reel video file"
    )

    class Meta:
        verbose_name = "Reel Video"
        verbose_name_plural = "Reel Video"

    def __str__(self):
        return "Reel Video"


# =========================
# TEAM MEMBERS
# =========================
class TeamMember(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Full name"
    )
    position = models.CharField(
        max_length=150,
        help_text="Job title / position"
    )
    bio = models.TextField(
        blank=True,
        null=True,
        help_text="Short introduction (optional)"
    )
    image = models.ImageField(
        upload_to="radome/team/",
        help_text="Team member photo"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} - {self.position}"


# =========================
# ACHIEVEMENTS
# =========================
class Achievement(models.Model):
    image = models.ImageField(
        upload_to="radome/achievements/",
        help_text="Achievement / certificate image"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return f"Achievement {self.order}"


# =========================
# MEDIA GALLERY
# =========================
class MediaGallery(models.Model):
    image = models.ImageField(
        upload_to="radome/media/",
        help_text="Media gallery image"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Display order"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Media Gallery Image"
        verbose_name_plural = "Media Gallery Images"

    def __str__(self):
        return f"Media Image {self.order}"
    
# =========================
# ACHIEVEMENT HIGHLIGHT IMAGE
# =========================
class AchievementHighlight(models.Model):
    background_image = models.ImageField(
        upload_to="radome/achievements/highlight/background/",
        help_text="Blurred background image"
    )
    overlay_image = models.ImageField(
        upload_to="radome/achievements/highlight/overlay/",
        help_text="Center award/logo image"
    )

    class Meta:
        verbose_name = "Achievement Highlight"
        verbose_name_plural = "Achievement Highlight"

    def __str__(self):
        return "Achievement Highlight"
    
#================================================================================
#Our-work Page Models
# =========================
class Industry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to="our_work/industries/")
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Industry"
        verbose_name_plural = "Industries"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
         return reverse("industry_detail", kwargs={"slug": self.slug})
    def __str__(self):
        return self.title


class AICoreCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(
        upload_to="our_work/ai_core/"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "AI Core Card"
        verbose_name_plural = "AI Core Cards"

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    banner_image = models.ImageField(
        upload_to="our_work/products/banner/",
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
class ProductModuleIcon(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="module_icons"
    )

    title = models.CharField(max_length=255) 
    icon = models.ImageField(
        upload_to="our_work/products/module_icons/"
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.product.title} - {self.title}"


class UseCase(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    banner_image = models.ImageField(
        upload_to="our_work/usecases/banner/",
        blank=True,
        null=True
    )
        # NEW FIELDS
    tags = models.CharField(max_length=200, blank=True)
    tags_icon = models.ImageField(
        upload_to="our_work/usecases/meta_icons/",
        blank=True,
        null=True
    )
    date = models.DateField(blank=True, null=True)
    date_icon = models.ImageField(
            upload_to="our_work/usecases/meta_icons/",
            blank=True,
            null=True
        )

    location = models.TextField(blank=True)
    location_icon = models.ImageField(
        upload_to="our_work/usecases/meta_icons/",
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("use_case_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
class UseCaseChallenge(models.Model):
    use_case = models.OneToOneField(
        UseCase,
        on_delete=models.CASCADE,
        related_name="challenge"
    )

    title = models.CharField(max_length=200, default="Challenge")
    description = models.TextField()
    image = models.ImageField(
        upload_to="our_work/usecases/challenge/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.use_case.title} - Challenge"
    
class UseCaseSolution(models.Model):
    use_case = models.OneToOneField(
        UseCase,
        on_delete=models.CASCADE,
        related_name="solution"
    )

    title = models.CharField(max_length=200, default="Our Solution")
    description = models.TextField()
    image = models.ImageField(
        upload_to="our_work/usecases/solution/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.use_case.title} - Solution"

class UseCaseFeature(models.Model):
    use_case = models.ForeignKey(
        UseCase,
        on_delete=models.CASCADE,
        related_name="features"
    )

    icon = models.ImageField(
        upload_to="our_work/usecases/features/"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.use_case.title} - {self.title}"

    
class IndustryDetail(models.Model):
    industry = models.OneToOneField(
        Industry,
        on_delete=models.CASCADE,
        related_name="detail"
    )

    banner_image = models.ImageField(
        upload_to="our_work/industries/banner/",
        blank=True,
        null=True
    )

    page_title = models.CharField(
        max_length=200,
        blank=True
    )

    intro_heading = models.CharField(
        max_length=300,
        blank=True
    )

    intro_image = models.ImageField(
        upload_to="our_work/industries/intro/",
        blank=True,
        null=True
    )

    intro_text = models.TextField(
        blank=True
    )

    highlight_text = models.TextField(
        blank=True,
        help_text="Black background highlight text"
    )
        # =========================
    # PRODUCT PREVIEW SECTION
    # =========================
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Select product to display"
    )

    product_preview_title = models.CharField(
        max_length=300,
        blank=True,
        help_text="Product preview title"
    )

    product_preview_description = models.TextField(
        blank=True,
        help_text="Short product preview text"
    )

    product_preview_image = models.ImageField(
        upload_to="our_work/industries/product/",
        blank=True,
        null=True
    )

    product_button_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Button text (e.g. Explore More)"
    )

     # =========================
    # USE CASE PREVIEW SECTION
    # =========================
    use_case = models.ForeignKey(
        "UseCase",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    use_case_preview_title = models.CharField(
        max_length=255,
        blank=True
    )

    use_case_preview_description = models.TextField(
        blank=True
    )

    use_case_button_text = models.CharField(
        max_length=100,
        blank=True
    )

# =========================
# INSIGHTS INTRO
# =========================
class InsightsIntro(models.Model):
    description = models.TextField()

    def __str__(self):
        return "Insights Intro Section"

# =========================
# MISSION / VISION / VALUE
# =========================
class MVVSection(models.Model):

    TAB_CHOICES = [
        ("mission", "Mission"),
        ("vision", "Vision"),
        ("value", "Value"),
    ]

    tab_type = models.CharField(max_length=20, choices=TAB_CHOICES)
    heading = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="insights/mvv/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.get_tab_type_display()

# =========================
# VALUE POINTS (Under Our Value)
# =========================
class ValuePoint(models.Model):
    icon = models.ImageField(upload_to="insights/value/icons/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

class BlogAuthor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="blog/authors/", blank=True, null=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.CharField(max_length=300, blank=True)

    banner_image = models.ImageField(
        upload_to="blog/banner/",
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        BlogAuthor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    short_description = models.TextField(
        help_text="Used in blog listing page"
    )

    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title

class BlogSection(models.Model):

    SECTION_TYPES = [
        ('toc', 'Table of Contents'), 
        ("h2", "Heading (H2 - Main Section)"),
        ("h3", "Sub Heading (H3 - Sub Section)"),
        ("paragraph", "Paragraph / Bullet List"),
        ("image", "Image"),
    ]

    blog = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name="sections"
    )

    section_type = models.CharField(
        max_length=20,
        choices=SECTION_TYPES
    )

    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="blog/sections/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]


    def __str__(self):
        return f"{self.blog.title} - {self.section_type}"


class BlogFAQ(models.Model):
    blog = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name="faqs"
    )

    question = models.CharField(max_length=500)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.blog.title} - FAQ"
