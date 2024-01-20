from dataclasses import dataclass
from typing import Any


class DoSomething2Service:
    @dataclass
    class Input:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass
    class Output:
        param_1: Any
        param_2: Any
        param_3: Any

    def __call__(self, input_: Input) -> Output:
        param_1 = input_.param_1
        param_2 = input_.param_2
        param_3 = input_.param_3

        # Do something 2 logic here

        return self.Output(
            param_1=param_1,
            param_2=param_2,
            param_3=param_3,
        )
