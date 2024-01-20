from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GetSomething1View(APIView):
    def get(self, request):
        param_1 = request.query_params.get("param_1")
        param_2 = request.query_params.get("param_2")
        param_3 = request.query_params.get("param_3")

        return Response(
            data={
                "param_1": param_1,
                "param_2": param_2,
                "param_3": param_3,
            },
            status=status.HTTP_200_OK,
        )
