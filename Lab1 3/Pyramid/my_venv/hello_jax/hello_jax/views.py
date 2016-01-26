from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'Witome!'}

@view_config(route_name='generate_ajax_data', renderer='json')                     #1
def my_ajax_view(request):                                                         #2
    return {'message': "Ajax pozwala na robienie niewiarygodnie fajnych rzeczy!"}
