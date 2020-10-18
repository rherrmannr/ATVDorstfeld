from django.views.generic import ListView

from courts.model import Court


class CourtsListView(ListView):
    model = Court
    # model = Post -> wird zu court
    template_name = 'courts/home.html'
    # context_object_name = 'posts'
# ordering = ['-date_posted']
# paginate_by = 5
