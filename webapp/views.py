from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm,BlogPostForm, BlogSectionForm
from django.utils.text import slugify
from django.db.models import Max
from django.db.models import F
import json
from django.http import JsonResponse



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
    UseCaseChallenge,
    UseCaseSolution,
    UseCaseFeature,
    InsightsIntro,      # ✅ ADD
    MVVSection,         # ✅ ADD
    ValuePoint, 
    BlogPost,
    BlogSection,
    BlogFAQ,
    BlogAuthor,

)

def home(request):
    # Hero
    hero = PageBanner.objects.filter(page="home").first()
    intro = Intro.objects.first()
    # Existing sections (unchanged)
    stats = CompanyStat.objects.all()
    what_we_do_image = WhatWeDoImage.objects.first()
    what_we_do_items = WhatWeDoItem.objects.all()
    value_cards = ValueCard.objects.all()
    portfolio_images = PortfolioImage.objects.all()
    reel_video = ReelVideo.objects.first()
    team_members = TeamMember.objects.all()
    achievements = Achievement.objects.all()
    media_gallery = MediaGallery.objects.all()
    achievement_highlight = AchievementHighlight.objects.first()

    context = {
        "hero": hero,
        "intro": intro,
        "stats": stats,
        "what_we_do_image": what_we_do_image,
        "what_we_do_items": what_we_do_items,
        "value_cards": value_cards,
        "portfolio_images": portfolio_images,
        "reel_video": reel_video,
        "team_members": team_members,
        "achievements": achievements,
        "media_gallery": media_gallery,
        "achievement_highlight": achievement_highlight,
    }

    return render(request, "home.html", context)

def our_work(request):
    hero = PageBanner.objects.filter(page="our_work").first()

    industries = Industry.objects.all()
    ai_core_cards = AICoreCard.objects.all()

    context = {
        "hero": hero,
        "industries": industries,
        "ai_core_cards": ai_core_cards,

    }

    return render(request, "our-work.html", context)

def industry_detail(request, slug):
    industry = get_object_or_404(Industry, slug=slug)
    detail = IndustryDetail.objects.filter(industry=industry).first()

    context = {
        "industry": industry,
        "detail": detail,
    }

    return render(request, "industry_detail.html", context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)


    context = {
        "product": product,
    }

    return render(request, "proHM.html", context)

def use_case_detail(request, slug):
    use_case = get_object_or_404(UseCase, slug=slug)

    # Related Data
    challenge = getattr(use_case, "challenge", None)
    solution = getattr(use_case, "solution", None)
    features = use_case.features.all()

    context = {
        "use_case": use_case,
        "challenge": challenge,
        "solution": solution,
        "features": features,
    }

    return render(request, "use_case_detail.html", context)

def insights(request):
    hero = PageBanner.objects.filter(page="insights").first()
    intro = InsightsIntro.objects.first()

    mission = MVVSection.objects.filter(tab_type="mission").first()
    vision = MVVSection.objects.filter(tab_type="vision").first()
    value = MVVSection.objects.filter(tab_type="value").first()

    value_points = ValuePoint.objects.all()
    team_members = TeamMember.objects.all()

    context = {
        "hero": hero,
        "intro": intro,
        "mission": mission,
        "vision": vision,
        "value": value,
        "value_points": value_points,
        "team_members": team_members,
    }

    return render(request, "insights.html", context)

def blog(request):
    hero = PageBanner.objects.filter(page="blog").first()

    posts = BlogPost.objects.filter(is_published=True)

    context = {
        "hero": hero,
        "posts": posts,
    }

    return render(request, "blog.html", context)

from django.http import Http404

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    preview = request.GET.get("preview") == "1"

    # Draft protection
    if not post.is_published:
        if not (preview and request.user.is_authenticated):
            raise Http404("Post not found")

    sections = post.sections.all()
    faqs = post.faqs.all()

    return render(request, "blog_detail.html", {
        "post": post,
        "sections": sections,
        "faqs": faqs,
        "preview_mode": preview
    })


