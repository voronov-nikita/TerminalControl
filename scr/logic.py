from fabric import Connection

def run_command_remotely(command, password, host):
    with Connection(host, connect_kwargs={"password": password}) as c:
        result = c.sudo(command, hide=True)
        return result.stdout.strip()


command_to_run = 'reboot'
remote_password = '1234'
ls = [218, 130, 142]
# for i in ls:
host = f"vnr@192.168.0.22"
output = run_command_remotely(command_to_run, remote_password, host)

print(output)
