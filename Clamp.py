# Clamp

# ================================================================================================ #

from typing import Any, Iterator, Optional, Tuple

# ================================================================================================ #

class Clamp:
	"""Clamps a numeric value within specified lower and upper bounds."""

	__slots__ = ("_lb", "_ub", "_cv")

	def __init__(self, lower_bound: float, current_value: float, upper_bound: float) -> None:
		self._lb = lower_bound
		self._ub = upper_bound
		self._cv = current_value

		self._enforce_bounds()

	# -------------------------------------------------------------------------
	# Dunder Methods
	# -------------------------------------------------------------------------

	def __eq__(self, other: Any) -> bool:
		# Operation: x == y
		if isinstance(other, Clamp):
			return self._cv == other._cv
		return self._cv == other

	def __lt__(self, other: Any) -> bool:
		# Operation: x < y
		if isinstance(other, Clamp):
			return self._cv < other._cv
		return self._cv < other

	def __gt__(self, other: Any) -> bool:
		# Operation: x > y
		if isinstance(other, Clamp):
			return self._cv > other._cv
		return self._cv > other
	
	def __le__(self, other: Any) -> bool:
		# Operation: x <= y
		return self.__lt__(other) or self.__eq__(other)

	def __ge__(self, other: Any) -> bool:
		# Operation: x >= y
		return self.__gt__(other) or self.__eq__(other)

	def __hash__(self) -> int:
		# Operation: hash(x)
		return hash((self._lb, self._ub, self._cv))
	
	def __repr__(self) -> str:
		# Operation: repr(x)
		return f'Clamp({self._lb}, {self._cv}, {self._ub})'

	def __str__(self) -> str:
		# Operation: str(x)
		raise NotImplementedError

	def __bool__(self) -> bool:
		# Operation: bool(x)
		raise NotImplementedError

	def __int__(self) -> int:
		# Operation: int(x)
		raise NotImplementedError

	def __float__(self) -> float:
		# Operation: float(x)
		raise NotImplementedError

	def __bytes__(self) -> bytes:
		# Operation: bytes(x)
		raise NotImplementedError

	def __complex__(self) -> complex:
		# Operation: complex(x)
		raise NotImplementedError

	def __format__(self, format_spec: str) -> str:
		# Operation: format(x, s)
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Context Managers
	# -------------------------------------------------------------------------

	def __enter__(self) -> Any:
		# Operation: with x as c:
		raise NotImplementedError

	def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
		# Operation: with x as c:
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Collections & Containers
	# -------------------------------------------------------------------------

	def __len__(self) -> int:
		# Operation: len(x)
		raise NotImplementedError

	def __iter__(self) -> Iterator[Any]:
		# Operation: iter(x)
		raise NotImplementedError

	def __getitem__(self, key: Any) -> Any:
		# Operation: x[a]
		raise NotImplementedError

	def __setitem__(self, key: Any, value: Any) -> None:
		# Operation: x[a] = b
		raise NotImplementedError

	def __delitem__(self, key: Any) -> None:
		# Operation: del x[a]
		raise NotImplementedError

	def __contains__(self, item: Any) -> bool:
		# Operation: a in x
		raise NotImplementedError

	def __reversed__(self) -> Iterator[Any]:
		# Operation: reversed(x)
		raise NotImplementedError

	def __next__(self) -> Any:
		# Operation: next(x)
		raise NotImplementedError

	def __missing__(self, key: Any) -> Any:
		# Operation: x[a] (when key is missing in dict subclasses)
		raise NotImplementedError

	def __length_hint__(self) -> int:
		# Operation: x.__length_hint__()
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Callability
	# -------------------------------------------------------------------------

	def __call__(self, *args: Any, **kwargs: Any) -> Any:
		# Operation: x()
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Arithmetic Operators
	# -------------------------------------------------------------------------

	def __add__(self, other: Any) -> Any:
		# Operation: x + y
		raise NotImplementedError

	def __radd__(self, other: Any) -> Any:
		# Operation: y + x
		raise NotImplementedError

	def __sub__(self, other: Any) -> Any:
		# Operation: x - y
		raise NotImplementedError

	def __rsub__(self, other: Any) -> Any:
		# Operation: y - x
		raise NotImplementedError

	def __mul__(self, other: Any) -> Any:
		# Operation: x * y
		raise NotImplementedError

	def __rmul__(self, other: Any) -> Any:
		# Operation: y * x
		raise NotImplementedError

	def __truediv__(self, other: Any) -> Any:
		# Operation: x / y
		raise NotImplementedError

	def __rtruediv__(self, other: Any) -> Any:
		# Operation: y / x
		raise NotImplementedError

	def __mod__(self, other: Any) -> Any:
		# Operation: x % y
		raise NotImplementedError

	def __rmod__(self, other: Any) -> Any:
		# Operation: y % x
		raise NotImplementedError

	def __floordiv__(self, other: Any) -> Any:
		# Operation: x // y
		raise NotImplementedError

	def __rfloordiv__(self, other: Any) -> Any:
		# Operation: y // x
		raise NotImplementedError

	def __pow__(self, other: Any) -> Any:
		# Operation: x ** y
		raise NotImplementedError

	def __rpow__(self, other: Any) -> Any:
		# Operation: y ** x
		raise NotImplementedError

	def __matmul__(self, other: Any) -> Any:
		# Operation: x @ y
		raise NotImplementedError

	def __rmatmul__(self, other: Any) -> Any:
		# Operation: y @ x
		raise NotImplementedError

	# Bitwise Operators
	def __and__(self, other: Any) -> Any:
		# Operation: x & y
		raise NotImplementedError

	def __rand__(self, other: Any) -> Any:
		# Operation: y & x
		raise NotImplementedError

	def __or__(self, other: Any) -> Any:
		# Operation: x | y
		raise NotImplementedError

	def __ror__(self, other: Any) -> Any:
		# Operation: y | x
		raise NotImplementedError

	def __xor__(self, other: Any) -> Any:
		# Operation: x ^ y
		raise NotImplementedError

	def __rxor__(self, other: Any) -> Any:
		# Operation: y ^ x
		raise NotImplementedError

	def __rshift__(self, other: Any) -> Any:
		# Operation: x >> y
		raise NotImplementedError

	def __rrshift__(self, other: Any) -> Any:
		# Operation: y >> x
		raise NotImplementedError

	def __lshift__(self, other: Any) -> Any:
		# Operation: x << y
		raise NotImplementedError

	def __rlshift__(self, other: Any) -> Any:
		# Operation: y << x
		raise NotImplementedError

	# Unary Operators
	def __neg__(self) -> Any:
		# Operation: -x
		raise NotImplementedError

	def __pos__(self) -> Any:
		# Operation: +x
		raise NotImplementedError

	def __invert__(self) -> Any:
		# Operation: ~x
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Math Functions
	# -------------------------------------------------------------------------

	def __divmod__(self, other: Any) -> Tuple[Any, Any]:
		# Operation: divmod(x, y)
		raise NotImplementedError

	def __rdivmod__(self, other: Any) -> Tuple[Any, Any]:
		# Operation: divmod(y, x)
		raise NotImplementedError

	def __abs__(self) -> Any:
		# Operation: abs(x)
		raise NotImplementedError

	def __index__(self) -> int:
		# Operation: x.__index__() (lossless integer conversion for slicing)
		raise NotImplementedError

	def __round__(self, n: int = 0) -> Any:
		# Operation: round(x)
		raise NotImplementedError

	def __trunc__(self) -> Any:
		# Operation: math.trunc(x)
		raise NotImplementedError

	def __floor__(self) -> Any:
		# Operation: math.floor(x)
		raise NotImplementedError

	def __ceil__(self) -> Any:
		# Operation: math.ceil(x)
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# In-Place Assignment Operators
	# -------------------------------------------------------------------------

	def __iadd__(self, other: Any) -> "Clamp":
		# Operation: x += y
		raise NotImplementedError

	def __isub__(self, other: Any) -> "Clamp":
		# Operation: x -= y
		raise NotImplementedError

	def __imul__(self, other: Any) -> "Clamp":
		# Operation: x *= y
		raise NotImplementedError

	def __itruediv__(self, other: Any) -> "Clamp":
		# Operation: x /= y
		raise NotImplementedError

	def __imod__(self, other: Any) -> "Clamp":
		# Operation: x %= y
		raise NotImplementedError

	def __ifloordiv__(self, other: Any) -> "Clamp":
		# Operation: x //= y
		raise NotImplementedError

	def __ipow__(self, other: Any) -> "Clamp":
		# Operation: x **= y
		raise NotImplementedError

	def __imatmul__(self, other: Any) -> "Clamp":
		# Operation: x @= y
		raise NotImplementedError

	def __iand__(self, other: Any) -> "Clamp":
		# Operation: x &= y
		raise NotImplementedError

	def __ior__(self, other: Any) -> "Clamp":
		# Operation: x |= y
		raise NotImplementedError

	def __ixor__(self, other: Any) -> "Clamp":
		# Operation: x ^= y
		raise NotImplementedError

	def __irshift__(self, other: Any) -> "Clamp":
		# Operation: x >>= y
		raise NotImplementedError

	def __ilshift__(self, other: Any) -> "Clamp":
		# Operation: x <<= y
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Attribute Access
	# -------------------------------------------------------------------------

	def __getattribute__(self, name: str) -> Any:
		# Operation: x.y
		raise NotImplementedError

	def __getattr__(self, name: str) -> Any:
		# Operation: x.y (fallback when __getattribute__ fails)
		raise NotImplementedError

	def __setattr__(self, name: str, value: Any) -> None:
		# Operation: x.y = z
		raise NotImplementedError

	def __delattr__(self, name: str) -> None:
		# Operation: del x.y
		raise NotImplementedError

	def __dir__(self) -> Any:
		# Operation: dir(x)
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Descriptors
	# -------------------------------------------------------------------------

	def __set_name__(self, owner: type, name: str) -> None:
		# Operation: class T: x = U() -> T.x.__set_name__(T, 'x')
		raise NotImplementedError

	def __get__(self, instance: Any, owner: Optional[type] = None) -> Any:
		# Operation: t.x
		raise NotImplementedError

	def __set__(self, instance: Any, value: Any) -> None:
		# Operation: t.x = y
		raise NotImplementedError

	def __delete__(self, instance: Any) -> None:
		# Operation: del t.x
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Class & Type Metaprogramming
	# -------------------------------------------------------------------------

	@classmethod
	def __init_subclass__(cls, **kwargs: Any) -> None:
		# Operation: class U(T): ...
		raise NotImplementedError

	def __mro_entries__(self, bases: Tuple[type, ...]) -> Tuple[type, ...]:
		# Operation: class U(x): ...
		raise NotImplementedError

	@classmethod
	def __class_getitem__(cls, item: Any) -> Any:
		# Operation: T[y] (Generic types/type hinting)
		raise NotImplementedError

	@classmethod
	def __prepare__(cls, name: str, bases: Tuple[type, ...], **kwargs: Any) -> Any:
		# Operation: type(base).__prepare__() -> Used in metaclasses
		raise NotImplementedError

	def __instancecheck__(self, instance: Any) -> bool:
		# Operation: isinstance(x, T) -> Used in metaclasses
		raise NotImplementedError

	def __subclasscheck__(self, subclass: type) -> bool:
		# Operation: issubclass(U, T) -> Used in metaclasses
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Async / Awaitable Interface
	# -------------------------------------------------------------------------

	def __await__(self) -> Iterator[Any]:
		# Operation: await x
		raise NotImplementedError

	async def __aenter__(self) -> Any:
		# Operation: async with x:
		raise NotImplementedError

	async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
		# Operation: async with x:
		raise NotImplementedError

	def __aiter__(self) -> Any:
		# Operation: async for a in x:
		raise NotImplementedError

	async def __anext__(self) -> Any:
		# Operation: async for a in x:
		raise NotImplementedError

	# -------------------------------------------------------------------------
	# Buffer Protocol
	# -------------------------------------------------------------------------

	def __buffer__(self, flags: int) -> Any:
		# Operation: memoryview(x)
		raise NotImplementedError

	def __release_buffer__(self, buffer: Any) -> None:
		# Operation: del memoryview(x)
		raise NotImplementedError
	
	# -------------------------------------------------------------------------
	# Private Methods
	# -------------------------------------------------------------------------
	
	def _enforce_bounds(self) -> None:
		self._cv = max(self._lb, min(self._cv, self._ub))

# ================================================================================================ #

if __name__ == '__main__':
	assert(Clamp(0.0, 3.0, 5.0) == 3.0)
	assert(Clamp(0.0, 3.0, 5.0) == 3)
	assert(Clamp(0.0, 3.0, 5.0) == Clamp(0.0, 3.0, 5.0))
	assert(Clamp(0.0, 5.0, 3.0) == 3.0)
	assert(Clamp(0.0, 3.0, 5.0) != Clamp(0.0, 4.0, 5.0))
	assert(Clamp(0.0, 3.0, 5.0) <= 3.0)
	assert(Clamp(0.0, 3.0, 5.0) >= 3.0)