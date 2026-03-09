from django.contrib import admin
from django.utils.html import format_html

from .models import (
    PageBanner,
    Intro,
    CompanyStat,
    WhatWeDoImage,
    WhatWeDoItem,
    ValueCard,
    PortfolioImage,
    ReelVideo,
    TeamMember,
    Achievement,
    MediaGallery,
    AchievementHighlight,
    Industry,
    AICoreCard,
    IndustryDetail,
    UseCase,  
    Product,
    ProductModuleIcon,
    UseCaseChallenge,
    UseCaseFeature,
    UseCaseSolution,
    InsightsIntro,     
    MVVSection,        
    ValuePoint, 
    BlogPost, BlogSection, BlogFAQ, BlogAuthor, 
)


# ==================================================
# BASE IMAGE PREVIEW MIXIN
# ==================================================
class ImagePreviewMixin:
    def image_preview(self, obj):
        image_field = None

        if hasattr(obj, "image") and obj.image:
            image_field = obj.image
        elif hasattr(obj, "icon") and obj.icon:
            image_field = obj.icon

        if image_field:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:6px;" />',
                image_field.url,
            )
        return "-"

    image_preview.short_description = "Preview"



# ==================================================
# SINGLE ENTRY MODELS
# ==================================================
@admin.register(PageBanner)
class PageBannerAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    max_num = 1  # enforce single entry

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display = ("title",)
    max_num = 1  # enforce single entry 

@admin.register(WhatWeDoImage)
class WhatWeDoImageAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview",)
    max_num = 1


@admin.register(ReelVideo)
class ReelVideoAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    max_num = 1

@admin.register(AchievementHighlight)
class AchievementHighlightAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    max_num = 1


# ==================================================
# ORDERED / LOOP MODELS
# ==================================================
@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "order")
    ordering = ("order",)
    list_editable = ("order",)


@admin.register(WhatWeDoItem)
class WhatWeDoItemAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview", "text", "order")
    ordering = ("order",)
    list_editable = ("order",)


@admin.register(ValueCard)
class ValueCardAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview", "text", "order")
    ordering = ("order",)
    list_editable = ("order",)


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview", "order")
    ordering = ("order",)
    list_editable = ("order",)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview", "name", "position", "order")
    ordering = ("order",)
    list_editable = ("order",)
    search_fields = ("name", "position")


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview", "order")
    ordering = ("order",)
    list_editable = ("order",)


@admin.register(MediaGallery)
class MediaGalleryAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview", "order")
    ordering = ("order",)
    list_editable = ("order",)



@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(AICoreCard)
class AICoreCardAdmin(admin.ModelAdmin):
    list_display = ("title", "order")

class ProductModuleIconInline(admin.TabularInline):
    model = ProductModuleIcon
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    inlines = [ProductModuleIconInline]


# ==================================================
# USE CASE INLINES
# ==================================================

class UseCaseChallengeInline(admin.StackedInline, ImagePreviewMixin):
    model = UseCaseChallenge
    extra = 0
    max_num = 1
    readonly_fields = ("image_preview",)
    fields = ("title", "description", "image", "image_preview")

class UseCaseSolutionInline(admin.StackedInline, ImagePreviewMixin):
    model = UseCaseSolution
    extra = 0
    max_num = 1
    readonly_fields = ("image_preview",)
    fields = ("title", "description", "image", "image_preview")


class UseCaseFeatureInline(admin.TabularInline, ImagePreviewMixin):
    model = UseCaseFeature
    extra = 1
    ordering = ("order",)
    readonly_fields = ("image_preview",)
    fields = ("image_preview", "icon", "title", "description", "order")


@admin.register(UseCase)
class UseCaseAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("title", "slug", "date", "tags")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "tags")
    list_filter = ("date",)

    readonly_fields = (
        "tags_icon_preview",
        "date_icon_preview",
        "location_icon_preview",
    )

    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "slug", "banner_image")
        }),
        ("Meta Details", {
            "fields": (
                "tags", "tags_icon", "tags_icon_preview",
                "date", "date_icon", "date_icon_preview",
                "location", "location_icon", "location_icon_preview",
            )
        }),
    )

    inlines = [
        UseCaseChallengeInline,
        UseCaseSolutionInline,
        UseCaseFeatureInline,
    ]

    # -------- ICON PREVIEWS --------

    def tags_icon_preview(self, obj):
        if obj.tags_icon:
            return format_html('<img src="{}" height="50"/>', obj.tags_icon.url)
        return "-"
    tags_icon_preview.short_description = "Tags Icon Preview"

    def date_icon_preview(self, obj):
        if obj.date_icon:
            return format_html('<img src="{}" height="50"/>', obj.date_icon.url)
        return "-"
    date_icon_preview.short_description = "Date Icon Preview"

    def location_icon_preview(self, obj):
        if obj.location_icon:
            return format_html('<img src="{}" height="50"/>', obj.location_icon.url)
        return "-"
    location_icon_preview.short_description = "Location Icon Preview"



@admin.register(IndustryDetail)
class IndustryDetailAdmin(admin.ModelAdmin):
    list_display = ("industry", "product", "use_case")
    autocomplete_fields = ["product", "use_case"]

# ==================================================
# INSIGHTS INTRO
# ==================================================
@admin.register(InsightsIntro)
class InsightsIntroAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

# ==================================================
# MISSION / VISION / VALUE
# ==================================================
@admin.register(MVVSection)
class MVVSectionAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("tab_type", "heading", "image_preview", "order")
    ordering = ("order",)
    list_editable = ("order",)
    list_filter = ("tab_type",)

# ==================================================
# VALUE POINTS (Insights Page)
# ==================================================
@admin.register(ValuePoint)
class ValuePointAdmin(admin.ModelAdmin, ImagePreviewMixin):
    list_display = ("image_preview", "title", "order")
    ordering = ("order",)
    list_editable = ("order",)


class BlogSectionInline(admin.TabularInline):
    model = BlogSection
    extra = 1


class BlogFAQInline(admin.TabularInline):
    model = BlogFAQ
    extra = 1


@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "published_at",
        "updated_at",
        "is_published",
    )

    list_filter = ("is_published", "published_at")
    search_fields = ("title", "meta_title", "meta_keywords")

    prepopulated_fields = {"slug": ("title",)}

    inlines = [BlogSectionInline, BlogFAQInline]