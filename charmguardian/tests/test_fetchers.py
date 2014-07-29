import unittest

from ..fetchers import (
    BzrFetcher,
    BzrMergeProposalFetcher,
    GithubFetcher,
    BitbucketFetcher,
    LocalFetcher,
    CharmstoreDownloader,
    BundleDownloader,
)


class BzrFetcherTest(unittest.TestCase):
    def test_can_fetch(self):
        f = BzrFetcher.can_fetch

        good_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo'),
            f('launchpad:~tvansteenburgh/charms/precise/foo'),
            f('http://launchpad.net/~tvansteenburgh/charms/precise/foo'),
            f('https://launchpad.net/~tvansteenburgh/charms/precise/foo'),
            f('http://www.launchpad.net/~tvansteenburgh/charms/precise/foo'),
            f('https://www.launchpad.net/~tvansteenburgh/charms/precise/foo'),
            f('http://code.launchpad.net/~tvansteenburgh/charms/precise/foo'),
            f('https://code.launchpad.net/~tvansteenburgh/charms/precise/foo'),
        ]

        bad_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo/+merge/12345'),
            f('gh:charms/meteor'),
            f('bb:charms/meteor'),
            f('local:~/src/charms/precise/meteor'),
            f('cs:precise/meteor'),
            f('bundle:mediawiki/single'),
        ]

        for test in good_tests:
            self.assertEqual(
                test['repo'],
                '~tvansteenburgh/charms/precise/foo')

        for test in bad_tests:
            self.assertEqual(test, {})


class BzrMergeProposalFetcherTest(unittest.TestCase):
    def test_can_fetch(self):
        f = BzrMergeProposalFetcher.can_fetch

        good_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo/+merge/12345'),
        ]

        bad_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo'),
            f('gh:charms/meteor'),
            f('bb:charms/meteor'),
            f('local:~/src/charms/precise/meteor'),
            f('cs:precise/meteor'),
            f('bundle:mediawiki/single'),
        ]

        for test in good_tests:
            self.assertEqual(
                test['repo'],
                '~tvansteenburgh/charms/precise/foo/+merge/12345')

        for test in bad_tests:
            self.assertEqual(test, {})


class GithubFetcherTest(unittest.TestCase):
    def test_can_fetch(self):
        f = GithubFetcher.can_fetch

        good_tests = [
            f('gh:charms/meteor'),
            f('github:charms/meteor'),
            f('http://github.com/charms/meteor'),
            f('https://github.com/charms/meteor'),
            f('http://www.github.com/charms/meteor'),
            f('https://www.github.com/charms/meteor'),
        ]

        bad_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo'),
            f('lp:~tvansteenburgh/charms/precise/foo/+merge/12345'),
            f('bb:charms/meteor'),
            f('local:~/src/charms/precise/meteor'),
            f('cs:precise/meteor'),
            f('bundle:mediawiki/single'),
        ]

        for test in good_tests:
            self.assertEqual(test['repo'], 'charms/meteor')

        for test in bad_tests:
            self.assertEqual(test, {})


class BitbucketFetcherTest(unittest.TestCase):
    def test_can_fetch(self):
        f = BitbucketFetcher.can_fetch

        good_tests = [
            f('bb:charms/meteor'),
            f('bitbucket:charms/meteor'),
            f('http://bitbucket.org/charms/meteor'),
            f('https://bitbucket.org/charms/meteor'),
            f('http://www.bitbucket.org/charms/meteor'),
            f('https://www.bitbucket.org/charms/meteor'),
        ]

        bad_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo'),
            f('lp:~tvansteenburgh/charms/precise/foo/+merge/12345'),
            f('gh:charms/meteor'),
            f('local:~/src/charms/precise/meteor'),
            f('cs:precise/meteor'),
            f('bundle:mediawiki/single'),
        ]

        for test in good_tests:
            self.assertEqual(test['repo'], 'charms/meteor')

        for test in bad_tests:
            self.assertEqual(test, {})


class LocalFetcherTest(unittest.TestCase):
    def test_can_fetch(self):
        f = LocalFetcher.can_fetch

        good_tests = [
            f('local:~/src/charms/precise/meteor'),
        ]

        bad_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo'),
            f('lp:~tvansteenburgh/charms/precise/foo/+merge/12345'),
            f('gh:charms/meteor'),
            f('bb:charms/meteor'),
            f('cs:precise/meteor'),
            f('bundle:mediawiki/single'),
        ]

        for test in good_tests:
            self.assertEqual(test['path'], '~/src/charms/precise/meteor')

        for test in bad_tests:
            self.assertEqual(test, {})


class CharmstoreDownloaderTest(unittest.TestCase):
    def test_can_fetch(self):
        f = CharmstoreDownloader.can_fetch

        good_tests = [
            f('cs:precise/meteor'),
        ]

        bad_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo'),
            f('lp:~tvansteenburgh/charms/precise/foo/+merge/12345'),
            f('gh:charms/meteor'),
            f('bb:charms/meteor'),
            f('local:~/src/charms/precise/meteor'),
            f('bundle:mediawiki/single'),
        ]

        for test in good_tests:
            self.assertEqual(test['charm'], 'precise/meteor')

        for test in bad_tests:
            self.assertEqual(test, {})


class BundleDownloaderTest(unittest.TestCase):
    def test_can_fetch(self):
        f = BundleDownloader.can_fetch

        good_tests = [
            f('bundle:mediawiki/single'),
        ]

        bad_tests = [
            f('lp:~tvansteenburgh/charms/precise/foo'),
            f('lp:~tvansteenburgh/charms/precise/foo/+merge/12345'),
            f('gh:charms/meteor'),
            f('bb:charms/meteor'),
            f('local:~/src/charms/precise/meteor'),
            f('cs:precise/meteor'),
        ]

        for test in good_tests:
            self.assertEqual(test['bundle'], 'mediawiki/single')

        for test in bad_tests:
            self.assertEqual(test, {})
