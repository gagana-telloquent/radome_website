from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost, Industry, Product, UseCase


# =========================
# STATIC PAGES
# =========================
class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ["home", "our_work", "insights", "contact", "blog"]

    def location(self, item):
        return reverse(item)
# =========================
# BLOG POSTS
# =========================
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(is_published=True).order_by("-created_at")

    def lastmod(self, obj):
        return obj.created_at


# =========================
# INDUSTRIES
# =========================
class IndustrySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Industry.objects.all().order_by("id")


# =========================
# PRODUCTS
# =========================
class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Product.objects.all().order_by("id")


# =========================
# USE CASES
# =========================
class UseCaseSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return UseCase.objects.all().order_by("id")