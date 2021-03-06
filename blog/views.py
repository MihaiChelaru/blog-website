from blog.models import SiteTags
from dal import autocomplete
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from markdownx.utils import markdownify

from .models import Post


# Views for blog app
def post_list(request):
    """
    View function for viewing a list of the 10 most recent posts.
    """
    posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
    return render(request, 'blog/post_list.html', {"posts": posts})


def post_detail(request, post_id, slug):
    """
    View function for viewing an individual blog post. Redirects to the correct slug if it is improperly entered.
    :param request:
    :param post_id:
    :param slug:
    :return:
    """
    # Checks if the slug in the URL matches the database, and if not redirects to the correct slug URL
    post = get_object_or_404(Post, pk=post_id)
    if post.slug != slug:
        return redirect('blog:post-detail', post_id=post.pk, slug=post.slug)
    author = post.author
    # markdownify() content and display on page
    post.content = markdownify(post.content)

    context = {
        'post': post,
        'author': author,
    }
    return render(request, 'blog/post_detail.html', context)


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SiteTags.objects.all()

        if self.q:
            qs = qs.filter(slug__icontains=self.q).order_by('slug')

        return qs
