## Endpoint-oriented Development (EOD)
>Endpoint-oriented development is an approach in which each endpoint encapsulates all the necessary business logic and is maximally isolated from other endpoints.
### Entities:
###### Endpoint
>An endpoint is a controller in the MVC pattern.
>* Endpoint can call not more than one interactor.
>* Endpoint can serve only one HTTP method.
```python
# POST: api/v1/do-something/ {"param_1": ..., "param_2": ..., "param_3": ...}
class DoSomethingEndpoint(APIView):
    def post(self, request):
        do_something_interactor = DoSomethingInteractor()
        do_something_interactor_request = do_something_interactor.Request(
            param_1=request.POST["param_1"],
            param_2=request.POST["param_2"],
            param_3=request.POST["param_3"],
        )

        try:
            do_something_interactor_response = do_something_interactor.execute(
                request=do_something_interactor_request,
            )
        except do_something_interactor.Error as e:
            response = Response(
                data=present_error(e),
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            response = Response(
                data={
                    "param_1": do_something_interactor_response.param_1,
                    "param_2": do_something_interactor_response.param_2,
                    "param_3": do_something_interactor_response.param_3,
                },
                status=status.HTTP_200_OK,
            )

        return response


# GET: api/v1/get-something/?param_1=...&param_2=...&param_3=...
class GetSomethingEndpoint(APIView):
    def get(self, request):
        get_something_interactor = GetSomethingInteractor()
        get_something_interactor_request = get_something_interactor.Request(
            param_1=request.query_params.get("param_1"),
            param_2=request.query_params.get("param_2"),
            param_3=request.query_params.get("param_3"),
        )

        try:
            get_something_interactor_response = get_something_interactor.execute(
                request=get_something_interactor_request,
            )
        except get_something_interactor.Error as e:
            response = Response(
                data=present_error(e),
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            response = Response(
                data={
                    "param_1": get_something_interactor_response.param_1,
                    "param_2": get_something_interactor_response.param_2,
                    "param_3": get_something_interactor_response.param_3,
                },
                status=status.HTTP_200_OK,
            )

        return response
```
###### Interactor
>An interactor is the entry point into the business logic.
>* Interactor can depend on any amount of other entities but not on any other interactor.
```python
class DoSomethingInteractor:
    @dataclass(frozen=True)
    class Request:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Response:
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
        # Here can be any amount of tasks, use cases, services and selectors as dependencies.
        do_something_task: DoSomethingTask,
        do_something_use_case: DoSomethingUseCase,
        do_something_service: DoSomethingService,
        get_something_selector: GetSomethingSelector,
    ) -> None:
        self._do_something_task = do_something_task
        self._do_something_use_case = do_something_use_case
        self._do_something_service = do_something_service
        self._get_something_selector = get_something_selector

    def execute(self, request: Request) -> Response:
        param_1 = request.param_1
        param_2 = request.param_2
        param_3 = request.param_3

        # Here can be any additional business logic.

        do_something_task_response = self._do_something_task.execute(
            request=self._do_something_task.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be any additional business logic.

        do_something_use_case_response = self._do_something_use_case.execute(
            request=self._do_something_use_case.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be any additional business logic.

        do_something_service_response = self._do_something_service.execute(
            request=self._do_something_service.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be any additional business logic.

        get_something_selector_response = self._get_something_selector.execute(
            request=self._get_something_selector.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be any additional business logic.

        return self.Response(
            param_1=ANY,
            param_2=ANY,
            param_3=ANY,
        )
```
###### Task
>A task is an isolated business algorithm that calls one or more background tasks.
```python
class DoSomethingTask:
    @dataclass(frozen=True)
    class Request:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Response:
        param_1: Any
        param_2: Any
        param_3: Any

    @inject
    def __init__(
        self,
        # Here can be any amount of use cases, services and selectors as dependencies.
        do_something_use_case: DoSomethingUseCase,
        do_something_service: DoSomethingService,
        get_something_selector: GetSomethingSelector,
    ) -> None:
        self._do_something_use_case = do_something_use_case
        self._do_something_service = do_something_service
        self._get_something_selector = get_something_selector

    def execute(self, request: Request) -> Response:
        param_1 = request.param_1
        param_2 = request.param_2
        param_3 = request.param_3

        # Here can be call of a background task.
        # do_something_task.delay(...)

        do_something_use_case_response = self._do_something_use_case.execute(
            request=self._do_something_use_case.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be call of a background task.
        # do_something_task.delay(...)

        do_something_service_response = self._do_something_service.execute(
            request=self._do_something_service.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be call of a background task.
        # do_something_task.delay(...)

        get_something_selector_response = self._get_something_selector.execute(
            request=self._get_something_selector.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be call of a background task.
        # do_something_task.delay(...)

        return self.Response(
            param_1=ANY,
            param_2=ANY,
            param_3=ANY,
        )
```
###### Use Case
>A use case is an isolated business algorithm that changes the state of the database.
```python
class DoSomethingUseCase:
    @dataclass(frozen=True)
    class Request:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Response:
        param_1: Any
        param_2: Any
        param_3: Any

    @inject
    def __init__(
        self,
        # Here can be any amount of services and selectors as dependencies.
        do_something_service: DoSomethingService,
        get_something_selector: GetSomethingSelector,
    ) -> None:
        self._do_something_service = do_something_service
        self._get_something_selector = get_something_selector

    def execute(self, request: Request) -> Response:
        param_1 = request.param_1
        param_2 = request.param_2
        param_3 = request.param_3

        # Here can be logic that changes the state of the database.
        # Something.objects.create(...)

        do_something_service_response = self._do_something_service.execute(
            request=self._do_something_service.Request(
                param_1=get_something_selector_response.param_1,
                param_2=get_something_selector_response.param_2,
                param_3=get_something_selector_response.param_3,
            )
        )

        # Here can be logic that changes the state of the database.
        # Something.objects.create(...)

        get_something_selector_response = self._get_something_selector.execute(
            request=self._get_something_selector.Request(
                param_1=param_1,
                param_2=param_2,
                param_3=param_3,
            )
        )

        # Here can be logic that changes the state of the database.
        # Something.objects.create(...)

        return self.Response(
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
    class Request:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Response:
        param_1: Any
        param_2: Any
        param_3: Any

    @inject
    def __init__(
        self,
        # Here can be any amount of selectors as dependencies.
        get_something_selector: GetSomethingSelector,
    ) -> None:
        self._get_something_selector = get_something_selector

    def execute(self, request: Request) -> Response:
        param_1 = request.param_1
        param_2 = request.param_2
        param_3 = request.param_3

        # Here can be logic that does not change the state of the database, but performs some requests to external APIs, for example.
        # requests.get(...)

        get_something_selector_response = self._get_something_selector.execute(
            request=self._get_something_selector.Request(
                param_1=ANY,
                param_2=ANY,
                param_3=ANY,
            )
        )

        # Here can be logic that does not change the state of the database, but performs some requests to external APIs, for example.
        # requests.get(...)

        return self.Response(
            param_1=ANY,
            param_2=ANY,
            param_3=ANY,
        )
```
###### Selector
>A selector is a complex query to a database that does not alter its state and is encapsulated in a separate function for subsequent reuse.
```python
class GetSomethingsSelector:
    @dataclass(frozen=True)
    class Request:
        param_1: Any
        param_2: Any
        param_3: Any

    @dataclass(frozen=True)
    class Response:
        somethings: QuerySet[Something]

    def execute(self, request: Request) -> Response:
        param_1 = request.param_1
        param_2 = request.param_2
        param_3 = request.param_3

        somethings = Something.objects.filter(
            param_1=param_1,
            param_2=param_2,
            param_3=param_3,
        )

        return self.Response(somethings)


class GetSomethingByIdSelector:
    @dataclass(frozen=True)
    class Request:
        something_id: int

    @dataclass(frozen=True)
    class Response:
        something: Something

    def execute(self, request: Request) -> Response:
        something_id = request.something_id

        something = Something.objects.get(id=something_id)

        return self.Response(something)


class GetFullNameOfSomethingByIdSelector:
    @dataclass(frozen=True)
    class Request:
        something_id: int

    @dataclass(frozen=True)
    class Response:
        first_name: str
        last_name: str
        full_name: str

    def execute(self, request: Request) -> Response:
        something_id = request.something_id

        something = Something.objects.get(id=something_id)
        first_name = something.first_name
        last_name = something.last_name
        full_name = f"{first_name} {last_name}"

        return self.Response(
            first_name=something.first_name,
            last_name=something.last_name,
            full_name=full_name,
        )
```
###### Utility
>A utility is an isolated non-business algorithm that does not change the state of the database.
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
