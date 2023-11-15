from fabric import Connection

def run_command_remotely(command, password):
    with Connection('vnr@192.168.0.21', connect_kwargs={"password": password}) as c:
        result = c.sudo(command, hide=True)
        return result.stdout.strip()


command_to_run = 'shutdown -h now'
remote_password = '1234'
output = run_command_remotely(command_to_run, remote_password)

print(output)
