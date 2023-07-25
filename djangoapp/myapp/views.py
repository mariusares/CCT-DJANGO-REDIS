import redis
import json
from datetime import datetime
import subprocess
from django.shortcuts import render, redirect
import socket

r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0)

def get_external_ip():
    return subprocess.check_output(['curl', 'ifconfig.me']).decode().strip()

def message_form_view(request):
    local_ip = socket.gethostbyname(socket.gethostname())
    external_ip = get_external_ip()
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {'name': name, 'message': message, 'timestamp': timestamp}
        r.rpush('messages', json.dumps(data))
        return redirect('message_table')
    return render(request, 'message_form.html', {'local_ip': local_ip, 'external_ip': external_ip})


def message_table_view(request):
    messages = []
    for data in r.lrange('messages', 0, -1):
        messages.append(json.loads(data))
    return render(request, 'message_table.html', {'messages': messages})
