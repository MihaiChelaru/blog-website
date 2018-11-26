from django.shortcuts import render, get_object_or_404, redirect
from markdownx.utils import markdownify

from .models import Review


def review_detail(request, review_id, slug):
    """
    View function for viewing an individual blog post. Redirects to the correct slug if it is improperly entered.
    :param request:
    :param post_id:
    :param slug:
    :return:
    """
    # Checks if the slug in the URL matches the database, and if not redirects to the correct slug URL
    review = get_object_or_404(Review, pk=review_id)
    if review.slug != slug:
        return redirect('reviews:review-detail', post_id=review.pk, slug=review.slug)
    author = review.review_author
    resource_type = review.resource_type
    # markdownify() content and display on page
    review.content = markdownify(review.content)
    return render(request, 'reviews/review_detail.html', {'review': review, 'author': author, 'resource_type': resource_type})


def book_list(request):
    """
    View function for viewing book reviews by category.
    """
    books = Review.objects.filter(resource_type__name__exact="Book")
    ml_books = books.objects.filter(tags="machine-learning")
    return render(request, 'reviews/book_reviews.html', {"ml_books": ml_books})