# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from logistica.models import Actividad


@login_required
def activities(request):
    context = {
        'activities': generate_activity_id_list(),
    }
    return render(request, 'app/activity.html', context)


def generate_activity_id_list():
    all_activities = Actividad.objects.all()
    return all_activities


def edit_activity_capacity(request):
    pk_activity = request.POST.get("id")
    ca_activity = int(request.POST.get("capacidadActual"))
    ans = {
        'status': False,
        'msg': ''
    }

    if pk_activity == -1:
        ans['msg'] = 'Escoja actividad válida'
        return JsonResponse(ans)

    activity = Actividad.objects.filter(pk=pk_activity)
    if not activity.exists():
        ans['msg'] = 'Actividad con dicho ID no existe'
        return JsonResponse(ans)

    activity = Actividad.objects.get(pk=pk_activity)
    if activity.capacidadTotal < ca_activity:
        ans['msg'] = 'No puede existir sobrecapacidad!'
        return JsonResponse(ans)
    activity.capacidadActual = ca_activity
    activity.save()
    ans['status'] = True
    return JsonResponse(ans)
