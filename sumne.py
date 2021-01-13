s = "http.request.method == POST"
command = 'tshark -r ' + "filename" + ' -Y ' + 'nskjd'
command = command.split()
command.insert(4, s)
print(command)