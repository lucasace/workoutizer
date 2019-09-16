import logging

from django.shortcuts import render
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect

from .views import MapView
from .models import Sport, Activity
from .forms import AddActivityForm, EditActivityForm

log = logging.getLogger('wizer.activity_views')


class ActivityView(MapView):
    template_name = "activity/activity.html"

    def get(self, request, activity_id):
        activity = Activity.objects.get(id=activity_id)
        context = super(ActivityView, self).get(request=request, list_of_activities=[activity])
        context['sports'] = Sport.objects.all().order_by('name')
        context['activity'] = activity
        return render(request, self.template_name, context)


def add_activity_view(request):
    sports = Sport.objects.all().order_by('name')
    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return HttpResponseRedirect('/')
        else:
            log.warning(f"form invalid: {form.errors}")
    else:
        form = AddActivityForm()
    return render(request, 'activity/add_activity.html', {'sports': sports, 'form': form})


def edit_activity_view(request, activity_id):
    sports = Sport.objects.all().order_by('name')
    log.debug(f"querying for activity id: {activity_id}")
    activity = Activity.objects.get(id=activity_id)
    form = EditActivityForm(request.POST or None, instance=activity)
    log.debug(f"got form: {form}")
    if request.method == 'POST':
        if form.is_valid():
            log.info(f"got valid form: {form.cleaned_data}")
            form.save()
            return HttpResponseRedirect(f"/activity/{activity_id}")
        else:
            log.warning(f"form invalid: {form.errors}")
    return render(request, 'activity/edit_activity.html', {'form': form, 'sports': sports, 'activity': activity})


class ActivityDeleteView(DeleteView):
    template_name = "activity/activity_confirm_delete.html"
    model = Activity
    slug_field = 'activity_id'
    success_url = "/"

    def get(self, request, *args, **kwargs):
        sports = Sport.objects.all().order_by('name')
        activity = Activity.objects.get(id=kwargs['pk'])
        log.debug(f"my sports: {sports}")
        log.debug(f"activity: {activity}")
        return render(request, self.template_name, {'sports': sports, 'activity': activity})