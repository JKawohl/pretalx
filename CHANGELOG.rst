Changelog
=========

This changelog contains the changes to be released in the **next** release.
For older changelogs, please visit our releases_ page.

vx.x.x
------

*Released on 2018-xx-xx*


Breaking Changes
~~~~~~~~~~~~~~~~

None.

Features
~~~~~~~~

- The API now exports links to submission images and speaker avatars.
- Organisers can configure a list of talks to be shown as "sneak peek" before the first schedule is released.
- Submitters can share a submission via a read-only link.

Fixed bugs
~~~~~~~~~~~

- An issue resulting in an empty HTML export was fixed.
- HTML exports failed if a talk was canceled.
- When accessing a confirmation link unauthenticated, a 404 page was shown instead of a login page.
- The API always showed the speaker biography as empty.
- The "Mark speaker arrived" button is now only shown during and slightly before the event. (#441)

.. _releases: https://github.com/pretalx/pretalx/releases
