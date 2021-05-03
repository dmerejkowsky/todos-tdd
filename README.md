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

Steps:

1. parsing commands
2. updating the tasks list
3. writing the main loop

