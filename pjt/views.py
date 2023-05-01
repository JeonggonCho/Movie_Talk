from django.shortcuts import render, redirect


# Create your views here.

# 메인 페이지 조회
def main(request):
    return render(request, 'main.html')