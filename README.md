## Endpoint-oriented Development (EOD)
>Endpoint-oriented development is an approach in which each endpoint encapsulates all the necessary business logic and is maximally isolated from other endpoints.
### Entities:
###### Endpoint
>An endpoint is the entry point for calling an interactor.
```python
class DoSomethingView(APIView):
    def post(self, request):
        do_something_interactor = DoSomethingInteractor()
        input_ = do_something_interactor.Input(
            param_1=request.POST["param_1"],
            param_2=request.POST["param_2"],
            param_3=request.POST["param_3"],
        )

        try:
            output = do_something_interactor(input_)
        except do_something_interactor.Error as e:
            response = Response(
                data=present_error(e),
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            response = Response(
                data={
                    "param_1": output.param_1,
                    "param_2": output.param_2,
                    "param_3": output.param_3,
                },
                status=status.HTTP_200_OK,
            )

        return response


class GetSomethingView(APIView):
    def get(self, request):
        get_something_interactor = GetSomethingInteractor()
        input_ = get_something_interactor.Input(
            param_1=request.query_params.get("param_1"),
            param_2=request.query_params.get("param_2"),
            param_3=request.query_params.get("param_3"),
        )

        try:
            output = get_something_interactor(input_)
        except get_something_interactor.Error as e:
            response = Response(
                data=present_error(e),
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            response = Response(
                data={
                    "param_1": output.param_1,
                    "param_2": output.param_2,
                    "param_3": output.param_3,
                },
                status=status.HTTP_200_OK,
            )

        return response
```
###### Interactor
>An interactor is the entry point into the business logic.
```python
class DoSomethingInteractor:
    @dataclass(frozen=True)
    class Input:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Output:
        param_1: Any
        param_2: Any
        param_3: Any

    class Error(Exception):
        ...

    class SomeError1(Error):
        ...

    class SomeError2(Error):
        ...

    class SomeError3(Error):
        ...

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

        # Here can be any additional logic.

        get_something_selector_output = self._get_something_selector(
            input_=self._get_something_selector.Input(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be any additional logic.

        do_something_service_output = self._do_something_service(
            input_=self._do_something_service.Input(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be any additional logic.

        do_something_use_case_output = self._do_something_use_case(
            input_=self._do_something_use_case.Input(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be any additional logic.

        return self.Output(
            param_1=ANY,
            param_2=ANY,
            param_3=ANY,
        )
```
###### Task
>A task is an isolated business algorithm that will be executed asynchronously.
###### Use Case
>A use case is an isolated business algorithm that changes the state of the database.
```python
class DoSomethingUseCase:
    @dataclass(frozen=True)
    class Input:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
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

        # Here can be logic that changes the state of the database.
        # Something.objects.create(...)

        get_something_selector_output = self._get_something_selector(
            input_=self._get_something_selector.Input(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )

        # Here can be logic that changes the state of the database.
        # Something.objects.create(...)

        do_something_service_output = self._do_something_service(
            input_=self._do_something_service.Input(
                param_1=get_something_selector_output.param_1,
                param_2=get_something_selector_output.param_2,
                param_3=get_something_selector_output.param_3,
            )
        )

        # Here can be logic that changes the state of the database.
        # Something.objects.create(...)

        return self.Output(
            param_1=ANY,
            param_2=ANY,
            param_3=ANY,
        )
```
###### Service
>A service is an isolated business algorithm that does not change the state of the database.
```python
class DoSomethingService:
    @dataclass(frozen=True)
    class Input:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Output:
        param_1: Any
        param_2: Any
        param_3: Any

    @inject
    def __init__(
        self,
        get_something_selector: GetSomethingSelector,
    ) -> None:
        self._get_something_selector = get_something_selector

    def __call__(self, input_: Input) -> Output:
        param_1 = input_.param_1
        param_2 = input_.param_2
        param_3 = input_.param_3

        # Here can be logic that does not change the state of the database, but performs some requests to external APIs, for example.
        # requests.get(...)

        get_something_selector_output = self._get_something_selector(
            input_=self._get_something_selector.Input(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be logic that does not change the state of the database, but performs some requests to external APIs, for example.
        # requests.get(...)

        return self.Output(
            param_1=ANY,
            param_2=ANY,
            param_3=ANY,
        )
```
###### Selector
>A selector is a complex query to a database that does not alter its state and is encapsulated in a separate function for subsequent reuse.
```python
class GetSomethingSelector:
    @dataclass(frozen=True)
    class Input:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Output:
        somethings: QuerySet[Something]

    def __call__(self, input_: Input) -> Output:
        param_1 = input_.param_1
        param_2 = input_.param_2
        param_3 = input_.param_3

        somethings = Something.objects.filter(
            param_1=param_1,
            param_2=param_2,
            param_3=param_3,
        )

        return self.Output(somethings=somethings)


class GetSomethingByIdSelector:
    @dataclass(frozen=True)
    class Input:
        something_id: int

    @dataclass(frozen=True)
    class Output:
        something: Something

    def __call__(self, input_: Input) -> Output:
        something_id = input_.something_id

        something = Something.objects.get(id=something_id)

        return self.Output(something=something)


class GetFullNameOfSomethingByIdSelector:
    @dataclass(frozen=True)
    class Input:
        something_id: int

    @dataclass(frozen=True)
    class Output:
        first_name: str
        last_name: str
        full_name: str

    def __call__(self, input_: Input) -> Output:
        something_id = input_.something_id

        something = Something.objects.get(id=something_id)
        first_name = something.first_name
        last_name = something.last_name
        full_name = f"{first_name} {last_name}"

        return self.Output(
            first_name=something.first_name,
            last_name=something.last_name,
            full_name=full_name,
        )
```
###### Utility
>A utility is an isolated non-business algorithm that does not change the state of the system.
```python
from functools import wraps
from typing import get_type_hints


class Injector:
    type_kwargs = {}

    @staticmethod
    def register(type_, **kwargs):
        Injector.type_kwargs[type_.__name__] = kwargs

    @staticmethod
    def get_instance(type_):
        kwargs = Injector.type_kwargs.get(type_.__name__, {})
        return type_(**kwargs)


def inject(method):
    @wraps(method)
    def wrapper(self, **kwargs):
        type_name = type(self).__name__
        kwargs = Injector.type_kwargs.get(type_name, {}) | kwargs
        type_hints = get_type_hints(method)
        type_hints.pop("return", None)

        for param, type_ in type_hints.items():
            instance = kwargs.get(param)

            if instance is None:
                instance = Injector.get_instance(type_)

            kwargs[param] = instance

        return method(self, **kwargs)

    return wrapper


def present_error(error: Exception) -> dict[str, str]:
    return {"error": str(error)}
```
