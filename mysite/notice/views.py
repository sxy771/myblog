# notice/views.py

from django.views.generic import ListView
from .models import Notice
from django.shortcuts import get_object_or_404, render
from users.decorators import login_message_required

class NoticeListView(ListView):
    model = Notice
    paginate_by = 10
    template_name = 'notice/notice_list.html'  #DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'notice_list'        #DEFAULT : <model_name>_list

    def get_queryset(self):
        notice_list = Notice.objects.order_by('-id')
        return notice_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context


@login_message_required
def notice_detail_view(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {
        'notice': notice,
    }
    return render(request, 'notice/notice_detail.html', context)
