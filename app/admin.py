from django.contrib import admin
from django import forms
from django.shortcuts import render, redirect
from django.urls import path, reverse
from django.http import JsonResponse
from django.contrib.admin import site
from .models import News, NewsImage, Category, SubCategory, Advertisement, Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "email", "phone_no", "logo")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name",)
    ordering = ("id",)


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    fields = ["image"]


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "description",
            "image",
            "video",
            "category",
            "sub_category",
            "is_video",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "video": forms.URLInput(attrs={"placeholder": "Enter video URL"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sub_category"].queryset = SubCategory.objects.none()

        # If we have an instance and category is set
        if self.instance and self.instance.pk and self.instance.category:
            self.fields["sub_category"].queryset = SubCategory.objects.filter(
                category=self.instance.category
            )

        # If form data is passed and category is selected
        if args and args[0] and "category" in args[0]:
            try:
                category_id = int(args[0]["category"])
                self.fields["sub_category"].queryset = SubCategory.objects.filter(
                    category_id=category_id
                )
            except (ValueError, TypeError):
                pass

    def clean(self):
        cleaned_data = super().clean()
        is_video = cleaned_data.get("is_video")
        video = cleaned_data.get("video")
        image = cleaned_data.get("image")

        if is_video and not video:
            self.add_error("video", "Video URL is required when is_video is selected.")
        elif not is_video and not image:
            self.add_error("image", "Image is required when is_video is not selected.")

        return cleaned_data


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    inlines = [NewsImageInline]
    list_display = [
        "title",
        "category",
        "sub_category",
        "is_video",
        "created_at",
        "updated_at",
    ]
    list_filter = ["category", "is_video", "created_at"]
    search_fields = ["title", "description"]
    date_hierarchy = "created_at"
    readonly_fields = ["created_at", "updated_at"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "add/",
                self.admin_site.admin_view(self.add_news_view),
                name="news_news_add",
            ),
            path(
                "get_subcategories/",
                self.admin_site.admin_view(self.get_subcategories),
                name="get_subcategories",
            ),
            path(
                "delete_news_image/",
                self.admin_site.admin_view(self.delete_news_image),
                name="delete_news_image",
            ),
        ]
        return custom_urls + urls

    def get_subcategories(self, request):
        category_id = request.GET.get("category_id")
        if category_id:
            subcategories = SubCategory.objects.filter(category_id=category_id).values(
                "id", "name"
            )
            return JsonResponse(list(subcategories), safe=False)
        return JsonResponse([], safe=False)

    def delete_news_image(self, request):
        image_id = request.GET.get("image_id")
        if image_id:
            try:
                news_image = NewsImage.objects.get(id=image_id)
                news_image.delete()
                return JsonResponse({"success": True})
            except NewsImage.DoesNotExist:
                pass
        return JsonResponse({"success": False})

    def add_news_view(self, request):
        if request.method == "POST":
            form = self.form(request.POST, request.FILES)
            if form.is_valid():
                news = form.save()

                # Handle additional images
                news_images = request.FILES.getlist("news_images")
                for image in news_images:
                    NewsImage.objects.create(news=news, image=image)

                self.message_user(request, "News created successfully.")
                if "_addanother" in request.POST:
                    return redirect(reverse("admin:news_news_add"))
                elif "_continue" in request.POST:
                    return redirect(reverse("admin:news_news_change", args=[news.pk]))
                else:
                    return redirect(reverse("admin:news_news_changelist"))
        else:
            form = self.form()

        context = {
            "form": form,
            "categories": Category.objects.all(),
            "opts": self.model._meta,
            "has_view_permission": self.has_view_permission(request),
            "has_add_permission": self.has_add_permission(request),
            "has_change_permission": self.has_change_permission(request),
            "has_delete_permission": self.has_delete_permission(request),
            "app_label": self.model._meta.app_label,
        }
        return render(request, "admin/app/news/add_form.html", context)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active", "img", "link")
    search_fields = ("link",)
    ordering = ("id",)
