import rx
from rx import operators as ops
import operator
a = rx.of(1, 2, 3, 4)
b = rx.of(2, 2, 4, 4)

a.pipe(
    ops.zip(b),  # returns a tuple with the items of a and b
    ops.map(lambda z: operator.mul(z[0], z[1]))
    ops.flat_map(lambda x: rx.range(0, x))
).subscribe(print)