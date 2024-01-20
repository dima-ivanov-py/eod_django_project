import pytest

from services.do_something_2_service import DoSomething2Service


class TestDoSomething2Service:
    @pytest.fixture()
    def do_something_2_service(self) -> DoSomething2Service:
        return DoSomething2Service()

    def test_call(
        self,
        do_something_2_service: DoSomething2Service,
    ) -> None:
        # Arrange
        input_ = DoSomething2Service.Input(
            param_1=1,
            param_2=2,
            param_3=3,
        )

        # Act
        response = do_something_2_service(input_)

        # Assert
        assert response.param_1 == 1
        assert response.param_2 == 2
        assert response.param_3 == 3
