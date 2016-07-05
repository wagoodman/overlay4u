from .overlay import OverlayFS, OverlayFSManager, OverlayFSDoesNotExist

import os

def mount(directory, lower_dir, upper_dir, working_dir=None, readonly=False, mount_table=None):
    return OverlayFS.mount(directory, lower_dir, upper_dir, working_dir, readonly,
            mount_table=mount_table)

def umount(mount_point, mount_table=None):
    overlays = OverlayFSManager.list(mount_table=mount_table)
    for overlay in overlays:
        if os.path.samefile(overlay.mount_point, mount_point):
            overlay.unmount()


def list(mount_table=None):
    return OverlayFSManager.list(mount_table=mount_table)

def get(mount_point, mount_table=None):
    return OverlayFSManager.get(mount_point, mount_table=mount_table)

def isMounted(mount_point, mount_table=None):

    overlays = OverlayFSManager.list(mount_table=mount_table)
    for overlay in overlays:
        if os.path.samefile(overlay.mount_point, mount_point):
            return True
    return False
