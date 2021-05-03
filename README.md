# Todo manager

An example of using TDD to implement a TODO manager
that looks like this:

```
>>> + Apprendre Python
1 [ ] Apprendre Python
>>> + Apprendre TDD
1 [ ] Apprendre Python
2 [ ] Apprendre TDD
>>> x 1
1 [x] Apprendre Python
2 [ ] Apprendre TDD
>>> x 2
1 [x] Apprendre Python
2 [x] Apprendre TDD
>>> o 1
1 [ ] Apprendre Python
2 [x] Apprendre TDD
>>> - 1
2 [x] Apprendre TDD
```

## How to fork this project

* Visit https://github.com/dmerejkowsky/todos-tdd
* Click on "fork" (top-right button)

```bash
# Clone your fork
git clone https://github.com/yourname-todos-tdd

# Add the 'upstream' remote
git remote add upstream https://git@github.com/dmerejkowsky/todos-tdd.git
# Fetch it
git fetch upstream

# Configure the local 'master' branch to track the remote 'master' branch f
# from upstream
git branch --set-upstream-to=upstream/master
```

Now, if you are on the `master` branch, you can run `git pull` to synchronize changes
from upstream.

You can also create a new branch like `your-name` and push it to your fork

```bash
git checkout your-name
# Change files, make commit
git push origin your-name
```

