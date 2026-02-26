from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # PUBLIC WEBSITE PAGES
    # =========================
    path("", views.home, name="home"),
    path("our-works/", views.our_work, name="our_work"),
    path("our-work/<slug:slug>/", views.industry_detail, name="industry_detail"),
    path("insights/", views.insights, name="insights"),
    path("contact/", views.contact, name="contact"),

    # Products & Use Cases
    path("products/<slug:slug>/", views.product_detail, name="product_detail"),
    path("use-cases/<slug:slug>/", views.use_case_detail, name="use_case_detail"),

    # =========================
    # PUBLIC BLOG (Frontend)
    # =========================
    path("blog/", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),

#     # =========================
#     # BLOG DASHBOARD (Admin)
#     # =========================
    path("dashboard/", views.blog_dashboard, name="blog_dashboard"),
    path("dashboard/login/", views.blog_login, name="blog_login"),
    path("dashboard/logout/", views.blog_logout, name="blog_logout"),

#     # Blog Post CRUD
     path("dashboard/posts/create/", views.create_post, name="create_post"),
   path("dashboard/posts/<int:post_id>/edit/", views.edit_blog_post, name="edit_blog_post"),
    path("dashboard/posts/<int:post_id>/delete/", views.delete_blog_post, name="delete_blog_post"),

    # Blog Sections
    path("dashboard/posts/<int:post_id>/sections/add/", views.add_blog_section, name="add_blog_section"),
    path("dashboard/sections/<int:section_id>/edit/", views.edit_blog_section, name="edit_blog_section"),
    path("dashboard/sections/<int:section_id>/delete/", views.delete_blog_section, name="delete_blog_section"),
    path('dashboard/authors/create/', views.create_author, name='create_author'),

    path("post/<int:post_id>/update-order/",views.update_section_order,name="update_section_order"),

    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
]

