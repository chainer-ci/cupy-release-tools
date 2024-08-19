import shlex
import subprocess
import sys

import cupy


def main():
    if cupy.cuda.runtime.is_hip:
        return

    # Only install if CUDA 12.2+.
    (major, minor) = cupy.cuda.nvrtc.getVersion()
    if major == 11:
        return
    elif major == 12:
        if minor < 2:
            return
    else:
        assert False, f'Unsupported CUDA version: {major}.{minor}'

    cmdline = [
        sys.executable, '-m', 'pip', 'install', '--user',
        f'nvidia-cuda-runtime-cu{major}=={major}.{minor}.*',
    ]
    print(f'Running: {shlex.join(cmdline)}')
    subprocess.run(cmdline, check=True)


if __name__ == '__main__':
    main()