def contact(request):
    hero = PageBanner.objects.filter(page="contact").first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            full_message = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}

            Message:
            {message}
            """

            send_mail(
                subject="New Contact Form Submission",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["sales@radometech.com"],
            )

            messages.success(request, "Message sent successfully!")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "hero": hero,
        "form": form
    })
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def blog_dashboard(request):
    posts = BlogPost.objects.select_related('author') \
        .prefetch_related('sections') \
        .order_by('-created_at')

    # ---- SEARCH ----
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(short_description__icontains=search_query)
        )

    # ---- FILTER ----
    status_filter = request.GET.get('status')
    if status_filter == "published":
        posts = posts.filter(is_published=True)
    elif status_filter == "draft":
        posts = posts.filter(is_published=False)

    # ---- COUNTS ----
    total_posts = BlogPost.objects.count()
    published_count = BlogPost.objects.filter(is_published=True).count()
    draft_count = BlogPost.objects.filter(is_published=False).count()

    # ---- PAGINATION ----
    paginator = Paginator(posts, 5)  # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/dashboard.html', {
        'page_obj': page_obj,
        'posts': page_obj,
        'posts_count': total_posts,
        'published_count': published_count,
        'draft_count': draft_count,
        'status_filter': status_filter,
        'search_query': search_query,
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            base_slug = slugify(post.title)
            slug = base_slug
            counter = 1

            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            post.slug = slug
            post.save()

            messages.success(request, "Blog post created successfully!")
            return redirect('blog_dashboard')
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_post.html', {
        'form': form,
    })


@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            updated_post = form.save(commit=False)

            # Unique slug logic (excluding current post)
            base_slug = slugify(updated_post.title)
            slug = base_slug
            counter = 1

            while BlogPost.objects.filter(slug=slug).exclude(id=post.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            updated_post.slug = slug
            updated_post.save()

            messages.success(request, "Blog post updated successfully!")
            return redirect("blog_dashboard")
    else:
        form = BlogPostForm(instance=post)

    return render(request, "blog/edit_blog_post.html", {
        "form": form,
        "post": post,
        "sections": post.sections.all().order_by("order"),
    })


@login_required
def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Blog post deleted successfully!")
        return redirect("blog_dashboard")

    return render(request, "blog/delete_blog_post.html", {"post": post})


@login_required
def add_blog_section(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == "POST":
        form = BlogSectionForm(request.POST, request.FILES)

        if form.is_valid():
            section = form.save(commit=False)
            section.blog = post

            if section.order:
                # If user gives order → shift others down
                post.sections.filter(order__gte=section.order).update(
                    order=F('order') + 1
                )
            else:
                # If order = 0 → append to end
                max_order = post.sections.aggregate(Max("order"))["order__max"] or 0
                section.order = max_order + 1

            section.save()  # ✅ MUST SAVE ALWAYS

            messages.success(request, "Section saved successfully!")

            action = request.POST.get("action")

            if action == "save_add":
                return redirect("add_blog_section", post_id=post.id)

            return redirect("edit_blog_post", post_id=post.id)

    else:
        form = BlogSectionForm()

    return render(request, "blog/add_blog_section.html", {
        "form": form,
        "post": post
    })

   
@login_required
def edit_blog_section(request, section_id):
    section = get_object_or_404(BlogSection, id=section_id)
    post = section.blog

    if request.method == "POST":
        form = BlogSectionForm(request.POST, request.FILES, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, "Section updated successfully!")
            return redirect("edit_blog_post", post_id=post.id)
    else:
        form = BlogSectionForm(instance=section)

    return render(request, "blog/edit_blog_section.html", {
        "form": form,
        "section": section,
        "post": post
    })


@login_required
def delete_blog_section(request, section_id):
    section = get_object_or_404(BlogSection, id=section_id)
    post = section.blog
    deleted_order = section.order

    if request.method == "POST":
        section.delete()

        # Shift remaining sections up
        post.sections.filter(order__gt=deleted_order).update(
            order=F('order') - 1
        )

        messages.success(request, "Section deleted successfully!")

    return redirect("edit_blog_post", post_id=post.id)


# =========================================================
# AUTH
# =========================================================

def blog_login(request):
    if request.user.is_authenticated:
        return redirect("blog_dashboard")

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect("blog_dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "blog/login.html")


def blog_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("blog_login")

@login_required
def create_author(request):
    if request.method == "POST":
        name = request.POST.get("name")
        bio = request.POST.get("bio")
        image = request.FILES.get("image")

        BlogAuthor.objects.create(
            name=name,
            bio=bio,
            image=image
        )

        messages.success(request, "Author created successfully!")
        return redirect("create_post")

    return render(request, "blog/create_author.html")

def update_section_order(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(BlogPost, id=post_id)
        data = json.loads(request.body)

        for item in data.get("order", []):
            post.sections.filter(id=item["id"]).update(order=item["order"])

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"}, status=400)

def privacy_policy(request):
    return render(request, "privacy_policy.html")