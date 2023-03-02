from typing import Dict, Any, List
from django.views.generic import ListView, CreateView, FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddBookForm
from .models import *
from django.shortcuts import render, redirect
import xlwt
from django.db import connection
from django.http import  HttpResponse, JsonResponse
import datetime
import json
from django.db.models import Q
from django.template import loader
from django.contrib.auth.decorators import login_required

colss: dict[str | Any, str | Any] = {'sem': "Semestr", 'kurs': "Kurs", 'book_name': "Kitob nomi",
                                     'book_author': "Avtor", 'year': "Nash yili", 'isbn': "ISBN",
                                     'printing_office': "Bosmaxona", 'lang': "Til", 'yonalish': "Yo`nalish",
                                     'science': "Fan nomi", 'teacher': "O`qituvchi", 'book_number': "Kitoblar soni",
                                     'elektron_bool': "Kitobxonada mavjud", 'book_url_file': "Fayl url", 'kaf_name': 'Kafedra nomi'}

def export_excel_xls(request):
    q_sem = request.GET.get('f_sem')
    if q_sem:
        q_sem = f"{q_sem}"
    else:
        q_sem = "%"

    q_kurs = request.GET.get('f_kurs')
    if q_kurs:
        q_kurs = f"{q_kurs}"
    else:
        q_kurs = "%"

    f_yunalish = request.GET.get('f_yunalish')
    if f_yunalish:
        f_yunalish = f"{f_yunalish}"
    else:
        f_yunalish = "%"

    f_lang = request.GET.get('f_lang')
    if f_lang:
        f_lang = f"{f_lang}"
    else:
        f_lang = "%"

    f_kaf = request.GET.get('f_kaf')
    if f_kaf:
        f_kaf = f"{f_kaf}"
    else:
        f_kaf = "%"

    columns = ["№",]
    rows_name = []
    to_str = ''
    for i in colss:
        if request.GET.get(i):
            rows_name.append(i)
            columns.append(colss[i])
    for i in range(len(rows_name)):
        if i == len(rows_name)-1:
            to_str += str(rows_name[i]) + " "
        else:
            to_str += str(rows_name[i]) + ", "
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Adabiyotlar.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(("Adabiyotlar"))
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.borders.bottom = True
    font_style.borders.left = True
    font_style.borders.top = True
    font_style.borders.right = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    sql_query = f"SELECT {to_str} FROM books_books INNER JOIN books_booklanguage ON books_books.lang_id = books_booklanguage.id INNER JOIN books_qanigelik ON books_books.yunalish_id = books_qanigelik.id INNER JOIN books_kafedra ON books_books.kafedra_id = books_kafedra.id WHERE sem LIKE \'{q_sem}\' and kurs LIKE \'{q_kurs}\' and yunalish_id LIKE \'{f_yunalish}\' and kafedra_id LIKE \'{f_kaf}\' and lang_id LIKE \'{f_lang}\' ;"
    print(sql_query)
    cursor = connection.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 0:
                ws.write(row_num, 0, row_num, font_style)
            ws.write(row_num, col_num+1, row[col_num], font_style)
    font_style = xlwt.XFStyle()
    wb.save(response)
    return response

class BookCreateView(LoginRequiredMixin, FormView):
    template_name = "BookCreate.html"
    form_class = AddBookForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
@login_required
def BookList(request):
    q_sem = request.GET.get('Semestr')
    q_kurs = request.GET.get('kurs')
    q_yonalish = request.GET.get('yonalish')
    q_kaf = request.GET.get('kaf')
    if not q_sem:
        q_sem = "%"
    if not q_kurs:
        q_kurs = "%"
    if not q_yonalish:
        q_yonalish = "%"
    if not q_kaf:
        q_kaf = "%"

    template = loader.get_template('BookMyList.html')
    qanigelik = Qanigelik.objects.all()
    lang = BookLanguage.objects.all()
    kafedra = Kafedra.objects.all() 

    book_list = f"SELECT book_name, book_author, kurs, sem  FROM books_books INNER JOIN books_kafedra ON books_books.kafedra_id = books_kafedra.id INNER JOIN books_booklanguage ON books_books.lang_id = books_booklanguage.id INNER JOIN books_qanigelik ON books_books.yunalish_id = books_qanigelik.id WHERE sem LIKE \"{q_sem}\" AND kurs LIKE \"{q_kurs}\" AND yunalish_id LIKE \"{q_yonalish}\" AND kafedra_id LIKE \"{q_kaf}\";"
    cursor = connection.cursor()
    cursor.execute(book_list)
    rows = cursor.fetchall()
    context = {
        'qanigelik': qanigelik,
        'lang': lang,
        'book_list': rows,
        'kaf_list': kafedra,
    }
    return HttpResponse(template.render(context, request))

class BookExportView(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'BookExport.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookExportView, self).get_context_data()
        rowss = colss
        qanigelik = Qanigelik.objects.all()
        lang = BookLanguage.objects.all()
        kafedra = Kafedra.objects.all()
        context['qanigelik'] = qanigelik
        context['rowss'] = rowss
        context['lang'] = lang
        context['kaf_list'] = kafedra
        return context

class search(ListView):
    model = Books
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Books.objects.filter(book_name__icontains=query)
        return object_list