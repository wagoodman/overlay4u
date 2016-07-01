overlayUtils - Tools for dealing with overlayfs in ubuntu (Work in Progress)
============================================================================

Simple way to create an overlayfs in ubuntu within Python.

Note: overlayUtils requires root. Be sure you're aware of that. It's still very much a
work in progress so please use with caution and hopefully on VM that you do not
care about.

Currently Working
-----------------

- Mounting works! (Tested and works)
- Creating a table of mounted filesystems
- Unmounting

Using overlayUtils
---------------

Create an overlay at dest::

    import overlayUtils

    overlay = overlayUtils.mount('dest', 'lower', 'upper')

    overlay.unmount()

If the destination already has something mounted it won't mount again::

    import overlayUtils

    overlay1 = overlayUtils.mount('dest', 'lower', 'upper')

    # This will throw an error.
    overlay2 = overlayUtils.mount('dest', 'lower', 'upper')

List all overlays::

    import overlayUtils

    overlays = overlayUtils.list()
    # Overlays is now a list of all the currently mounted overlays on your
    # system

Grab a previously mounted overlayfs::

    import overlayUtils

    overlay = overlayUtils.get('/some_mount_point')

That's all. It's a relatively simple tool.
