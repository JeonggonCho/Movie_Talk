from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.

# 리뷰 인덱스 페이지 조회
def index(request):
    reviews = Review.objects.all().order_by('-created_at')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)


# 리뷰 생성
@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review = form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/review_create.html', context)


# 리뷰 삭제
@login_required
def review_delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('reviews:index')


# 리뷰 수정
@login_required
def review_update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', review_pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('reviews:detail', review_pk)
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'reviews/review_update.html', context)


# 리뷰 디테일
def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    # 댓글 작성 폼
    comment_form = CommentForm()
    # 해당 리뷰에 작성된 모든 댓글(역참조)
    comments = review.comment_set.all().order_by('-created_at')
    comments_cnt = review.comment_set.all().count()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
        'comments_cnt': comments_cnt,
    }
    return render(request, 'reviews/detail.html', context)


# 댓글 생성
@login_required
def comment_create(request, review_pk):
    # 게시글 조회
    review = Review.objects.get(pk=review_pk)
    # 댓글 데이터를 변수에 담아 유효성 검사
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)


# 댓글 삭제
@login_required
def comment_delete(request, review_pk, comment_pk):
    # 삭제할 댓글 조회
    comment = Comment.objects.get(pk=comment_pk)
    # 삭제
    if comment.user == request.user:
        comment.delete()
    return redirect('reviews:detail', review_pk)