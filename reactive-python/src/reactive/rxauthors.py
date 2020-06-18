import rx
from rx import Observable, operators as ops, from_, just

articles = [
    {"post_id": 1, "author_id": 1, "title": "title1"},
    {"post_id": 2, "author_id": 2, "title": "title2"},
    {"post_id": 3, "author_id": 2, "title": "title1"}
]

authors = [
    {"author_id": 1, "name": "AA"},
    {"author_id": 2, "name": "BB"}
]

# from_(articles).pipe(
#     ops.flat_map(
#         lambda x: ops.zip(
#             just_(x), from_(authors)
#         )
#     )
#     # ops.flat_map(articles)
# ).subscribe(on_next=lambda s: print(s), on_completed=lambda: print("group_by Done!\n"), on_error=lambda e: print(e))

# from_(articles).pipe(
#     ops.flat_map(lambda x: ops.zip(just(x), from_(authors).pipe(ops.filter(lambda y: y["author_id"] == x["author_id"])),
#     lambda l, r: dict(list(l.items()) + list(r.items()))))
# ).subscribe(on_next=lambda s: print(s), on_completed=lambda: print("group_by Done!\n"), on_error=lambda e: print(e))


# rx.just(articles).subscribe(
#     on_next=lambda x : print("Next: {0}".format(x)),
#     on_error=lambda e: print(e),
#     on_completed=lambda: print("Sequence complete.")
# )

a = rx.of(1, 2, 3, 4, 5)
b = rx.of("A", "B", "C")

# subscribe(
#     on_next=lambda x : print("Next: {0}".format(x)),
#     on_error=lambda e: print(e),
#     on_completed=lambda: print("Sequence complete.")
# )

articleObservable = rx.from_(articles)
authorsObservable = rx.from_(authors)

def filterById(x):
    if (x["id"] == 1):
        return x
    else:
        return ""

case2 = articleObservable.pipe(
    ops.filter(lambda d: filterById(d)),
    ops.flat_map(articleObservable)
)

case2.subscribe(
    on_next=lambda i: print("Got - {0}".format(i)),
    on_error=lambda e: print("Error : {0}".format(e)),
    on_completed=lambda: print("Job Done!"),
)

# articleObservable.pipe(
#     # ops.zip(authorsObservable),
#     # ops.merge(authorsObservable),
#     ops.filter(authorsObservable)
#     # ops.flat_map(lambda grp: grp.pipe(ops.to_list()))
#     # ops.flat_map(lambda x: ops.zip(just(x), b))  
# ).subscribe(
#     on_next = lambda x: print("Next: {0}".format(x)),
#     on_error = lambda e: print(e),
#     on_completed = lambda: print("Sequence complete.")
# )


# just(articles).subscribe(
#     on_next=lambda x: print("Next: {0}".format(x)),
#     on_error=lambda e: print(e),
#     on_completed=lambda: print("Sequence complete.")
# )


# from rx import of, operators as op
# source = of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")
# composed = source.pipe(
#     op.map(lambda s: len(s)),
#     op.filter(lambda i: i >= 5)
# )
    
# composed.subscribe(lambda value: print("Received {0}".format(value)))



# rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
#     ops.group_by(lambda s: len(s)),
#     ops.flat_map(lambda grp: grp.pipe(ops.to_list()))  
# ).subscribe(lambda i: print(i))

# c = rx.of("B", "C")
# d = rx.of("A", "B", "C")

# c.pipe(
#     ops.flat_map(d),
#     ops.distinct()  
# ).subscribe(lambda i: print(i))