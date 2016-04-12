# How to setup Travis-CI

[Travis-CI][travis-ci] is a continuous integration platform, that integrates well
with GitHub.

Continuous integration is key to ensure confidence for maintainers
and instant feedback for contributors.

Travis-CI is free for OpenSource projects. We encourage you to use it
for your private projects as well and support them to tests all the
OpenSource packages you rely on every day. 

## Setup

We have an [example file](examples/.travis.yaml) that includes all tests
that and it's setup that to ensure Django-CC conformity.

You can simply copy the file and adopt your test command.

Next head over to [`travis-ci.org`](https://travis-ci.org/) and enable
test builds for your repository.

If you have the [travis command line tool][travis-cli] installed you can simply run:

```shell
travis enable
```

## Automatic PyPi deployment

Travis-CI has support for
[PyPi deployment](https://docs.travis-ci.com/user/deployment/pypi/).

Make sure you have the
[travis command line tool][travis-cli]
installed.

Next you can setup the deployment with an easy setup script.

```shell
travis setup pypi
```

Type in your PyPi username and password and answer all questions
with yes.

Once you're done, you'll find a new deployment section in your travis
configuration. Similar to this:

```yaml
deploy:
  provider: pypi
  user: codingjoe
  password:
    secure: some very long string
  on:
    tags: true
    distributions: sdist bdist_wheel
    repo: codingjoe/django-cc
```

Make sure you password is not stored securely and commit the change.

**Note:** You will still have to increase your version number yourself.
Make sure you increased your version number and mark the commit you
would like to commit as a tag. Also don't forget to push the tag to
GitHub.

```shell
git tag 1.1.2 -m "Minor fixes"
git push --tags
```

Travis-CI will now do the PyPi deployment for you!

[travis-cli]: https://github.com/travis-ci/travis.rb#installation
[travis-ci]: https://travis-ci.org/
