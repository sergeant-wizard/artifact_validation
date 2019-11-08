import contextlib
import hashlib
import pathlib
import typing


_FileType = typing.Union[str, pathlib.Path]

class Artifact:
    def __init__(self, filename: _FileType) -> None:
        self._filename = filename

    def __str__(self) -> str:
        return str(self._filename)

    def digest(self) -> str:
        m = hashlib.md5()
        m.update(open(self._filename).read().encode('utf-8'))
        return m.hexdigest()



def check_inputs(inputs: typing.Dict[_FileType, str]) -> None:
    for inp, ahash in inputs.items():
        artifact = Artifact(inp)
        if artifact.digest() != ahash:
            message = f'Unexpected input hash for {artifact}'
            raise RuntimeError(message)


def check_outputs(outputs: typing.List[_FileType]) -> typing.List[str]:
    ret: typing.List[str] = list()
    for output in outputs:
        artifact = Artifact(output)
        ret.append(artifact.digest())
    return ret


if __name__ == '__main__':
    import tempfile

    with tempfile.NamedTemporaryFile() as train_data:
        check_inputs({
            train_data.name: 'd41d8cd98f00b204e9800998ecf8427e',
            # hash for empty file
        })

    out1 = tempfile.NamedTemporaryFile()
    out2 = tempfile.NamedTemporaryFile()

    out1.write(b'good result')
    out1.seek(0)
    out2.write(b'beter result')
    out2.seek(0)
    print(check_outputs([out1.name, out2.name]))
