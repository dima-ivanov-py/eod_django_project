import pytest

from entities.services.do_something_3_service import DoSomething3Service


class TestDoSomething3Service:
    @pytest.fixture()
    def do_something_3_service(self) -> DoSomething3Service:
        return DoSomething3Service()

    def test_call(
        self,
        do_something_3_service: DoSomething3Service,
    ) -> None:
        # Arrange
        input_ = DoSomething3Service.Input(
            param_1=[],
            param_2={},
            param_3=None,
        )

        # Act
        response = do_something_3_service(input_)

        # Assert
        assert response.param_1 == []
        assert response.param_2 == {}
        assert response.param_3 is None
