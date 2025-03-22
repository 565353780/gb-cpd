import subprocess


def runCMD(command: str, mute: bool = False) -> bool:
    try:
        if mute:
            process = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                text=True,
            )
        else:
            process = subprocess.run(
                command,
                shell=True,
                text=True,
            )
    except:
        print('[ERROR][run::runCMD]')
        print('\t run command failed!')
        print('\t command:', command)
        return False

    return True
