
# Created from dockerfile: https://raw.githubusercontent.com/tianon/dockerfiles/master/steam/Dockerfile
from shutit_module import ShutItModule

class steam(ShutItModule):

        def is_installed(self,shutit):
                return False

        def build(self,shutit):
		shutit.send('apt-get update && apt-get install -yq steam-launcher')
		shutit.send('echo \'deb [arch=amd64,i386] http://repo.steampowered.com/steam precise steam\' > /etc/apt/sources.list.d/steam.list && dpkg --add-architecture i386')
		shutit.send('apt-get update && apt-get install -yq libgl1-mesa-dri:i386 libgl1-mesa-glx:i386 libc6:i386')
		shutit.send('apt-get install -yq sudo')
		shutit.send('echo \'steam ALL = NOPASSWD: ALL\' > /etc/sudoers.d/steam && chmod 0440 /etc/sudoers.d/steam')
		shutit.send('adduser --disabled-password --gecos \'Steam\' steam && adduser steam video')
		shutit.send('export HOME=/home/steam')
                return True

	def finalize(self,shutit):
		return True

	def test(self,shutit):
		return True

	def is_installed(self,shutit):
		return False

	def get_config(self,shutit):
		return True

def module():
        return steam(
                'shutit.tk.steam.steam', 782914092.00,
                depends=['shutit.tk.setup']
        )