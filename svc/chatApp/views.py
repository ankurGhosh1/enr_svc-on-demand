from django.shortcuts import render, redirect, reverse
from svc.utils import AllProcedures, FastProcedures



def chat(request, user_id, job_id):
    chatRoom = None
    messages = []
    if request.session.has_key('user'):
        user = AllProcedures.getUserWithId(user_id)[0]
        name = user['first_name']
        my_id = request.session['user']['id']
        if not request.session['user']['type']=="Professional":
            room_name = f'chat{user_id}{my_id}-{job_id}-s'
            messages = AllProcedures.getChatRecord(client_id=my_id, professional_id=user_id, room_name=room_name)
            professional_id = user_id
            client_id = my_id
            messages = [(i[0], i[1], name) for i in messages]
        else:
            room_name = f'chat{my_id}{user_id}-{job_id}-s'
            messages = AllProcedures.getChatRecord(client_id=user_id, professional_id=my_id, room_name=room_name)
            professional_id = my_id
            client_id = user_id
            messages = [(i[0], not i[1], name) for i in messages]
        job = AllProcedures.getJobById(job_id)
        context = {
            'senderId': (user_id, name),
            'room_name':room_name,
            'messages': messages,
            'professional_id':professional_id,
            'client_id':client_id,
            'job':job[0]
        }
        return render(request, 'chatApp/chatroom.html', context)
    return redirect('accounts:login')


def chatApp(request):
    if request.session['user'] and request.session['user']['type']=='Client':
        my_id = request.session['user']['id']
        connections = AllProcedures.getClientConnections(user_id=my_id)
    elif request.session['user'] and request.session['user']['type']=='Professional':
        my_id = request.session['user']['id']
        connections = AllProcedures.getProfessionalConnections(user_id=my_id)
    # connections = list(set(connections))
    print(connections)
    return render(request, 'chatApp/chatApp.html', {'connections':connections})
