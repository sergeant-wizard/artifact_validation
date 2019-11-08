# Artifact Validation

Keep real world artifacts tractable.

# Usage

## Installation

```
pip install git+git://github.com/sergeant-wizard/artifact_validation.git#egg=artifact_validation
```

## Usage

When you use input data in your script that you do not track in your repository,
obtain the `md5sum` of that data file to make sure the process is reproducible in the future.

```
$ md5sum inputs/input_file1
>>> 'deadbeaf01'
$ md5sum inputs/input_file2
>>> 'deadbeaf02'
```

Keep a record in your script like so:

```
import artifact_validation
artifact_validation.check_inputs({
    'inputs/input_file1': 'deadbeaf01',
    'inputs/input_file2': 'deadbeaf02',
})
```

if the files are changed for some reason a `RuntimeError` is raised.

To share your outputs,

```
import artifact_validation
artifact_validation.check_outputs(['output1', 'output2])
```

Gives you the list of `md5sum`s for each output which you can record or share to be used as inputs for the lower stream pipelines.
