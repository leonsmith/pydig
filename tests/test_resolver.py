import pydig

from contextlib import contextmanager


@contextmanager
def _resolver(monkeypatch, expected, response):
    """
    This is our patched resolver context
    """

    def _execute(self, args):
        """
        This is our patched execute method which asserts it was called with the
        correct command args and then subsequently returns the faked response.
        """

        # Check the passed in command matches what we expected
        command = ' '.join(args)
        assert command == expected

        # We encode our response into a byte string as thats what subprocess returns
        return response.encode(self.encoding)

    # Start the pyunit monkeypatch context
    with monkeypatch.context() as context:

        # Inject our custom execute method
        context.setattr('pydig.Resolver._execute', _execute)

        # Yield back, this is what turns our function into a context processor
        yield


def test_query(monkeypatch):
    """
    Tests that the query returns the values we expect
    """

    with _resolver(monkeypatch, 'dig example.com A +short', '127.0.0.1'):
        assert pydig.query('example.com', 'A') == ['127.0.0.1']

    with _resolver(monkeypatch, 'dig example.com TXT +short', '"1"\n"2"'):  # noqa
        assert pydig.query('example.com', 'TXT') == ['"1"', '"2"']

    with _resolver(monkeypatch, 'dig example.com CNAME +short', ''):  # noqa
        assert pydig.query('example.com', 'CNAME') == []


def test_custom_resolver(monkeypatch):
    """
    Tests that the query returns the values we expect
    """

    resolver = pydig.Resolver(
        executable='foo',
        nameservers=['1.1.1.1'],
        additional_args=['+time=10']
    )

    with _resolver(monkeypatch, 'foo @1.1.1.1 example.com A +short +time=10', '127.0.0.1'):
        assert resolver.query('example.com', 'A') == ['127.0.0.1']

    with _resolver(monkeypatch, 'foo @1.1.1.1 example.com TXT +short +time=10', '"1"\n"2"'):
        assert resolver.query('example.com', 'TXT') == ['"1"', '"2"']

    with _resolver(monkeypatch, 'foo @1.1.1.1 example.com CNAME +short +time=10', ''):
        assert resolver.query('example.com', 'CNAME') == []
