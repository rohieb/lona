

Protocol
========


Methods
-------

+---------------+------+----------+-------------------------------------------+
| Name          | Code | Issuer   | Description                               |
+===============+======+==========+===========================================+
| VIEW          | 101  | Frontend |                                           |
+---------------+------+----------+-------------------------------------------+
| INPUT_EVENT   | 102  | Frontend |                                           |
+---------------+------+----------+-------------------------------------------+
| WINDOW_EVENT  | 103  | Frontend | Not implemented yet                       |
+---------------+------+----------+-------------------------------------------+
| REDIRECT      | 201  | Backend  |                                           |
+---------------+------+----------+-------------------------------------------+
| HTTP_REDIRECT | 202  | Backend  |                                           |
+---------------+------+----------+-------------------------------------------+
| HTML          | 203  | Backend  |                                           |
+---------------+------+----------+-------------------------------------------+
| VIEW_START    | 204  | Backend  | Not implemented yet                       |
+---------------+------+----------+-------------------------------------------+
| VIEW_STOP     | 205  | Backend  | Not implemented yet                       |
+---------------+------+----------+-------------------------------------------+
| WINDOW_ACTION | 206  | Backend  | Not implemented yet                       |
+---------------+------+----------+-------------------------------------------+


Examples
''''''''

::

    >> [1, VIEW, 'example.org/foo/bar']
    >> [1, VIEW, 'example.org/foo/bar?foo=bar', {'foo': 'bar'}]

    << [1, REDIRECT, 'example.org/foo/bar']

    << [1, HTML, 'example.org/foo/bar', '<div id="foo"></div>', $INPUT_EVENTS]
    << [1, HTML, 'example.org/foo/bar', {'foo': {}},            $INPUT_EVENTS]

    >> [1, INPUT_EVENT, 'example.org/foo/bar', $EVENT_PAYLOAD]


Input Events
------------

+---------------+------+------------------------------------------------------+
| Name          | Code | Description                                          |
+===============+======+======================================================+
| CLICK         | 301  | onClick()                                            |
+---------------+------+------------------------------------------------------+
| CHANGE        | 302  | onChange()                                           |
+---------------+------+------------------------------------------------------+
| SUBMIT        | 303  | form.submit()                                        |
+---------------+------+------------------------------------------------------+


Examples
''''''''

::

    >> [1, INPUT_EVENT, 'example.org/foo/bar', CLICK, $DATA, 1600156474948232]

    >> [1, INPUT_EVENT, 'example.org/foo/bar', 'custom-event-name', $DATA,
        1600156474948232]

    >> [1, INPUT_EVENT, 'example.org/foo/bar', CLICK, $DATA,
        None, $TAG_NAME, $DIV_ID, $DIV_CLASS]


Window Events
-------------

+---------------+------+------------------------------------------------------+
| Name          | Code | Description                                          |
+===============+======+======================================================+
| CLOSE         | 401  | Not implemented yet                                  |
+---------------+------+------------------------------------------------------+
| BLUR          | 402  | Not implemented yet                                  |
+---------------+------+------------------------------------------------------+
| FOCUS         | 403  | Not implemented yet                                  |
+---------------+------+------------------------------------------------------+
| RESIZE        | 404  | Not implemented yet                                  |
+---------------+------+------------------------------------------------------+


Examples
''''''''

::

    >> [1, WINDOW_EVENT, 'example.org/foo/bar', CLOSE]
    >> [1, WINDOW_EVENT, 'example.org/foo/bar', RESIZE, $DATA]
