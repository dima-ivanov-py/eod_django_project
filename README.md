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
        get_something_selector: GetSomethingSelector,
        do_something_service: DoSomethingService,
        do_something_use_case: DoSomethingUseCase,
    ) -> None:
        self._get_something_selector = get_something_selector
        self._do_something_service = do_something_service
        self._do_something_use_case = do_something_use_case

    def __call__(self, input_: Input) -> Output:
        param_1 = input_.param_1
        param_2 = input_.param_2
        param_3 = input_.param_3

        get_something_selector_output = self._get_something_selector(
            input_=self._get_something_selector.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )
        do_something_service_output = self._do_something_service(
            input_=self._do_something_service.Input(
                param_1=do_something_selector_output.param_1,
                param_2=do_something_selector_output.param_2,
                param_3=do_something_selector_output.param_3,
            )
        )
        do_something_use_case_output = self._do_something_use_case(
            input_=self._do_something_use_case.Input(
                param_1=do_something_service_output.param_1,
                param_2=do_something_service_output.param_2,
                param_3=do_something_service_output.param_3,
            )
        )

        return self.Output(
            param_1=do_something_use_case_output.param_1,
            param_2=do_something_use_case_output.param_2,
            param_3=do_something_use_case_output.param_3,
        )
```
###### Task
>A task is an isolated business algorithm that will be executed asynchronously.
###### Use Case
>A use case is an isolated business algorithm that changes the state of the system.
```python
class DoSomethingUseCase:
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
        get_something_selector: GetSomethingSelector,
        do_something_service: DoSomethingService,
    ) -> None:
        self._get_something_selector = get_something_selector
        self._do_something_service = do_something_service

    def __call__(self, input_: Input) -> Output:
        param_1 = input_.param_1
        param_2 = input_.param_2
        param_3 = input_.param_3

        get_something_selector_output = self._get_something_selector(
            input_=self._get_something_selector.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )
        do_something_service_output = self._do_something_service(
            input_=self._do_something_service.Input(
                param_1=get_something_selector_output.param_1,
                param_2=get_something_selector_output.param_2,
                param_3=get_something_selector_output.param_3,
            )
        )

        return self.Output(
            param_1=do_something_service_output.param_1,
            param_2=do_something_service_output.param_2,
            param_3=do_something_service_output.param_3,
        )
```
###### Service
>A service is an isolated business algorithm that does not change the state of the system.
###### Utility
>A utility is an isolated non-business algorithm that does not change the state of the system.
