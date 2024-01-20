## Endpoint Oriented Development (EOD)
>EOD is a development methodology that focuses on the endpoints of an application. It is a methodology that is based on the idea that the endpoints of an application are the most important part of the application.
### Entities:
###### Endpoint
>An endpoint is the entry point for calling an interactor.
###### Interactor
>An interactor is the entry point into the business logic.

```python
class DoSomethingInteractor:
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

    @inject
    def __init__(
        self,
        do_something_1_use_case: DoSomething1UseCase,
        do_something_2_use_case: DoSomething2UseCase,
        do_something_3_use_case: DoSomething3UseCase,
    ) -> None:
        self._do_something_1_use_case = do_something_1_use_case
        self._do_something_2_use_case = do_something_2_use_case
        self._do_something_3_use_case = do_something_3_use_case

    def __call__(self, input_: Input) -> Output:
        param_1 = input_.param_1
        param_2 = input_.param_2
        param_3 = input_.param_3

        self._do_something_1_use_case(
            input_=DoSomething1UseCase.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )
        self._do_something_2_use_case(
            input_=DoSomething2UseCase.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )
        self._do_something_3_use_case(
            input_=DoSomething3UseCase.Input(
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
```
###### Task
>A task is an isolated business algorithm that will be executed asynchronously.
###### Use Case
>A use case is an isolated business algorithm that changes the state of the system.
###### Service
>A service is an isolated business algorithm that does not change the state of the system.
###### Utility
>A utility is an isolated non-business algorithm that does not change the state of the system.
