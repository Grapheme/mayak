# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from yugregion.shanson_advertisers.forms import ManagerConnectForm
from yugregion.shanson_advertisers.models import Managers, Shanson_Action, Research, Partners

def manager_list(request):
    manager_list = Managers.objects.all().order_by('weight')
    connect_form = ManagerConnectForm(request.GET or None)
    return render_to_response("advertisers/shanson_manager_list.html", RequestContext(request, {
    	'manager_list': manager_list,
    	'connect_form': connect_form,
    }))

def action_list(request):
    action_list = Shanson_Action.objects.published()
    return render_to_response("advertisers/shanson_action_list.html", RequestContext(request, {
    	'action_list': action_list,
    }))

def action_detail(request, action_id=1):
    action = get_object_or_404(Shanson_Action, id=action_id)
    return render_to_response("advertisers/shanson_action_detail.html", RequestContext(request, {
    	'action': action,
    }))

def research(request):
    try: research = Research.objects.published()[0]
    except IndexError: raise Http404
    return render_to_response("advertisers/shanson_research.html", RequestContext(request, {
    	'research': research,
    }))

def manager_connect(request):
    connect_form = ManagerConnectForm(request.POST or None)
    if connect_form.is_valid():
        connect_form.save()
    context = RequestContext(request)
    context['connect_form'] = connect_form
    response = render_to_response('feedback/manager_connect_form.html', context)
    response.set_cookie('manager_connect_result', connect_form.is_valid())
    return response

def partners(request):
    partners_list = Partners.objects.published()
    return render_to_response("advertisers/shanson_partners_list.html", RequestContext(request, {
        'partners_list': partners_list,
    }))

#EOF