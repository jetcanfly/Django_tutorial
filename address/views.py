from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from .models import Address
from django.http import HttpResponse
from django.template import loader, Context
from django.views import generic


class IndexView(generic.ListView):
    model = Address
    template_name = 'address_list.html'

@csrf_exempt
def upload(request):
    file_obj = request.FILES.get('file', None)
    if file_obj:
        import csv
        from io import StringIO
        try:
            csvfile = StringIO(file_obj.read().decode())
            reader = csv.reader(csvfile)
        except:
            return render_to_response('error.html',
                {'message': 'file format should be csv.'})
        for row in reader:
            objs = Address.objects.filter(name=row[0])
            if not objs:
                obj = Address(name=row[0], gender=row[1],
                    telphone=row[2], mobile=row[3], room=row[4])
            else:
                obj = objs[0]
                obj.gender = row[1]
                obj.telphone = row[2]
                obj.mobile = row[3]
                obj.room = row[4]
            obj.save()
        return HttpResponseRedirect('/address/')
    else:
        return render_to_response('error.html',
            {'message': 'You need to upload a file.'})


def output(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'address.csv'
    t = loader.get_template('csv.html')
    objs = Address.objects.all()
    d = []
    for o in objs:
        d.append((o.name, o.gender, o.telphone, o.mobile, o.room))
    c = {'data': d,}
    response.write(t.render(c))
    return response