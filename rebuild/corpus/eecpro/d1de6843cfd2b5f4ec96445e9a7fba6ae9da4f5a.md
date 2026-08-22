# ifError(Block block)

If an error occurs the result of the formula given with the argument block is returned.

| ifError(Block block) | | | |
| --- | --- | --- | --- |
| Argument | Block | block | Formula, which returns an alternative result. |
| Return value |  |  | |

### [ClosedExamples](javascript:void(0);)

| Formula | Result |
| --- | --- |
| =List{null,1,2}.first.ifError('An error occurred!') | <<null>> |