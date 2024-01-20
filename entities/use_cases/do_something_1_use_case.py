from dataclasses import dataclass
from typing import Any

from entities.services.do_something_1_service import DoSomething1Service
from entities.services.do_something_2_service import DoSomething2Service
from entities.services.do_something_3_service import DoSomething3Service
from entities.utilities.injector import inject


class DoSomething1UseCase:
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

    class Error(Exception):
        pass

    class SomeError1(Error):
        pass

    class SomeError2(Error):
        pass

    class SomeError3(Error):
        pass

    @inject
    def __init__(
        self,
        do_something_1_service: DoSomething1Service,
        do_something_2_service: DoSomething2Service,
        do_something_3_service: DoSomething3Service,
    ) -> None:
        self._do_something_1_service = do_something_1_service
        self._do_something_2_service = do_something_2_service
        self._do_something_3_service = do_something_3_service

    def __call__(self, input_: Input) -> Output:
        param_1 = input_.param_1
        param_2 = input_.param_2
        param_3 = input_.param_3

        self._do_something_1_service(
            input_=self._do_something_1_service.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )
        self._do_something_2_service(
            input_=self._do_something_2_service.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )
        self._do_something_3_service(
            input_=self._do_something_3_service.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )

        return self.Output(
            param_1=param_1,
            param_2=param_2,
            param_3=param_3,
        )
