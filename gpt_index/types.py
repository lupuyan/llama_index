from typing import Generator, Union, List

RESPONSE_TEXT_TYPE = Union[str, Generator]

RESPONSE_CHUNK_TYPE = tuple[str | Generator | None, list[str]]
