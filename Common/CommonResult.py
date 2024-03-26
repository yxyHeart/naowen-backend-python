class CommonResult:

    @staticmethod
    def success(data):
        return {
            'code': 0,
            'data': data,
            'message': 'success'
        }

    @staticmethod
    def fail(message):
        return {
            'code': 500,
            'data': None,
            'message': message
        }